from pyValkLib.serialisation.ValkSerializable import Serializable, ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray
from pyValkLib.containers.Metadata.POF0.POF0ReadWriter import POF0ReadWriter
from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

class KFSSReadWriter(ValkSerializable32BH):
    FILETYPE = "KFSS"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x18000000
        
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.count_1 = None
        self.offset_1 = None
        
        self.mesh_deform_count = None
        self.mesh_deforms_offset = None
        self.vertex_info_count = None
        self.vertex_info_offset = None
        
        self.mesh_definition_count = None
        self.mesh_definitions_offset = None
        self.unknown_0x28 = None
        self.unknown_0x2C = None

        self.data_1 = []
        self.mesh_deforms = []
        self.vertex_info = []
        self.mesh_defs = []
        
        self.POF0 = POF0ReadWriter("<")
        self.ENRS = ENRSReadWriter("<")
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.POF0, self.ENRS, self.EOFC]
    
    def __repr__(self):
        return f"KFSS Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains POF0, ENRS."    
        
    def read_write_contents(self, rw):
        rw.mark_new_contents_array()
        if self.header.data_length:
            rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))
        else:
            rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))
        
        self.unknown_0x00            = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04            = rw.rw_uint32(self.unknown_0x04)
        self.count_1                 = rw.rw_uint32(self.count_1)
        self.offset_1                = rw.rw_pointer(self.offset_1)
        self.mesh_deform_count       = rw.rw_uint32(self.mesh_deform_count)
        self.mesh_deforms_offset     = rw.rw_pointer(self.mesh_deforms_offset)
        self.vertex_info_count       = rw.rw_uint32(self.vertex_info_count)
        self.vertex_info_offset      = rw.rw_pointer(self.vertex_info_offset)
        self.mesh_definition_count   = rw.rw_uint32(self.mesh_definition_count)
        self.mesh_definitions_offset = rw.rw_pointer(self.mesh_definitions_offset)
        self.unknown_0x28 = rw.rw_float32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_float32(self.unknown_0x2C)
        
        self.rw_data_1(rw)
        self.rw_mesh_deforms(rw)
        self.rw_vertex_info(rw)
        self.rw_mesh_defs(rw)
        
        rw.mark_new_contents_array()
        
    def rw_data_1(self, rw):
        rw.mark_new_contents_array()
        rw.assert_local_file_pointer_now_at("Data 1", self.offset_1)
        self.data_1 = rw.rw_obj_array(self.data_1, lambda: Data1(self.context), self.count_1)
        rw.align(rw.local_tell(), 0x10)
            
        rw.mark_new_contents_array()
        for obj in self.data_1:
            rw.rw_obj_method(obj, obj.rw_floats)
        
    def rw_mesh_deforms(self, rw):
        rw.mark_new_contents_array()
        rw.assert_local_file_pointer_now_at("Mesh Deforms", self.mesh_deforms_offset)
        self.mesh_deforms = rw.rw_obj_array(self.mesh_deforms, lambda: MeshDeform(self.context), self.mesh_deform_count)
        rw.align(rw.local_tell(), 0x10)
        
    def rw_vertex_info(self, rw):
        rw.mark_new_contents_array()
        rw.assert_local_file_pointer_now_at("Vertex Info", self.vertex_info_offset)
        self.vertex_info = rw.rw_obj_array(self.vertex_info, lambda: VertexInfo(self.context), self.vertex_info_count)
        rw.align(rw.local_tell(), 0x10)
        
    def rw_mesh_defs(self, rw):
        rw.mark_new_contents_array()
        rw.assert_local_file_pointer_now_at("Mesh Definitions", self.mesh_definitions_offset)
        self.mesh_defs = rw.rw_obj_array(self.mesh_defs, lambda: VertexFormat(self.context), self.mesh_definition_count)
        
        rw.mark_new_contents_array()
        for obj in self.mesh_defs:
            rw.rw_obj_method(obj, obj.rw_vertex_partitions)
        rw.align(rw.local_tell(), 0x10)
        
