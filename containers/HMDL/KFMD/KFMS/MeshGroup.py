from pyValkLib.serialisation.Serializable import Context, Serializable

class MeshGroup(Serializable):
    def __init__(self, context=None):
        if context is None:
            self.context = Context()
        super().__init__(context)
        
        self.ID                 = None
        self.is_root            = None
        self.parent_bone_ID     = None
        self.material_offset    = None
        self.unknown_0x0A       = None
        self.mesh_count         = None
        self.meshes_offset      = None
        self.vertex_offset      = None
        self.vertex_count       = None
        
    def __repr__(self):
        return f"[MeshGroup {self.is_root} {self.ID}] {self.material_offset} {self.unknown_0x0A} {self.mesh_count} {self.meshes_offset} {self.vertex_offset} {self.vertex_count}"
        
    def read_write(self, rw):
        self.ID                 = rw.rw_uint32(self.ID)
        self.is_root            = rw.rw_uint16(self.is_root)
        self.parent_bone_ID     = rw.rw_uint16(self.parent_bone_ID)
        self.material_offset    = rw.rw_pointer(self.material_offset)
        self.unknown_0x0A       = rw.rw_uint16(self.unknown_0x0A) # Material count?
        self.mesh_count         = rw.rw_uint16(self.mesh_count)
        
        self.meshes_offset      = rw.rw_pointer(self.meshes_offset)
        self.vertex_offset      = rw.rw_uint32(self.vertex_offset)
        self.vertex_count       = rw.rw_uint16(self.vertex_count)
        
        rw.align(0x1A, 0x20)

        rw.assert_equal(self.unknown_0x0A, 0)        
