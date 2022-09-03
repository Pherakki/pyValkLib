from pyValkLib.serialisation.Serializable import Serializable

class StructureNode(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.flags = None
        self.padding = 0
        self.offset_1 = None
        self.offset_2 = None
        
    def read_write(self, rw):
        self.flags = rw.rw_uint64(self.flags)
        self.offset_1 = rw.rw_pointer(self.offset_1)
        self.offset_2 = rw.rw_pointer(self.offset_2)
        
        rw.assert_is_zero(self.padding)
    