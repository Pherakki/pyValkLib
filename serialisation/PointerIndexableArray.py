from pyValkLib.serialisation.Serializable import Serializable


class PointerIndexableArray(Serializable):
    def __init__(self):
        #self.context.anchor_pos = context.anchor_pos
        #self.context.endianness = context.endianness
        
        self.data = []
        self.ptr_to_idx = {}
        self.idx_to_ptr = []
        
    def at_ptr(self, ptr):
        return self.data[self.ptr_to_idx[ptr]]
    
    def at_idx(self, idx):
        return self.data[idx]
    
    def __iter__(self):
        for elem in self.data:
            yield elem
    