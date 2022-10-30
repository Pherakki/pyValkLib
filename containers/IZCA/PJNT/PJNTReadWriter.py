from pyValkLib.serialisation.ValkSerializable import Context, Serializable, ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray

from pyValkLib.containers.Metadata.POF0.POF0ReadWriter import POF0ReadWriter
from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

from pyValkLib.containers.Metadata.POF0.POF0Compression import POF0Validator
from pyValkLib.containers.Metadata.ENRS.ENRSCompression import ENRSValidator



class PJNTReadWriter(ValkSerializable32BH):
    FILETYPE = "PJNT"
    
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
        self.collider_subdata_1 = PointerIndexableArray(self.context)
        self.collider_subdata_2 = PointerIndexableArray(self.context)
        self.collider_subdata_3 = PointerIndexableArray(self.context)
        self.collider_subdata_4 = PointerIndexableArray(self.context)
        self.collider_subdata_5 = PointerIndexableArray(self.context)
        self.collider_subdata_6 = PointerIndexableArray(self.context)
        self.collider_subdata_1A = PointerIndexableArray(self.context)
        
        self.remainder = b''

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
        rw.align(rw.local_tell(), 0x10)
            
        # Section 2
        rw.mark_new_contents_array()
        data_offsets = sorted(set(o.data_offset for o in self.colliders if o.data_offset > 0))
        if len(data_offsets):
            rw.assert_local_file_pointer_now_at("Collider Data", data_offsets[0])
            if rw.mode() == "read":
                self.collider_data.data = [ColliderData(self.context) for _ in range(len(data_offsets))]
            rw.rw_obj(self.collider_data)
        rw.align(rw.local_tell(), 0x10)
                       
        # Section 3
        rw.mark_new_contents_array()
        data_offsets = set()
        data_offsets.update(o.unknown_0x04 for o in self.collider_data if o.unknown_0x04 > 0)
        data_offsets.update(o.unknown_0x08 for o in self.collider_data if o.unknown_0x08 > 0)
        data_offsets = sorted(data_offsets)
        
        if len(data_offsets):
            rw.assert_local_file_pointer_now_at("Collider SubData 1", data_offsets[0])
            if rw.mode() == "read":
                self.collider_subdata_1.data = [ColliderSubData1(self.context) for _ in range(len(data_offsets))]
            rw.rw_obj(self.collider_subdata_1)
        rw.align(rw.local_tell(), 0x10)
                       
        # Section 4
        rw.mark_new_contents_array()
        data_offsets = set()
        data_offsets.update(o.unknown_0x10 for o in self.collider_data if o.unknown_0x10 > 0)
        data_offsets.update(o.unknown_0x18 for o in self.collider_data if o.unknown_0x18 > 0)
        data_offsets.update(o.unknown_0x1C for o in self.collider_data if o.unknown_0x1C > 0)
        data_offsets.update(o.unknown_0x20 for o in self.collider_data if o.unknown_0x20 > 0)
        data_offsets.update(o.unknown_0x24 for o in self.collider_data if o.unknown_0x24 > 0)
        data_offsets = sorted(data_offsets)
        
        if len(data_offsets):
            rw.assert_local_file_pointer_now_at("Collider SubData 2", data_offsets[0])
            if rw.mode() == "read":
                self.collider_subdata_2.data = [ColliderSubData2(self.context) for _ in range(len(data_offsets))]
            rw.rw_obj(self.collider_subdata_2)
        rw.align(rw.local_tell(), 0x10)

        # Section 5
        rw.mark_new_contents_array()
        data_offsets = sorted(set(o.unknown_0x28 for o in self.collider_data if o.unknown_0x28 > 0))
        
        if len(data_offsets):
            rw.assert_local_file_pointer_now_at("Collider SubData 3", data_offsets[0])
            if rw.mode() == "read":
                self.collider_subdata_3.data = [ColliderSubData3(self.context) for _ in range(len(data_offsets))]
            rw.rw_obj(self.collider_subdata_3)
        rw.align(rw.local_tell(), 0x10)
            
        # Section 6
        rw.mark_new_contents_array()
        data_offsets = set()
        data_offsets.update(o.unknown_0x2C for o in self.collider_data if o.unknown_0x2C > 0)
        data_offsets.update(o.unknown_0x30 for o in self.collider_data if o.unknown_0x30 > 0)
        data_offsets.update(o.unknown_0x34 for o in self.collider_data if o.unknown_0x34 > 0)
        data_offsets.update(o.unknown_0x38 for o in self.collider_data if o.unknown_0x38 > 0)
        data_offsets.update(o.unknown_0x3C for o in self.collider_data if o.unknown_0x3C > 0)
        data_offsets.update(o.unknown_0x40 for o in self.collider_data if o.unknown_0x40 > 0)
        data_offsets = sorted(data_offsets)
        
        if len(data_offsets):
            rw.assert_local_file_pointer_now_at("Collider SubData 4", data_offsets[0])
            if rw.mode() == "read":
                self.collider_subdata_4.data = [ColliderSubData4(self.context) for _ in range(len(data_offsets))]
            rw.rw_obj(self.collider_subdata_4)
        rw.align(rw.local_tell(), 0x10)
        
        # Section 7
        rw.mark_new_contents_array()
        data_offsets = set()
        data_offsets.update(o.unknown_0x44 for o in self.collider_data if o.unknown_0x44 > 0)
        data_offsets.update(o.unknown_0x48 for o in self.collider_data if o.unknown_0x48 > 0)
        data_offsets = sorted(data_offsets)
        
        if len(data_offsets):
            rw.assert_local_file_pointer_now_at("Collider SubData 5", data_offsets[0])
            if rw.mode() == "read":
                self.collider_subdata_5.data = [ColliderSubData5(self.context) for _ in range(len(data_offsets))]
            rw.rw_obj(self.collider_subdata_5)
        rw.align(rw.local_tell(), 0x10)
        
        # Section 8
        rw.mark_new_contents_array()
        data_offsets = set()
        data_offsets.update(o.unknown_0x4C for o in self.collider_data if o.unknown_0x4C > 0)
        data_offsets.update(o.unknown_0x50 for o in self.collider_data if o.unknown_0x50 > 0)
        data_offsets = sorted(data_offsets)
        
        if len(data_offsets):
            rw.assert_local_file_pointer_now_at("Collider SubData 6", data_offsets[0])
            if rw.mode() == "read":
                self.collider_subdata_6.data = [ColliderSubData6(self.context) for _ in range(len(data_offsets))]
            rw.rw_obj(self.collider_subdata_6)
        rw.align(rw.local_tell(), 0x10)
        
        # Section 9
        rw.mark_new_contents_array()
        data_offsets = set()
        data_offsets.update(o.unknown_0x04 for o in self.collider_subdata_1 if o.unknown_0x04 > 0)
        data_offsets.update(o.unknown_0x08 for o in self.collider_subdata_1 if o.unknown_0x08 > 0)
        data_offsets.update(o.unknown_0x0C for o in self.collider_subdata_1 if o.unknown_0x0C > 0)
        data_offsets.update(o.unknown_0x04 for o in self.collider_subdata_5 if o.unknown_0x04 > 0)
        data_offsets.update(o.unknown_0x04 for o in self.collider_subdata_6 if o.unknown_0x04 > 0)
        data_offsets = sorted(data_offsets)
        
        if len(data_offsets):
            rw.assert_local_file_pointer_now_at("Collider SubData 1A", data_offsets[0])
            if rw.mode() == "read":
                self.collider_subdata_1A.data = [ColliderSubData1A(self.context) for _ in range(len(data_offsets))]
            rw.rw_obj(self.collider_subdata_1A)
        rw.align(rw.local_tell(), 0x10)
        
        self.remainder = rw.rw_bytestring(self.remainder, self.header.header_length + self.header.data_length - rw.local_tell())
        
            
    def __repr__(self):
        return f"PJNT Object [{self.header.depth}] [0x{self.header.flags:0>8x}]."

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
        
        self.filetype     = None
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.data_count   = None
        
        self.data_offset  = None
        
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        self.filetype     = rw.rw_str(self.filetype, 4)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.data_count   = rw.rw_uint32(self.data_count)
        
        self.data_offset  = rw.rw_pointer(self.data_offset)
        rw.align(0x14, 0x20)
        
        self.unknown_0x20 = rw.rw_uint32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_uint32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_uint32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_uint32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_uint32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_uint32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_uint32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_uint32(self.unknown_0x3C)
        
        rw.assert_equal(self.unknown_0x04, 0)
        rw.assert_equal(self.unknown_0x08, 0)
        rw.assert_equal(self.unknown_0x28, 0)
        rw.assert_equal(self.unknown_0x2C, 0)
        rw.assert_equal(self.unknown_0x30, 0)
        rw.assert_equal(self.unknown_0x34, 0)
        rw.assert_equal(self.unknown_0x38, 0)
        rw.assert_equal(self.unknown_0x3C, 0)
        
    def __repr__(self):
        return f"[PACT::Collider] {self.filetype} {self.data_count} {self.data_offset} {self.unknown_0x20} {self.unknown_0x24}"

