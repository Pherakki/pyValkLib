from pyValkLib.serialisation.Serializable import Context, Serializable

class SkeletonBinary(Serializable):
    __slots__ = ("id_count", "bone_ids")
    
    def __init__(self, id_count, context=None):
        if context is None:
            self.context = Context()
        super().__init__(context)
        
        self.id_count = id_count
        self.bone_ids = []
    
    def __repr__(self):
        return f"[KFMS::Skeleton] {self.id_count} {self.bone_ids}"
    
    def read_write(self, rw):
        rw.mark_new_contents_array()
        self.bone_ids = rw.rw_uint16s(self.bone_ids, self.id_count)
