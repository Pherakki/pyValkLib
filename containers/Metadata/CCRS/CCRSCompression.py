from pyValkLib.utils.Compression.integers import compressInt, decompressInt
from pyValkLib.utils.Compression.integers import compressSubStencil, decompressSubStencil
from pyValkLib.utils.Compression.Stencilled import SCRelRep, SCAbsRep, SCUnpackedRep
from pyValkLib.utils.Compression.Stencilled.common import SCTemplateComponent
from pyValkLib.utils.Compression.Stencilled.relative import SCRelativeTemplateGenerator
from pyValkLib.utils.Compression.Stencilled.unpacked import SCUnpackedTemplateComponents, SCTemplate, SCTemplatePack
from pyValkLib.utils.Compression.Stencilled.validation import flattenStencil, compareStencil
from pyValkLib.utils.Compression.Stencilled.validation import Validator
from pyValkLib.serialisation.ReadWriter import CCRSBuilder

class CCRSRelRep(SCRelRep):
    @property
    def classname(self):
        return "CCRSRelRep"
        
    @property
    def absclass(self):
        return CCRSAbsRep
    
class CCRSAbsRep(SCAbsRep):
    @property
    def classname(self):
        return "CCRSAbsRep"
        
    @property
    def relclass(self):
        return CCRSRelRep
        
    @property
    def unpackedclass(self):
        return CCRSUnpackedRep
        
    @property
    def utcclass(self):
        return CCRSUnpackedTemplateComponents
    
    
class CCRSUnpackedRep(SCUnpackedRep):
    @property
    def component_type(self):
        return CCRSTemplateComponent

    @property
    def classname(self):
        return "CCRSUnpackedRep"

    @property
    def absclass(self):
        return CCRSAbsRep
    
class CCRSTemplateComponent(SCTemplateComponent):
    @property
    def classname(self):
        return "CCRSTemplateComponent"
            
    def get_item_size(self):
        if self.type == 0:
            return 0x10
        elif self.type == 1:
            return 0x04
        elif 1 < self.type <= 5:
            return 0x02
        else:
            raise ValueError(f"Invalid type: {self.type}")
        
    
class CCRSUnpackedTemplateComponents(SCUnpackedTemplateComponents):
    def get_type_sizes(self):
        return {0: 0x10,
                1: 0x04,
                2: 0x02,
                3: 0x02,
                4: 0x02,
                5: 0x02}
    
    @property
    def classname(self):
        return "CCRS UTC"
    
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
            
        cgen = SCRelativeTemplateGenerator(jump_from_previous_group, stencil_size, stencil_repetitions,
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
        
    n_to_extend = (0x10 - (len(out) % 0x10)) % 0x10
    out += [0]*n_to_extend
    return out

def toCCRSPackedRep(data):
    out = CCRSUnpackedRep()
    
    for tpack_data in data:
        templates = []
        for template_data in tpack_data:
            template = SCTemplate()
            for comp_data in template_data:
                template.append(CCRSUnpackedTemplateComponents(comp_data, comp_data.type))
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

def buildCCRS(ctr):
    cb = CCRSBuilder()
    cb.anchor_pos = -ctr.header.header_length
    cb.mark_new_contents_array()
    ctr.read_write_contents(cb)
    cb.mark_new_contents_array()
    
    return cb.pointers

def compareCCRS(ctr_1, ctr_2, print_errs=True):
    compareStencil(ctr_1, ctr_2, lambda x: x.CCRS, decompressCCRS, compressCCRS, buildCCRS, toCCRSPackedRep, print_errs)

def validateCCRS(pointers, print_errs=False):
    reference_ccrs = flattenStencil(pointers)
    
    # Test if moving to structure works
    ccrs_test_1 = toCCRSPackedRep(pointers)
    ccrs_test_1 = ccrs_test_1.flatten()
    if ccrs_test_1 != reference_ccrs:
        for i, (c1, c2) in enumerate(zip(reference_ccrs, ccrs_test_1)):
            if print_errs:
                print("> CCRS TEST 1", i, c1, "---", c2)
            
            if c1 != c2:
                print(f"{i} {c1} --- {c2}")
                raise Exception()
                
    # Test if moving to AbsRep works
    ccrs_test_2 = toCCRSPackedRep(pointers)
    ccrs_test_2 = ccrs_test_2.to_abs_rep().to_unpacked_rep()
    ccrs_test_2 = flattenStencil(ccrs_test_2)
    if ccrs_test_2 != reference_ccrs:
        for i, (c1, c2) in enumerate(zip(reference_ccrs, ccrs_test_2)):
            if print_errs:
                print("> CCRS TEST 2", i, c1, "---", c2)
            
            if c1 != c2:
                print(f"{i} {c1} --- {c2}")
                raise Exception()   
                
    # Test if moving to RelRep works
    ccrs_test_2 = toCCRSPackedRep(pointers)
    ccrs_test_2 = ccrs_test_2.to_abs_rep().to_rel_rep().to_abs_rep().to_unpacked_rep()
    ccrs_test_2 = flattenStencil(ccrs_test_2)
    if ccrs_test_2 != reference_ccrs:
        for i, (c1, c2) in enumerate(zip(reference_ccrs, ccrs_test_2)):
            if print_errs:
                print("> CCRS TEST 3", i, c1, "---", c2)
            
            if c1 != c2:
                print(f"{i} {c1} --- {c2}")
                raise Exception()   
                
    # Test if compressing and decompressing works
    ccrs_test_3 = toCCRSPackedRep(pointers)
    ccrs_test_3 = compressCCRS(ccrs_test_3)
    ccrs_test_3 = decompressCCRS(len(pointers), ccrs_test_3).flatten()
    
    if ccrs_test_3 != reference_ccrs:
        for i, (c1, c2) in enumerate(zip(reference_ccrs, ccrs_test_3)):
            if print_errs:
                print("> CCRS TEST 4", i, c1, "---", c2)
            
            if c1 != c2:
                print(f"{i} {c1} --- {c2}")
                raise Exception()

class CCRSValidator(Validator):
    FILETYPE="CCRSVALIDATOR"
    
    def __init__(self, ctr, print_errs=True):
        super().__init__(lambda: compareCCRS(ctr, ctr, print_errs))
