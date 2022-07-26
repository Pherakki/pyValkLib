import array

class CCRSUnpackedTemplateComponents:
    __slots__ = ("values", "type")
    
    def __init__(self, values, type_):
        self.values = array.array('I', values)
        self.type = type_
                   
    def __getitem__(self, idx):
        return self.values[idx]
    
    def __len__(self):
        return len(self.values)
    
    def __iter__(self):
        for elem in self.values:
            yield elem
     
    def __repr__(self):
        return f"<CCRS UTC>{{{self.type}}} {list(self.values)}</CCRS UTC>"

class CCRSTemplate:
    __slots__ = ("components",)
    
    def __init__(self):
        self.components = []
        
    def __getitem__(self, idx):
        return self.components[idx]
            
    def __len__(self):
        return len(self.components)
    
    def __iter__(self):
        for elem in self.components:
            yield elem
    
    def __repr__(self):
        out = "<CCRS UT>" 
        for tg in self.components:
            tg_rep = '\n'.join(['\t' + ln for ln in str(tg).split('\n')])
            out += f"\n{tg_rep}"
        out += "\n</CCRS UT>"
        return out
    
    def get_first_offset(self):
        return self[0][0]
    
    def append(self, item):
        if type(item) != CCRSUnpackedTemplateComponents:
            raise TypeError(f"Tried to append \'{type(item)}\', expected CCRSUnpackedTemplateComponents.")
        self.components.append(item)
        
    def flatten(self):
        return [subitem for item in self for subitem in item]
    
    def typed_flatten(self):
        return [(subitem, item.type) for item in self for subitem in item]

class CCRSTemplatePack:
    __slots__ = ("templates", "stride")
    
    def __init__(self, stride):
        self.templates = []
        self.stride = stride
        
    def __getitem__(self, idx):
        return self.templates[idx]
        
    def __len__(self):
        return len(self.templates)
    
    def __iter__(self):
        for elem in self.templates:
            yield elem
    
    def __repr__(self):
        out = f"<CCRS UTP> Stride: {self.stride}"
        for tg in self.templates:
            tg_rep = '\n'.join(['\t' + ln for ln in str(tg).split('\n')])
            out += f"\n{tg_rep}"
        out += "\n</CCRS UTP>"
        return out
    
    def get_first_offset(self):
        return self[0][0][0]
    
    def append(self, item):
        if type(item) != CCRSTemplate:
            raise TypeError(f"Tried to append \'{type(item)}\', expected CCRSTemplate.")
        self.templates.append(item)
        
    def flatten(self):
        return [subitem for item in self for subitem in item.flatten()]
    
    def typed_flatten(self):
        return [subitem for item in self for subitem in item.typed_flatten()]
