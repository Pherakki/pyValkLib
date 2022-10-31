from pyValkLib.serialisation.Serializable import Context, Serializable
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray

class UnknownIndicesBinary(Serializable):
    def __init__(self, context=None):
        if context is None:
            self.context = Context()
        super().__init__(context)
        
        self.index_group_count   = 0
        self.unknown_objs_offset = 0
        self.index_groups = []
        
    def __repr__(self):
        return f"[KFMS::UnknownIndices] {self.index_groups.data}"
        
    def read_write(self, rw):
        rw.mark_new_contents_array()
        self.index_group_count   = rw.rw_uint32(self.index_group_count)
        self.unknown_objs_offset = rw.rw_pointer(self.unknown_objs_offset)
        rw.align(0x08, 0x10)
        
        rw.mark_new_contents_array()
        self.index_groups = rw.rw_obj_array(self.index_groups, lambda: UnknownIndexGroupBinary(self.context), self.index_group_count)

        rw.align(rw.local_tell(), 0x10)
        rw.mark_new_contents_array()
        for ig in self.index_groups:
            rw.rw_obj_method(ig, ig.read_write_indices)
        rw.align(rw.local_tell(), 0x10)

class UnknownIndexGroupBinary(Serializable):
    def __init__(self, context=None):
        if context is None:
            self.context = Context()
        super().__init__(context)
        
        self.count   = 0
        self.offset  = 0
        self.indices = []
        
    def __repr__(self):
        return f"[KFMS::UnknownIndices::UnknownIndexGroup {self.count}/{self.offset}] {self.indices}"
        
    def read_write(self, rw):
        self.count  = rw.rw_uint32(self.count)
        self.offset = rw.rw_pointer(self.offset)
        
    def read_write_indices(self, rw):
        rw.assert_local_file_pointer_now_at("Unknown Index Group Indices", self.offset)
        self.indices = rw.rw_uint32s(self.indices, (self.count, 2))
