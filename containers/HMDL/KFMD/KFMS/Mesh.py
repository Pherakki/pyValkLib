from pyValkLib.serialisation.Serializable import Context, Serializable

class Mesh(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.vertex_group_count   = None
        self.unknown_0x02         = None
        self.unknown_0x04         = None
        self.vertex_count         = None
        self.faces_count          = None
        self.padding_0x0A         = 0
        self.vertex_groups_offset = None
        
        self.vertices_offset      = None
        self.faces_offset         = None
        self.vertex_idxs_offset   = None
        self.unknown_0x1C         = 0

    def __repr__(self):
        return f"[Mesh] {self.vertex_groups_offset}/{self.vertex_group_count} {self.unknown_0x02} {self.unknown_0x04} {self.vertices_offset}/{self.vertex_idxs_offset}/{self.vertex_count}"
        
    def read_write(self, rw):
        self.vertex_group_count   = rw.rw_uint16(self.vertex_group_count)
        self.unknown_0x02         = rw.rw_uint16(self.unknown_0x02)
        self.unknown_0x04         = rw.rw_uint16(self.unknown_0x04)
        self.vertex_count         = rw.rw_uint16(self.vertex_count)
        self.faces_count          = rw.rw_uint16(self.faces_count)
        self.padding_0x0A         = rw.rw_pad16(self.padding_0x0A)
        self.vertex_groups_offset = rw.rw_pointer(self.vertex_groups_offset)
        
        self.vertices_offset      = rw.rw_uint32(self.vertices_offset)
        self.faces_offset         = rw.rw_uint32(self.faces_offset)
        self.vertex_idxs_offset   = rw.rw_uint32(self.vertex_idxs_offset)
        self.unknown_0x1C         = rw.rw_pad32(self.unknown_0x1C)

        rw.assert_is_zero(self.padding_0x0A)
        rw.assert_is_zero(self.unknown_0x1C)