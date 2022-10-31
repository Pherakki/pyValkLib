from pyValkLib.serialisation.Serializable import Context, Serializable

class MeshDefinitionBinary(Serializable):
    def __init__(self, context=None):
        if context is None:
            self.context = Context()
        super().__init__(context)
        
        self.flags            = None
        self.bytes_per_vertex = None
        self.faces_offset     = None
        self.faces_count      = None
        
        self.vertices_offset  = None
        self.vertices_count   = None
        self.padding_0x18     = None
        
        
    def read_write(self, rw):
        self.flags            = rw.rw_uint32(self.flags)
        self.bytes_per_vertex = rw.rw_uint32(self.bytes_per_vertex)
        self.faces_offset     = rw.rw_uint32(self.faces_offset)
        self.faces_count      = rw.rw_uint32(self.faces_count)
        
        self.vertices_offset  = rw.rw_uint32(self.vertices_offset)
        self.vertices_count   = rw.rw_uint32(self.vertices_count)
        self.padding_0x18     = rw.rw_uint32(self.padding_0x18)
        
        rw.align(rw.local_tell(), 0x10)
        
        rw.assert_is_zero(self.padding_0x18)
        # Hashes: 0x80000003, 0x80000006
        #rw.assert_equal(self.unknown_hash, 0x80000006)
