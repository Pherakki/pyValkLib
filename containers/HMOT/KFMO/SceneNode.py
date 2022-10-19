from pyValkLib.serialisation.Serializable import Serializable

class SceneNode(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.flags = None
        self.animation_offset = None
        self.transform_offset = None
        
    def __repr__(self):
        return f"[KFMO::SceneNode] "\
            f"{self.flags if self.flags is None else hex(self.flags)} " \
            f"{self.animation_offset} {self.transform_offset}"
        
    def read_write(self, rw):
        self.flags = rw.rw_uint64(self.flags)
        self.animation_offset = rw.rw_pointer(self.animation_offset)
        self.transform_offset = rw.rw_pointer(self.transform_offset)
        
    def get_count(self):
        count = 0
        flags = self.flags
        for i in range(64):
            count += flags & 1
            flags >>= 1
        return count
