from pyValkLib.serialisation.Serializable import Context, Serializable

class Bone(Serializable):
    __slots__ = ("ibpm_offset", "ID")
    
    def __init__(self, context=None):
        if context is None:
            self.context = Context()
        super().__init__(context)
        
        self.ibpm_offset = None
        self.ID = None
    
    def read_write(self, rw):
        self.ibpm_offset = rw.rw_pointer(self.ibpm_offset)
        self.ID          = rw.rw_uint32(self.ID)
