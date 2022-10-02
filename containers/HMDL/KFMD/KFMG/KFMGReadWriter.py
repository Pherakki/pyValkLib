from pyValkLib.serialisation.ValkSerializable import Serializable, ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray, PointerIndexableArrayUint16

from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.CCRS.CCRSReadWriter import CCRSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter


class KFMGReadWriter(ValkSerializable32BH):
    FILETYPE = "KFMG"
    
    def __init__(self, KFMS_ref, endianness=None):
        super().__init__({}, endianness)
        
        self.KFMS_ref = KFMS_ref
        
        self.header.flags = 0x18000000
        self.ENRS = ENRSReadWriter("<")
        self.CCRS = CCRSReadWriter("<")
        self.EOFC = EOFCReadWriter("<")
        
        self.faces    = PointerIndexableArrayUint16(self.context)
        self.vertices = PointerIndexableArray(self.context)
        
    def get_subcontainers(self):
        return [self.ENRS, self.CCRS, self.EOFC]
    
    def read_write_contents(self, rw):
        is_big_endian = self.KFMS_ref.flags & 1 == 1
        self.context.endianness = '>' if is_big_endian else '<'
        if self.header.data_length and is_big_endian:
            rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))
        else:
            rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))
        self.rw_faces(rw)
        self.rw_verts(rw)

    def rw_faces(self, rw):
        rw.mark_new_contents_array()
        mesh_definition = self.KFMS_ref.mesh_definitions[0]
        rw.assert_local_file_pointer_now_at("Faces", mesh_definition.faces_offset + self.header.header_length)
        if rw.mode() == "read":
            self.faces.data = [None for _ in range(mesh_definition.faces_count)]
        rw.rw_obj(self.faces)
        rw.align(rw.local_tell(), 0x10)
        
    def rw_verts(self, rw):
        rw.mark_new_contents_array()
        
        mesh_definition = self.KFMS_ref.mesh_definitions[0]
        rw.assert_local_file_pointer_now_at("Vertices", mesh_definition.vertices_offset + self.header.header_length)
        if rw.mode() == "read":
            vertex_type = {
                0x2C: Vertex0x2C,
                0x30: Vertex0x30,
                0x50: Vertex0x50    
            }[mesh_definition.bytes_per_vertex]
            self.vertices.data = [vertex_type(self.context) for _ in range(mesh_definition.vertices_count)]
        
        rw.rw_obj(self.vertices)
        rw.align(rw.local_tell(), 0x10)

    def __repr__(self):
        return f"KFMG Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains {', '.join(c.FILETYPE for c in self.get_subcontainers())}."

class Vertex0x2C(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.position = None
        self.unknown = None
        self.normal = None
        self.color_1 = None
        self.color_2 = None
        self.UV_1 = None
        self.UV_2 = None
        self.UV_3 = None
        
    def read_write(self, rw):
        self.position = rw.rw_float32s(self.position, 3)
        self.unknown  = rw.rw_vec32(self.unknown) # Tangent?
        self.normal   = rw.rw_float16s(self.normal, 4)
        self.color_1    = rw.rw_color32(self.color_1)
        self.color_2  = rw.rw_color32(self.color_2)
        self.UV_1      = rw.rw_float16s(self.UV_1, 2)
        self.UV_2      = rw.rw_float16s(self.UV_2, 2)
        self.UV_3      = rw.rw_float16s(self.UV_3, 2)
        

class Vertex0x30(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.position       = None
        self.vertex_groups  = None
        self.vertex_weights = None
        self.color = None
        self.UV_1 = None
        self.UV_2 = None
        self.UV_3 = None
        self.normal = None
        self.unknown = None
        
    def read_write(self, rw):
        self.position       = rw.rw_float32s(self.position, 3)
        self.vertex_groups  = rw.rw_uint8s(self.vertex_groups, 4)
        self.vertex_weights = rw.rw_float16s(self.vertex_weights, 2)
        self.color          = rw.rw_color32(self.color)
        self.UV_1            = rw.rw_float16s(self.UV_1, 2)
        self.UV_2            = rw.rw_float16s(self.UV_2, 2)
        self.UV_3            = rw.rw_float16s(self.UV_3, 2)
        self.normal         = rw.rw_float16s(self.normal, 4)
        self.unknown        = rw.rw_vec32(self.unknown) # Tangent?

class Vertex0x50(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.position       = None
        self.unknown        = None
        
    def read_write(self, rw):
        self.position       = rw.rw_float32s(self.position, 3)
        self.vertex_groups  = rw.rw_int8s(self.vertex_groups, 4)
        self.vertex_weights = rw.rw_float32s(self.vertex_weights, 2)
        self.unknown_1      = rw.rw_vec32(self.unknown_1) # Tangent?
        self.unknown_2      = rw.rw_vec32(self.unknown_2) # Binormal?
        self.normal         = rw.rw_float32s(self.normal, 3)
        self.color          = rw.rw_color32(self.color)
        self.UV_1           = rw.rw_float32s(self.UV_1, 2)
        self.UV_2           = rw.rw_float32s(self.UV_2, 2)
        self.UV_3           = rw.rw_float32s(self.UV_3, 2)
        self.unknown_3      = rw.rw_float32s(self.unknown_3, 2) # padding?

