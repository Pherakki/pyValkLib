from pyValkLib.utils.Compression.integers import compressInt, decompressInt
from pyValkLib.utils.Compression.integers import compressSubStencil, decompressSubStencil
from pyValkLib.utils.Compression.Stencilled import SCRelRep, SCAbsRep, SCUnpackedRep
from pyValkLib.utils.Compression.Stencilled.common import SCTemplateComponent
from pyValkLib.utils.Compression.Stencilled.relative import SCRelativeTemplateGenerator
from pyValkLib.utils.Compression.Stencilled.unpacked import SCUnpackedTemplateComponents, SCTemplate, SCTemplatePack
from pyValkLib.utils.Compression.Stencilled.validation import flattenStencil, compareStencil, validateStencil
from pyValkLib.utils.Compression.Stencilled.validation import Validator
from pyValkLib.serialisation.ReadWriter import MTXSBuilder

class MTXSRelRep(SCRelRep):
    @property
    def classname(self):
        return "MTXSRelRep"
        
    @property
    def absclass(self):
        return MTXSAbsRep
    
class MTXSAbsRep(SCAbsRep):
    @property
    def classname(self):
        return "MTXSAbsRep"
        
    @property
    def relclass(self):
        return MTXSRelRep
        
    @property
    def unpackedclass(self):
        return MTXSUnpackedRep
        
    @property
    def utcclass(self):
        return MTXSUnpackedTemplateComponents
    
    
class MTXSUnpackedRep(SCUnpackedRep):
    @property
    def component_type(self):
        return MTXSTemplateComponent

    @property
    def classname(self):
        return "MTXSUnpackedRep"

    @property
    def absclass(self):
        return MTXSAbsRep
    
class MTXSTemplateComponent(SCTemplateComponent):
    @property
    def classname(self):
        return "MTXSTemplateComponent"
            
    def get_item_size(self):
        if self.type == 0:
            return 0x40
        else:
            raise ValueError(f"Invalid type: {self.type}")
        
    
class MTXSUnpackedTemplateComponents(SCUnpackedTemplateComponents):
    def __repr__(self):
        return f"<MTXS UTC>{{{self.type}}} {list(self.values)}</MTXS UTC>"
    
    def get_type_sizes(self):
        return {0: 0x40}
    
    @property
    def classname(self):
        return "MTXS UTC"
    
def decompressMTXS(num_groups, data):
    MTXS_iter_data = iter(data)
    out = MTXSRelRep()
    
    for _ in range(num_groups):
        jump_from_previous_group = decompressInt(MTXS_iter_data) << 4
        num_sub_stencils = decompressInt(MTXS_iter_data)
        stencil_size = decompressInt(MTXS_iter_data) << 4
        stencil_repetitions = decompressInt(MTXS_iter_data)

        sub_stencil_defs = []
        for j in range(num_sub_stencils):
            jump, stride = decompressSubStencil(MTXS_iter_data)
            count = decompressInt(MTXS_iter_data)
            sub_stencil_defs.append(MTXSTemplateComponent(jump, count, stride))
            
        cgen = SCRelativeTemplateGenerator(jump_from_previous_group, stencil_size, stencil_repetitions,
                                           sub_stencil_defs)
        out.append(cgen)
        
    return out.to_abs_rep().to_unpacked_rep()

def compressMTXS(MTXS_unpacked_rep):
    out = []
    
    MTXS_rel_rep = MTXS_unpacked_rep.to_abs_rep().to_rel_rep()
    for tg in MTXS_rel_rep:
        out.extend(compressInt(tg.jump >> 4))
        out.extend(compressInt(len(tg.subs)))
        out.extend(compressInt(tg.stride >> 4))
        out.extend(compressInt(tg.count))
        
        for comp in tg:
            out.extend(compressSubStencil(comp.stride, comp.type))
            out.extend(compressInt(comp.count))

    n_to_extend = (0x10 - (len(out) % 0x10)) % 0x10
    out += [0]*n_to_extend
    return out

def toMTXSPackedRep(data):
    out = MTXSUnpackedRep()
    
    for tpack_data in data:
        templates = []
        for template_data in tpack_data:
            template = SCTemplate()
            for comp_data in template_data:
                template.append(MTXSUnpackedTemplateComponents(comp_data, comp_data.type))
            templates.append(template)
        
        # Shouldn't need to calculate this, should receive it..!!!
        if len(templates) > 1:
            stride = templates[1].get_first_offset() - templates[0].get_first_offset()
        else:
            stride = 1 # Wrong, but probably doesn't matter?
            
        tpack = SCTemplatePack(stride)
        
        for template in templates:
            tpack.append(template)
        out.append(tpack)

    return out

##############
# VALIDATION #
##############

def buildMTXS(ctr):
    mb = MTXSBuilder()
    mb.anchor_pos = -ctr.header.header_length
    mb.mark_new_contents_array()
    ctr.read_write_contents(mb)
    mb.mark_new_contents_array()
    
    return mb.pointers

def compareMTXS(ctr_1, ctr_2, print_errs=True):
    compareStencil(ctr_1, ctr_2, lambda x: x.MTXS, decompressMTXS, compressMTXS, buildMTXS, toMTXSPackedRep, print_errs)

def validateMTXS(pointers, print_errs=False):
    validateStencil(pointers, "MTXS", toMTXSPackedRep, compressMTXS, decompressMTXS, print_errs)

class MTXSValidator(Validator):
    def __init__(self, ctr, print_errs=True):
        super().__init__(lambda: compareMTXS(ctr, ctr, print_errs))