class Data1(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x02 = None
        self.unknown_0x04 = None
        self.unknown_0x06 = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        self.unknown_0x10 = None
        self.unknown_0x12 = None
        self.unknown_0x14 = None
        self.unknown_0x16 = None
        self.unknown_0x18 = None
        self.unknown_0x1C = None
        self.unknown_0x20 = None
        
        self.floats = []
        
    def __repr__(self):
        return f"[KFSS::Data1] {self.unknown_0x00} {self.unknown_0x02} "\
               f"{self.unknown_0x04} {self.unknown_0x08} {self.unknown_0x0C} "\
               f"{self.unknown_0x10} {self.unknown_0x12} {self.unknown_0x14} {self.unknown_0x16} "\
               f"{self.unknown_0x18} {self.unknown_0x1C} {self.unknown_0x20} {self.floats}"
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        self.unknown_0x00 = rw.rw_uint16(self.unknown_0x00)
        self.unknown_0x02 = rw.rw_pad16(self.unknown_0x02)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_pointer(self.unknown_0x0C)
        self.unknown_0x10 = rw.rw_uint16(self.unknown_0x10)
        self.unknown_0x12 = rw.rw_uint16(self.unknown_0x12)
        self.unknown_0x14 = rw.rw_uint16(self.unknown_0x14)
        self.unknown_0x16 = rw.rw_uint16(self.unknown_0x16)
        self.unknown_0x18 = rw.rw_pointer(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_pointer(self.unknown_0x1C)
        self.unknown_0x20 = rw.rw_pointer(self.unknown_0x20)
        
    def rw_floats(self, rw):
        if self.unknown_0x0C:
            rw.assert_local_file_pointer_now_at("Data 1 Floats", self.unknown_0x0C)
            if rw.mode() == "read":
                self.floats = [None for _ in range(self.unknown_0x10)]
                
            for i in range(self.unknown_0x10):
                rw.mark_new_contents_array_member()
                self.floats[i] = rw.rw_float32s(self.floats[i], 4)
            

class MeshDeform(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = 0
        self.unknown_0x02 = 0
        self.unknown_0x04 = 1
        self.kfsg_vertex_count = None
        self.vertex_info_offset = None
        self.kfsg_vertex_offset = None
        
    def __repr__(self):
        return f"[KFSS::MeshDeform] {self.unknown_0x00} {self.unknown_0x02} {self.unknown_0x04} {self.kfsg_vertex_count} {self.vertex_info_offset} {self.kfsg_vertex_offset}"
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        self.unknown_0x00 = rw.rw_uint16(self.unknown_0x00) # Can be 4
        self.unknown_0x02 = rw.rw_uint16(self.unknown_0x02)
        self.unknown_0x04 = rw.rw_uint16(self.unknown_0x04)
        self.kfsg_vertex_count = rw.rw_uint16(self.kfsg_vertex_count)
        self.vertex_info_offset = rw.rw_pointer(self.vertex_info_offset)
        self.kfsg_vertex_offset = rw.rw_uint32(self.kfsg_vertex_offset)
        
        #rw.assert_equal(self.unknown_0x00, 0)
        rw.assert_equal(self.unknown_0x02, 0)
        rw.assert_equal(self.unknown_0x04, 1)
        
        
class VertexInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.kfsg_vertex_idx = None
        self.kfsg_vertex_count = None
        self.padding_0x06 = 0
        
    def __repr__(self):
        return f"[KFSS::VertexInfo] {self.kfsg_vertex_idx} {self.kfsg_vertex_count} {self.padding_0x06}"
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        self.kfsg_vertex_idx = rw.rw_uint32(self.kfsg_vertex_idx)
        self.kfsg_vertex_count = rw.rw_uint16(self.kfsg_vertex_count)
        self.padding_0x06 = rw.rw_pad16(self.padding_0x06)
        
class VertexFormat(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.vertex_size = None
        self.unknown_0x0C = None
        self.unknown_0x10 = None
        self.vertex_count = None
        self.vertex_partitions_offset = None
        self.partition_count = None
        
        self.vertex_partitions = []
        
    def __repr__(self):
        return f"[KFSS::VertexFormat] "\
            f"{self.unknown_0x00 if self.unknown_0x00 is None else hex(self.unknown_0x00)} "\
            f"{self.unknown_0x04 if self.unknown_0x04 is None else hex(self.unknown_0x04)} "\
            f"{self.vertex_size} {self.unknown_0x0C} "\
            f"{self.unknown_0x10} {self.vertex_count} {self.vertex_partitions_offset} {self.partition_count} "\
            f"{self.vertex_partitions}"
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.vertex_size = rw.rw_uint32(self.vertex_size)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)

        self.unknown_0x10 = rw.rw_uint32(self.unknown_0x10)
        self.vertex_count = rw.rw_uint32(self.vertex_count)
        self.vertex_partitions_offset = rw.rw_pointer(self.vertex_partitions_offset)
        self.partition_count = rw.rw_uint32(self.partition_count)
        
        #rw.assert_equal(self.unknown_0x00, 0x03000000)
        rw.assert_equal(self.unknown_0x04, 0x80000006)
        rw.assert_equal(self.unknown_0x0C, 0)
        rw.assert_equal(self.unknown_0x10, 0)
        
    def rw_vertex_partitions(self, rw):
        # These list (unused vertex count, used vertex count) pairs such that all numbers
        # sum to the total vertices on the target model
        # Doesn't necessarily occur in the order in which the meshes are defined, however...
        rw.mark_new_contents_array_member()
        if self.vertex_partitions_offset != 0:
            rw.assert_local_file_pointer_now_at("Vertex Partitions", self.vertex_partitions_offset)
            self.vertex_partitions = rw.rw_uint32s(self.vertex_partitions, (self.partition_count, 2))
            
