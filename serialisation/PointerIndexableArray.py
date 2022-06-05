from pyValkLib.serialisation.Serializable import Serializable


class PointerIndexableArray(Serializable):
    def __init__(self, context):
        super().__init__(context)
        #self.context.anchor_pos = context.anchor_pos
        #self.context.endianness = context.endianness
        
        self.data = []
        self.ptr_to_idx = {}
        self.idx_to_ptr = {}
        
    def at_ptr(self, ptr):
        return self.data[self.ptr_to_idx[ptr]]
    
    def at_idx(self, idx):
        return self.data[idx]
    
    def __iter__(self):
        for elem in self.data:
            yield elem
    def read_write(self, rw):
        for i, elem in enumerate(self.data):
            if i in self.idx_to_ptr:
                rw.assert_local_file_pointer_at("Start of Array Entry", self.idx_to_ptr[i])
            curpos = rw.local_tell()
            self.ptr_to_idx[curpos] = i
            self.idx_to_ptr[i] = curpos

            self.rw_element(rw, i)

    def rw_element(self, rw, idx):
        rw.rw_obj(self.data[idx])
    
class PointerIndexableArrayInt8(Serializable):
