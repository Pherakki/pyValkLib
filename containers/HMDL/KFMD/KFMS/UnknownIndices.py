from pyValkLib.serialisation.Serializable import Context, Serializable
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray

class UnknownIndexGroup(Serializable):
    def __init__(self, context=None):
        if context is None:
            self.context = Context()
        super().__init__(context)
        
        self.count   = 0
        self.offset  = 0
        self.indices = []
        
    def __repr__(self):
        return f"[UnknownIndexGroup {self.count}/{self.offset}] {self.indices}"
        
    def read_write(self, rw):
        self.count  = rw.rw_uint32(self.count)
        self.offset = rw.rw_pointer(self.offset)
        print(">>", self.count)
        print(">>", self.offset)
        
    def read_write_indices(self, rw):
        rw.assert_local_file_pointer_now_at("Unknown Index Group Indices", self.offset)
        self.indices = rw.rw_uint32s(self.indices, 2*self.count)
        print(">>>>", self.indices)

class UnknownIndices(Serializable):
    def __init__(self, context=None):
        if context is None:
            self.context = Context()
        super().__init__(context)
        
        self.index_group_count   = 0
        self.unknown_objs_offset = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.index_groups = PointerIndexableArray(self.context)
        
    def __repr__(self):
        return f"[UnknownIndices] {self.index_groups.data}"
        
    def read_write(self, rw):
        self.index_group_count   = rw.rw_uint32(self.index_group_count)
        self.unknown_objs_offset = rw.rw_pointer(self.unknown_objs_offset)
        rw.align(0x08, 0x10)
        
        if rw.mode() == "read":
            self.index_groups.data = [UnknownIndexGroup(self.context) for _ in range(self.index_group_count)]
        rw.rw_obj(self.index_groups)
        rw.align(rw.local_tell(), 0x10)
        for ig in self.index_groups:
            rw.rw_obj_method(ig, ig.read_write_indices)
        rw.align(rw.local_tell(), 0x10)
