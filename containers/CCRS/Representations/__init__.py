from .common import CCRSTemplateComponent
from .relative import CCRSRelativeTemplateGenerator
from .absolute import CCRSAbsoluteTemplateGenerator
from .unpacked import CCRSUnpackedTemplateComponents, CCRSTemplate, CCRSTemplatePack

class CCRSRelRep:
    def __init__(self):
        self.template_generators = []
        
    def __repr__(self):
        out = ""
        for tg in self.template_generators:
            tg_rep = '\n'.join(['\t' + ln for ln in str(tg).split('\n')])
            out += f"\n{tg_rep}"
        return f"<CCRS RelRep>{out}\n</CCRS RelRep>"

    def __getitem__(self, idx):
        return self.template_generators[idx]
    
    def append(self, item):
        if type(item) != CCRSRelativeTemplateGenerator:
            raise TypeError(f"Tried to append \'{type(item)}\', expected CCRSRelativeTemplateGenerator.")
        self.template_generators.append(item)
    
    def to_abs_rep(self):
        out = CCRSAbsRep()
        
        prev_offset = 0
        for tg in self.template_generators:
            atg = CCRSAbsoluteTemplateGenerator(tg.jump + prev_offset, tg.stride, tg.count, tg.subs)
            prev_offset += tg.jump
            out.append(atg)
        
        return out
    
class CCRSAbsRep:
    def __init__(self):
        self.template_generators = []
        
    def __getitem__(self, idx):
        return self.template_generators[idx]
    
    def __repr__(self):
        out = ""
        for tg in self.template_generators:
            tg_rep = '\n'.join(['\t' + ln for ln in str(tg).split('\n')])
            out += f"\n{tg_rep}"
        return f"<CCRS AbsRep>{out}\n</CCRS AbsRep>"
    
    def append(self, item):
        if type(item) != CCRSAbsoluteTemplateGenerator:
            raise TypeError(f"Tried to append \'{type(item)}\', expected CCRSAbsoluteTemplateGenerator.")
        self.template_generators.append(item)
        
    def to_rel_rep(self):
        out = CCRSRelRep()
        
        prev_offset = 0
        for atg in self.template_generators:
            tg = CCRSRelativeTemplateGenerator(atg.offset - prev_offset, atg.stride, atg.count, atg.subs)
            prev_offset = atg.offset
            out.append(tg)
        
        return out
    
    def to_unpacked_rep(self):
        out = CCRSUnpackedRep()
        
        for atg in self.template_generators:
            tpack = CCRSTemplatePack(atg.stride)
            
            # Generate the template
            prev_offset = 0
            utcs = []
            pack_offset = atg.offset
            for template_comp in atg.subs:
                offsets = [item + prev_offset for item in template_comp.unpack()]
                utcs.append((offsets, template_comp.type))
                prev_offset = offsets[-1]
            
            # Now copy the template
            for template_copy_idx in range(atg.count):
                ct = CCRSTemplate()
                
                for offsets, type_ in utcs:
                    abs_offsets = [pack_offset + item for item in offsets]
                    utc = CCRSUnpackedTemplateComponents(abs_offsets, type_)
                    ct.append(utc)
                    
                pack_offset += atg.stride
                
                tpack.append(ct)
            out.append(tpack)
        return out
        
class CCRSUnpackedRep:
    __slots__ = ("template_packs",)
    
    def __init__(self):
        self.template_packs = []

    def __repr__(self):
        out = "<CCRS UnpackedRep>"
        for tg in self.template_packs:
            tg_rep = '\n'.join(['\t' + ln for ln in str(tg).split('\n')])
            out += f"\n{tg_rep}"
        out += "\n</CCRS UnpackedRep>"
        return out
    
    def __getitem__(self, idx):
        return self.template_packs[idx]
    
    def __len__(self):
        return len(self.template_packs)
    
    def __iter__(self):
        for elem in self.template_packs:
            yield elem
    
    def append(self, item):
        if type(item) != CCRSTemplatePack:
            raise TypeError(f"Tried to append \'{type(item)}\', expected CCRSTemplatePack.")
        self.template_packs.append(item)
    
    def flatten(self):
        return [subitem for item in self for subitem in item.flatten()]
    
    def typed_flatten(self):
        return [subitem for item in self for subitem in item.typed_flatten()]
    
    def get_first_offset(self):
        return self[0].get_first_offset()
    
    def to_abs_rep(self):
        out = CCRSAbsRep()
        
        for tpack in self:
            tpack_offset = tpack.get_first_offset()
            
            first_template = tpack[0]
            subs = []
            # Check that elements are contiguous?
            prev_offset = tpack_offset
            for component in first_template:
                comp_stride = component[0] - prev_offset
                subs.append(CCRSTemplateComponent(comp_stride, len(component), component.type))
                prev_offset = component[0]
            
            # Check that all subsequent templates match the first?
            
            atg = CCRSAbsoluteTemplateGenerator(tpack_offset, tpack.stride, len(tpack), subs)
            out.append(atg)
        return out
