from pyValkLib.serialisation.Serializable import Serializable

class View:
    @staticmethod
    def rw_op(rw, buffer, buffer_size):
        raise NotImplementedError

class BufferViewArray(Serializable):
    def __init__(self, context, view_t):
        super().__init__(context)
        
        self.buffer = None
        self.views = None
        self.idx_anchor = None
        self.view_t = view_t
        self.ptr_to_idx = {}
        
    def read_write(self, rw, buffer_size, view_offsets, view_args):
        rw.mark_new_contents_array()
        self.idx_anchor = rw.local_tell()
        rw_op = self.view_t.rw_op
        self.buffer = memoryview(rw_op(rw, self.buffer, buffer_size))
        
        if rw.mode() == "read":
            self.views = [self.view_t(self.buffer[self.buffer_ptr_to_idx(offset):], *args) 
                          for offset, args 
                          in zip(view_offsets, view_args)]
            self.view_ptr_to_idx = {v: k for k, v in enumerate(view_offsets)}
            
    def buffer_ptr_to_idx(self, ptr):
        return (ptr-self.idx_anchor)//self.view_t.element_size
        
    def buffer_idx_to_ptr(self, idx):
        return self.idx_anchor + self.view_t.element_size*idx
    
    def at_ptr(self, ptr):
        idx = self.view_ptr_to_idx[ptr]
        return self.views[idx]
    