class ColliderData(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        
        self.unknown_0x10 = None
        self.unknown_0x14 = None
        self.unknown_0x18 = None
        self.unknown_0x1C = None
        
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        
        self.unknown_0x50 = 0
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_pointer(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_bytestring(self.unknown_0x0C, 4)
        
        self.unknown_0x10 = rw.rw_pointer(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_bytestring(self.unknown_0x14, 4)
        self.unknown_0x18 = rw.rw_pointer(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_pointer(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_pointer(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_pointer(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pointer(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pointer(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pointer(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pointer(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pointer(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pointer(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_pointer(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_pointer(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_pointer(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_pointer(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_pointer(self.unknown_0x50)
        
    def __repr__(self):
        return f"[PJNT::ColliderData] {self.unknown_0x00} {self.unknown_0x04} {self.unknown_0x08} {self.unknown_0x0C} "\
            f"{self.unknown_0x10} {self.unknown_0x14} {self.unknown_0x18} {self.unknown_0x1C} "\
            f"{self.unknown_0x20} {self.unknown_0x24} {self.unknown_0x28} {self.unknown_0x2C} "\
            f"{self.unknown_0x30} {self.unknown_0x34} {self.unknown_0x38} {self.unknown_0x3C} "\
            f"{self.unknown_0x40} {self.unknown_0x44} {self.unknown_0x48} {self.unknown_0x4C} "\
            f"{self.unknown_0x50}"


class ColliderSubData1(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x02 = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        rw.align(0x02, 0x04)
        self.unknown_0x02 = rw.rw_uint16(self.unknown_0x02)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_pointer(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_pointer(self.unknown_0x0C)
        
    def __repr__(self):
        return f"[PJNT::ColliderSubData1] {self.unknown_0x02} {self.unknown_0x04} {self.unknown_0x08} {self.unknown_0x0C}"

class ColliderSubData2(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        self.unknown_0x10 = None
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        self.unknown_0x00 = rw.rw_uint8(self.unknown_0x00)
        rw.align(0x01, 0x04)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        
    def __repr__(self):
        return f"[PJNT::ColliderSubData2] {self.unknown_0x00} {self.unknown_0x04} {self.unknown_0x08} {self.unknown_0x0C} {self.unknown_0x10}"
    
class ColliderSubData3(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x01 = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        self.unknown_0x00 = rw.rw_uint8(self.unknown_0x00)
        self.unknown_0x01 = rw.rw_uint8(self.unknown_0x01)
        rw.align(0x02, 0x04)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        
    def __repr__(self):
        return f"[PJNT::ColliderSubData3] {self.unknown_0x00} {self.unknown_0x01} {self.unknown_0x04} {self.unknown_0x08}"

class ColliderSubData4(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x01 = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        self.unknown_0x00 = rw.rw_uint8(self.unknown_0x00)
        self.unknown_0x01 = rw.rw_uint8(self.unknown_0x01)
        rw.align(0x02, 0x04)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        
    def __repr__(self):
        return f"[PJNT::ColliderSubData4] {self.unknown_0x00} {self.unknown_0x01} {self.unknown_0x04} {self.unknown_0x08} {self.unknown_0x0C}"

class ColliderSubData5(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        self.unknown_0x00 = rw.rw_uint8(self.unknown_0x00)
        rw.align(0x01, 0x04)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        
    def __repr__(self):
        return f"[PJNT::ColliderSubData5] {self.unknown_0x00} {self.unknown_0x04}"

class ColliderSubData6(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        self.unknown_0x00 = rw.rw_uint8(self.unknown_0x00)
        rw.align(0x01, 0x04)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        
    def __repr__(self):
        return f"[PJNT::ColliderSubData6] {self.unknown_0x00} {self.unknown_0x04}"
    
class ColliderSubData1A(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        self.unknown_0x00 = rw.rw_float32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        
    def __repr__(self):
        return f"[PJNT::ColliderSubData1A] {self.unknown_0x00} {self.unknown_0x04} {self.unknown_0x08} {self.unknown_0x0C}"
