from pyValkLib.utils.Compression.integers import compressInt, decompressInt
from pyValkLib.utils.Compression.integers import compressSubStencil, decompressSubStencil
from pyValkLib.utils.Compression.Stencilled import SCRelRep, SCAbsRep, SCUnpackedRep
from pyValkLib.utils.Compression.Stencilled.common import SCTemplateComponent
from pyValkLib.utils.Compression.Stencilled.relative import SCRelativeTemplateGenerator
from pyValkLib.utils.Compression.Stencilled.unpacked import SCUnpackedTemplateComponents, SCTemplate, SCTemplatePack
from pyValkLib.utils.Compression.Stencilled.validation import flattenStencil, compareStencil
from pyValkLib.utils.Compression.Stencilled.validation import Validator
from pyValkLib.serialisation.ReadWriter import ENRSBuilder

class ENRSRelRep(SCRelRep):
    @property
    def classname(self):
        return "ENRSRelRep"
        
    @property
    def absclass(self):
        return ENRSAbsRep
    
class ENRSAbsRep(SCAbsRep):
    @property
    def classname(self):
        return "ENRSAbsRep"
        
    @property
    def relclass(self):
        return ENRSRelRep
        
    @property
    def unpackedclass(self):
        return ENRSUnpackedRep
        
    @property
    def utcclass(self):
        return ENRSUnpackedTemplateComponents
    
    
class ENRSUnpackedRep(SCUnpackedRep):
    @property
    def component_type(self):
        return ENRSTemplateComponent

    @property
    def classname(self):
        return "ENRSUnpackedRep"

    @property
    def absclass(self):
        return ENRSAbsRep
    
class ENRSTemplateComponent(SCTemplateComponent):
    @property
    def classname(self):
        return "ENRSTemplateComponent"
            
    def get_item_size(self):
        if self.type == 0:
            return 0x02
        elif self.type == 1:
            return 0x04
        elif self.type == 2:
            return 0x08
        else:
            raise ValueError(f"Invalid type: {self.type}")
        
    
class ENRSUnpackedTemplateComponents(SCUnpackedTemplateComponents):
    def __repr__(self):
        return f"<ENRS UTC>{{{self.type}}} {list(self.values)}</ENRS UTC>"
    
    def get_type_sizes(self):
        return {0: 0x02,
                1: 0x04,
                2: 0x08}
    
    @property
    def classname(self):
        return "ENRS UTC"
    
def decompressENRS(num_groups, data):
    ENRS_iter_data = iter(data)
    out = ENRSRelRep()
    
    for _ in range(num_groups):
        jump_from_previous_group = decompressInt(ENRS_iter_data)
        num_sub_stencils = decompressInt(ENRS_iter_data)
        stencil_size = decompressInt(ENRS_iter_data)
        stencil_repetitions = decompressInt(ENRS_iter_data)

        sub_stencil_defs = []
        for j in range(num_sub_stencils):
            jump, stride = decompressSubStencil(ENRS_iter_data)
            count = decompressInt(ENRS_iter_data)
            sub_stencil_defs.append(ENRSTemplateComponent(jump, count, stride))
            
        cgen = SCRelativeTemplateGenerator(jump_from_previous_group, stencil_size, stencil_repetitions,
                                           sub_stencil_defs)
        out.append(cgen)
        
    return out.to_abs_rep().to_unpacked_rep()

def compressENRS(enrs_unpacked_rep):
    out = []
    
    enrs_rel_rep = enrs_unpacked_rep.to_abs_rep().to_rel_rep()
    for tg in enrs_rel_rep:
        out.extend(compressInt(tg.jump))
        out.extend(compressInt(len(tg.subs)))
        out.extend(compressInt(tg.stride))
        out.extend(compressInt(tg.count))
        
        for comp in tg:
            out.extend(compressSubStencil(comp.stride, comp.type))
            out.extend(compressInt(comp.count))

    n_to_extend = (0x10 - (len(out) % 0x10)) % 0x10
    out += [0]*n_to_extend
    return out

def toENRSPackedRep(data):
    out = ENRSUnpackedRep()
    
    for tpack_data in data:
        templates = []
        for template_data in tpack_data:
            template = SCTemplate()
            for comp_data in template_data:
                template.append(ENRSUnpackedTemplateComponents(comp_data, comp_data.get_item_size() >> 2))
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

def buildENRS(ctr):
    eb = ENRSBuilder(ctr.context.endianness)
    eb.anchor_pos = -ctr.header.header_length
    ctr.read_write_contents(eb)
    
    return eb.pointers

def compareENRS(ctr_1, ctr_2, print_errs=True):
    compareStencil(ctr_1, ctr_2, lambda x: x.ENRS, decompressENRS, compressENRS, buildENRS, toENRSPackedRep, print_errs)

def validateENRS(pointers, print_errs=False):
    reference_enrs = flattenStencil(pointers)
    
    # Test if moving to structure works
    enrs_test_1 = toENRSPackedRep(pointers)
    enrs_test_1 = enrs_test_1.flatten()
    if enrs_test_1 != reference_enrs:
        for i, (c1, c2) in enumerate(zip(reference_enrs, enrs_test_1)):
            if print_errs:
                print("> ENRS TEST 1", i, c1, "---", c2)
            
            if c1 != c2:
                print(f"Critical ENRS Structural Error: {i} {c1} --- {c2}")
                raise Exception()
                
    # Test if moving to AbsRep works
    enrs_test_2 = toENRSPackedRep(pointers)
    enrs_test_2 = enrs_test_2.to_abs_rep().to_unpacked_rep()
    enrs_test_2 = flattenStencil(enrs_test_2)
    if enrs_test_2 != reference_enrs:
        for i, (c1, c2) in enumerate(zip(reference_enrs, enrs_test_2)):
            if print_errs:
                print("> ENRS TEST 2", i, c1, "---", c2)
            
            if c1 != c2:
                print(f"Critical ENRS AbsRep Error: {i} {c1} --- {c2}")
                raise Exception()   
                
    # Test if moving to RelRep works
    enrs_test_2 = toENRSPackedRep(pointers)
    enrs_test_2 = enrs_test_2.to_abs_rep().to_rel_rep().to_abs_rep().to_unpacked_rep()
    enrs_test_2 = flattenStencil(enrs_test_2)
    if enrs_test_2 != reference_enrs:
        for i, (c1, c2) in enumerate(zip(reference_enrs, enrs_test_2)):
            if print_errs:
                print("> ENRS TEST 3", i, c1, "---", c2)
            
            if c1 != c2:
                print(f"Critical ENRS RelRep Error: {i} {c1} --- {c2}")
                raise Exception()   
                
    # Test if compressing and decompressing works
    enrs_test_3 = toENRSPackedRep(pointers)
    enrs_test_3 = compressENRS(enrs_test_3)
    enrs_test_3 = decompressENRS(len(pointers), enrs_test_3).flatten()
    
    if enrs_test_3 != reference_enrs:
        for i, (c1, c2) in enumerate(zip(reference_enrs, enrs_test_3)):
            if print_errs:
                print("> ENRS TEST 4", i, c1, "---", c2)
            
            if c1 != c2:
                print(f"Critical ENRS Compression Error: {i} {c1} --- {c2}")
                raise Exception()

class ENRSValidator(Validator):
    def __init__(self, ctr, print_errs=True):
        super().__init__(lambda: compareENRS(ctr, ctr, print_errs))