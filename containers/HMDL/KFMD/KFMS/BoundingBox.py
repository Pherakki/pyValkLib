from pyValkLib.serialisation.Serializable import Context, Serializable

class BoundingBox(Serializable):
    __slots__ = ("vertex_count", "vertices")
    
    def __init__(self, vertex_count, context=None):
        if context is None:
            self.context = Context()
        super().__init__(context)
        
        self.vertex_count = vertex_count
        self.vertices = []
        
    def read_write(self, rw):
        rw.mark_new_contents_array()
        self.vertices = rw.rw_float32s(self.vertices, (self.vertex_count, 4))
        