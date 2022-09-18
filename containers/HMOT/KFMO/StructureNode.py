from pyValkLib.serialisation.Serializable import Serializable

class StructureNode(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.flags = None
        self.animation_offset = None
        self.transform_offset = None
        
    def read_write(self, rw):
        self.flags = rw.rw_uint64(self.flags)
        self.animation_offset = rw.rw_pointer(self.animation_offset)
        self.transform_offset = rw.rw_pointer(self.transform_offset)
        
    