from pyValkLib.serialisation.Serializable import Context, Serializable

class InverseBindPoseMatrix(Serializable):
    __slots__ = ("matrix",)
    
    def __init__(self, context=None):
        if context is None:
            self.context = Context()
        super().__init__(context)
        
        self.matrix = None
    
    def __repr__(self):
        return f"[InverseBindPoseMatrix] {self.transform}"
    
    def read_write(self, rw):
        self.matrix = rw.rw_float32s(self.matrix, (4, 4))
