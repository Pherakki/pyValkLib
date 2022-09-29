from pyValkLib.serialisation.Serializable import Context, Serializable

class VertexGroup(Serializable):
    __slots__ = ("bone_id", "mesh_group_vertex_group_id")
    
    def __init__(self, context=None):
        if context is None:
            self.context = Context()
        super().__init__(context)
        
        self.bone_id = None
        self.mesh_group_vertex_group_id = None
        
    def read_write(self, rw):
        self.bone_id                    = rw.rw_uint16(self.bone_id)
        self.mesh_group_vertex_group_id = rw.rw_uint16(self.mesh_group_vertex_group_id)
