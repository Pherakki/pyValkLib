from pyValkLib.serialisation.Serializable import Context, Serializable

class MeshBinary(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.vertex_group_count      = None
        self.unknown_0x02            = None
        self.unknown_0x04            = None
        self.vertex_count            = None
        self.faces_count             = None
        self.vertex_groups_offset    = None
        
        self.kfmg_vertices_idx       = None
        self.kfmg_faces_idx          = None
        self.mesh_group_vertices_idx = None

    def __repr__(self):
        return f"[MeshBinary] {self.vertex_groups_offset}/{self.vertex_group_count} {self.unknown_0x02} {self.unknown_0x04} {self.kfmg_vertices_idx}/{self.mesh_group_vertices_idx}/{self.vertex_count}"
        
    def read_write(self, rw):
        self.vertex_group_count      = rw.rw_uint16(self.vertex_group_count)
        self.unknown_0x02            = rw.rw_uint16(self.unknown_0x02)
        self.unknown_0x04            = rw.rw_uint16(self.unknown_0x04)
        self.vertex_count            = rw.rw_uint16(self.vertex_count)
        self.faces_count             = rw.rw_uint16(self.faces_count)
        rw.align(0x0A, 0x0C)
        self.vertex_groups_offset    = rw.rw_pointer(self.vertex_groups_offset)
        
        self.kfmg_vertices_idx       = rw.rw_uint32(self.kfmg_vertices_idx)
        self.kfmg_faces_idx          = rw.rw_uint32(self.kfmg_faces_idx)
        self.mesh_group_vertices_idx = rw.rw_uint32(self.mesh_group_vertices_idx)
        rw.align(0x1C, 0x20)
