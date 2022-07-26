from .Representations import CCRSRelRep, CCRSRelativeTemplateGenerator, CCRSTemplateComponent
from .Representations import CCRSUnpackedRep, CCRSTemplatePack, CCRSTemplate, CCRSUnpackedTemplateComponents

from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH


class CCRSReadWriter(ValkSerializable32BH):
    FILETYPE = "CCRS"
    
    __slots__ = ("padding_0x20", "num_groups", "data")
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        
        # Data holders
        self.padding_0x20 = 0
        self.num_groups = None
        self.data = None
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))
        self.padding_0x20 = rw.rw_uint32(self.padding_0x20)
        self.num_groups   = rw.rw_uint32(self.num_groups)
        rw.align(rw.local_tell(), 0x10)
        
        rw.assert_is_zero(self.padding_0x20)
        self.data = rw.rw_uint8s(self.data, self.header.data_length - 0x10, endianness='<')
        
def pull_bytecode(ENRS_iter, byte_power, bytecode_value):
    for _ in range((1 << byte_power) - 1):
        elem = next(ENRS_iter)
        bytecode_value <<= 8
        bytecode_value |= elem
        
    return bytecode_value

def decompressInt(ENRS_iter):
    elem = next(ENRS_iter)
    byte_power = elem >> 6
    bytecode_value = elem & 0x3F
    
    return pull_bytecode(ENRS_iter, byte_power, bytecode_value)

def compressInt(integer):
    data = []
    if integer < 2**6:
        power_val = 0x00
        
        byte_1 = (integer & 0x3F) >> 0x00
        
        data.append(power_val | byte_1)
    elif integer < 2**14:
        power_val = 0x40
        
        byte_1 = (integer & 0x3F00) >> 0x08
        byte_2 = (integer & 0x00FF) >> 0x00
        
        data.append(power_val | byte_1)
        data.append(byte_2)
    elif integer < 2**30:
        power_val = 0x80
        
        byte_1 = (integer & 0x3F000000) >> 0x18
        byte_2 = (integer & 0x00FF0000) >> 0x10
        byte_3 = (integer & 0x0000FF00) >> 0x08
        byte_4 = (integer & 0x000000FF) >> 0x00
        
        data.append(power_val | byte_1)
        data.append(byte_2)
        data.append(byte_3)
        data.append(byte_4)
    else:
        raise ValueError(f"Int can be no larger than 2**30: {integer}.")
    return data

def decompressCCRS(num_groups, data):
    CCRS_iter_data = iter(data)
    out = CCRSRelRep()
    
    for _ in range(num_groups):
        jump_from_previous_group = decompressInt(CCRS_iter_data)
        num_sub_stencils = decompressInt(CCRS_iter_data)
        stencil_size = decompressInt(CCRS_iter_data)
        stencil_repetitions = decompressInt(CCRS_iter_data)

        sub_stencil_defs = []
        for j in range(num_sub_stencils):
            sub_stencil_defs.append(CCRSTemplateComponent(decompressInt(CCRS_iter_data), 
                                                          decompressInt(CCRS_iter_data), 
                                                          decompressInt(CCRS_iter_data)))
            
        cgen = CCRSRelativeTemplateGenerator(jump_from_previous_group, stencil_size, stencil_repetitions,
                                             sub_stencil_defs)
        out.append(cgen)
        
    return out.to_abs_rep().to_unpacked_rep()

def compressCCRS(ccrs_unpacked_rep):
    out = []
    
    ccrs_rel_rep = ccrs_unpacked_rep.to_abs_rep().to_rel_rep()
    for tg in ccrs_rel_rep:
        out.extend(compressInt(tg.jump))
        out.extend(compressInt(len(tg.subs)))
        out.extend(compressInt(tg.stride))
        out.extend(compressInt(tg.count))
        
        for comp in tg:
            out.extend(compressInt(comp.stride))
            out.extend(compressInt(comp.count))
            out.extend(compressInt(comp.type))
        
    return out

def toCCRSPackedRep(data):
    out = CCRSUnpackedRep()
    
    for tpack_data in data:
        templates = []
        for template_data in tpack_data:
            template = CCRSTemplate()
            for comp_type, comp_data in template_data:
                template.append(CCRSUnpackedTemplateComponents(comp_data, comp_type))
            templates.append(template)
        
        # Shouldn't need to calculate this, should receive it..!!!
        if len(templates) > 1:
            stride = templates[1].get_first_offset() - templates[0].get_first_offset()
        else:
            stride = 1 # Wrong, but probably doesn't matter?
            
        tpack = CCRSTemplatePack(stride)
        
        for template in templates:
            tpack.append(template)
        out.append(tpack)

    return out