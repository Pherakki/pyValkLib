from pyValkLib.serialisation.ValkSerializable import Context, Serializable, ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray
from pyValkLib.containers.Metadata.POF0.POF0ReadWriter import POF0ReadWriter
from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

from pyValkLib.containers.Metadata.POF0.POF0Compression import POF0Validator
from pyValkLib.containers.Metadata.ENRS.ENRSCompression import ENRSValidator

class PACTReadWriter(ValkSerializable32BH):
    FILETYPE = "PACT"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.data_length = 0
        self.header.flags = 0x18000000
        self.POF0 = POF0ReadWriter("<")
        self.ENRS = ENRSReadWriter("<")
        self.EOFC = EOFCReadWriter("<")
        
        self.contents = Contents(self.context)
        self.colliders = []
        self.collider_data = PointerIndexableArray(self.context)
        self.collider_data_data = PointerIndexableArray(self.context)

    def get_subcontainers(self):
        return [self.POF0, self.ENRS, self.EOFC,
                ENRSValidator(self),
                POF0Validator(self)]
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))

        rw.mark_new_contents_array()
        rw.rw_obj(self.contents)
        
        # Section 1
        rw.assert_local_file_pointer_now_at("Colliders", self.contents.colliders_offset)
        rw.mark_new_contents_array()
        self.colliders = rw.rw_obj_array(self.colliders, lambda: Collider(self.context), self.contents.container_count)
            
        # Section 2
        rw.mark_new_contents_array()
        data_offsets = sorted(set(o.data_offset for o in self.colliders if o.data_offset > 0))
        if len(data_offsets):
            rw.assert_local_file_pointer_now_at("Collider Data", data_offsets[0])
            if rw.mode() == "read":
                self.collider_data.data = [ColliderData(self.context) for _ in range(len(data_offsets))]
            rw.rw_obj(self.collider_data)
            
            
        # Section 3
        data_offsets = set()
        data_offsets.update(o.offset_1 for o in self.collider_data if o.offset_1 > 0)
        data_offsets.update(o.offset_2 for o in self.collider_data if o.offset_2 > 0)
        data_offsets.update(o.offset_3 for o in self.collider_data if o.offset_3 > 0)
        data_offsets.update(o.offset_4 for o in self.collider_data if o.offset_4 > 0)
        data_offsets = sorted(data_offsets)
        
        rw.mark_new_contents_array()
        if len(data_offsets):
            rw.assert_local_file_pointer_now_at("Collider Data Data", data_offsets[0])
            if rw.mode() == "read":
                self.collider_data_data.data = [ColliderDataData(self.context) for _ in range(len(data_offsets))]
            rw.rw_obj(self.collider_data_data)

    def __repr__(self):
        return f"PACT Object [{self.header.depth}] [0x{self.header.flags:0>8x}]."

class Contents(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00     = None
        self.container_count  = None
        self.colliders_offset = None
        
    def __repr__(self):
        return f"[PACT::Contents] {self.unknown_0x00} {self.container_count} {self.colliders_offset}"
    
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        self.unknown_0x00     = rw.rw_uint32(self.unknown_0x00)
        self.container_count  = rw.rw_uint32(self.container_count)
        self.colliders_offset = rw.rw_pointer(self.colliders_offset)
        rw.align(rw.local_tell(), 0x10)

class Collider(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.filetype = None
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.data_offset  = None
        
        self.data_count   = None
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        self.filetype = rw.rw_str(self.filetype, 4)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.data_offset  = rw.rw_pointer(self.data_offset)
        
        self.data_count = rw.rw_uint32(self.data_count)
        self.unknown_0x14 = rw.rw_uint32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_uint32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_uint32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_uint32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_uint32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_uint32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_uint32(self.unknown_0x2C)
        
        rw.assert_equal(self.unknown_0x04, 0)
        rw.assert_equal(self.unknown_0x08, 0)
        rw.assert_equal(self.unknown_0x14, 0)
        rw.assert_equal(self.unknown_0x18, 0)
        rw.assert_equal(self.unknown_0x1C, 0)
        rw.assert_equal(self.unknown_0x20, 0)
        rw.assert_equal(self.unknown_0x24, 0)
        rw.assert_equal(self.unknown_0x28, 0)
        rw.assert_equal(self.unknown_0x2C, 0)
        
    def __repr__(self):
        return f"[PACT::Collider] {self.filetype} {self.data_offset} {self.data_count}"

class ColliderData(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.unknown_0x06 = None
        self.unknown_0x08 = None
        self.offset_1     = None
        
        self.offset_2     = None
        self.offset_3     = None
        self.unknown_0x18 = None
        self.unknown_0x1C = None
        
        self.offset_4     = None
        self.unknown_0x24 = None
        self.unknown_0x28 = None
        self.unknown_0x2C = None
        
        self.unknown_0x30 = None
        self.unknown_0x34 = None
        
    def __repr__(self):
        return f"[PACT::ColliderData] {self.unknown_0x00} "\
            f"{self.unknown_0x04} {self.unknown_0x06} {self.unknown_0x08} {self.offset_1} "\
            f"{self.offset_2} {self.offset_3} {self.unknown_0x18} {self.unknown_0x1C} "\
            f"{self.offset_4} {self.unknown_0x24} {self.unknown_0x28} {self.unknown_0x2C} "\
            f"{self.unknown_0x30} {self.unknown_0x34}"
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint16(self.unknown_0x04)
        self.unknown_0x06 = rw.rw_uint16(self.unknown_0x06)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.offset_1     = rw.rw_pointer(self.offset_1)
        
        self.offset_2     = rw.rw_pointer(self.offset_2)
        self.offset_3     = rw.rw_pointer(self.offset_3)
        self.unknown_0x18 = rw.rw_float32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_float32(self.unknown_0x1C)
        
        self.offset_4     = rw.rw_pointer(self.offset_4)
        self.unknown_0x24 = rw.rw_float32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_float32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_float32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_uint32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_uint32(self.unknown_0x34)
        rw.align(0x38, 0x40)

class ColliderDataData(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        
    def __repr__(self):
        return f"[PACT::ColliderDataData] {self.unknown_0x00} "\
               f"{self.unknown_0x04} {self.unknown_0x08} {self.unknown_0x0C}"
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        