from pyValkLib.serialisation.ValkSerializable import Serializable, ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray
from pyValkLib.containers.Metadata.POF0.POF0ReadWriter import POF0ReadWriter
from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

from pyValkLib.containers.Metadata.POF0.POF0Compression import POF0Validator
from pyValkLib.containers.Metadata.ENRS.ENRSCompression import ENRSValidator

class KFMAReadWriter(ValkSerializable32BH):
    FILETYPE = "KFMA"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x18000000
        
        self.unknown_0x00 = None
        
        self.unknown_0x10 = None
        self.frame_count  = None
        self.framerate    = None
        self.unknown_0x1C = None
        
        self.count_1      = None
        self.count_2      = None
        self.count_3      = None
        self.count_4      = None
        self.count_5      = None
        self.bone_count   = None
        self.count_7      = None
        
        self.offset_1     = None
        self.offset_2     = None
        self.offset_3     = None
        
        self.offset_4     = None
        self.offset_5     = None
        self.bones_offset = None
        self.offset_7     = None
        
        self.data_1   = []
        self.data_1A  = []
        self.data_2   = []
        self.data_2A  = []
        self.data_3   = []
        self.bones   = []
        self.fcurve_offsets  = []
        self.fcurve_defs     = []
        self.bone_transforms = []
        
        self.POF0 = POF0ReadWriter(endianness)
        self.ENRS = ENRSReadWriter(endianness)
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.POF0, self.ENRS, self.EOFC,
                ENRSValidator(self),
                POF0Validator(self)]
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))
        
        self.unknown_0x00 = rw.rw_float32(self.unknown_0x00)
        rw.align(rw.local_tell(), 0x10)
        
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.frame_count  = rw.rw_float32(self.frame_count)
        self.framerate    = rw.rw_float32(self.framerate)
        self.unknown_0x1C = rw.rw_float32(self.unknown_0x1C)
        
        self.count_1      = rw.rw_uint16(self.count_1)
        self.count_2      = rw.rw_uint16(self.count_2)
        self.count_3      = rw.rw_uint16(self.count_3)
        rw.align(rw.local_tell(), 0x08)
        self.count_4      = rw.rw_uint16(self.count_4)
        self.count_5      = rw.rw_uint16(self.count_5)
        self.bone_count   = rw.rw_uint16(self.bone_count)
        self.count_7      = rw.rw_uint16(self.count_7)
        
        self.offset_1 = rw.rw_pointer(self.offset_1)
        self.offset_2 = rw.rw_pointer(self.offset_2)
        self.offset_3 = rw.rw_pointer(self.offset_3)
        rw.align(rw.local_tell(), 0x10)
        
        self.offset_4 = rw.rw_pointer(self.offset_4)
        self.offset_5 = rw.rw_pointer(self.offset_5)
        self.bones_offset = rw.rw_pointer(self.bones_offset)
        self.offset_7 = rw.rw_pointer(self.offset_7)
                    
        rw.assert_is_zero(self.count_4)
        rw.assert_is_zero(self.count_5)
        rw.assert_is_zero(self.count_7)
        rw.assert_is_zero(self.offset_4)
        rw.assert_is_zero(self.offset_5)
        rw.assert_is_zero(self.offset_7)
        
        self.rw_data1(rw)
        self.rw_data2(rw)
        self.rw_data3(rw)
        self.rw_data1A(rw)
        self.rw_data2A(rw)
        self.rw_bones(rw)
        self.rw_fcurve_offsets(rw)
        self.rw_fcurve_defs(rw)
        self.rw_bone_transforms(rw)
        self.rw_fcurve_data(rw)
        
        
    def rw_data1(self, rw):
        if self.offset_1:
            rw.mark_new_contents_array()
            rw.assert_local_file_pointer_now_at("Data 1", self.offset_1)
            self.data_1 = rw.rw_obj_array(self.data_1, lambda: Data1(self.context), self.count_1)
    
    def rw_data2(self, rw):
        if self.offset_2:
            rw.mark_new_contents_array()
            rw.assert_local_file_pointer_now_at("Data 2", self.offset_2)
            self.data_2 = rw.rw_obj_array(self.data_2, lambda: Data2(self.context), self.count_2)
            rw.align(rw.local_tell(), 0x10)
    
    def rw_data3(self, rw):
        if self.offset_3:
            rw.mark_new_contents_array()
            rw.assert_local_file_pointer_now_at("Data 3", self.offset_3)
            self.data_3 = rw.rw_obj_array(self.data_3, lambda: Data3(self.context), self.count_3)

    def rw_data1A(self, rw):
        offsets = set()
        for o in self.data_1:
            offsets.update(set(o.offset_1 + 2*i for i in range(o.count_1)))
        offsets = sorted(offsets)
        
        if len(offsets):
            rw.mark_new_contents_array()
            rw.assert_local_file_pointer_now_at("Data 1A", offsets[0])
            self.data_1A = rw.rw_int16s(self.data_1A, len(offsets))
            rw.align(rw.local_tell(), 0x10)
            
    def rw_data2A(self, rw):
        offsets = set()
        for o in self.data_2:
            offsets.update(set(o.offset_1 + 2*i for i in range(o.count_1)))
        offsets = sorted(offsets)
        
        if len(offsets):
            rw.mark_new_contents_array()
            rw.assert_local_file_pointer_now_at("Data 2A", offsets[0])
            self.data_2A = rw.rw_int16s(self.data_2A, len(offsets))
            rw.align(rw.local_tell(), 0x10)
            
    def rw_bones(self, rw):
        if self.bones_offset:
            rw.mark_new_contents_array()
            rw.assert_local_file_pointer_now_at("Bones", self.bones_offset)
            self.bones = rw.rw_obj_array(self.bones, lambda: Bone(self.context), self.bone_count)
            
    def rw_fcurve_offsets(self, rw):
        offsets = sorted(set(o.animation_offset + 4*i 
                             for o in self.bones
                             for i in range(o.get_count())
                             if o.animation_offset != 0))
        
        if len(offsets):
            rw.mark_new_contents_array()
            rw.assert_local_file_pointer_now_at("FCurve Offsets", offsets[0])
            self.fcurve_offsets = rw.rw_pointers(self.fcurve_offsets, len(offsets))
            rw.align(rw.local_tell(), 0x10)
            
    def rw_fcurve_defs(self, rw):
        offsets = sorted(set(offset for offset in self.fcurve_offsets if offset != 0))
        
        if len(offsets):
            rw.mark_new_contents_array()
            rw.assert_local_file_pointer_now_at("FCurve Defs", offsets[0])
            self.fcurve_defs = rw.rw_obj_array(self.fcurve_defs, lambda: FCurveDef(self.context), len(offsets))
            rw.align(rw.local_tell(), 0x10)
            
    def rw_bone_transforms(self, rw):
        offsets = sorted(set(o.transform_offset + 4*i 
                             for o in self.bones
                             for i in range(o.get_count())
                             if o.transform_offset != 0))

        if len(offsets):
            rw.mark_new_contents_array()
            rw.assert_local_file_pointer_now_at("Bone Transforms", offsets[0])
            self.bone_transforms = rw.rw_float32s(self.bone_transforms, len(offsets))
            rw.align(rw.local_tell(), 0x10)
            
    def rw_fcurve_data(self, rw):
        for fcurve_def in self.fcurve_defs:
            fcurve_def.rw_framedata(rw, int(self.frame_count))
        rw.align(rw.local_tell(), 0x10)
            
        
class Data1(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.count_1 = None
        self.count_2 = None
        self.count_3 = None
        self.count_4 = None
        
        self.offset_1 = None
        self.offset_2 = None
        self.offset_3 = None
        self.offset_4 = None
        
    def __repr__(self):
        return f"[KFMA::Data1] {self.count_1} {self.count_2} {self.count_3} {self.count_4} "\
               f"{self.offset_1} {self.offset_2} {self.offset_3} {self.offset_4}"
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        self.count_1 = rw.rw_uint16(self.count_1)
        self.count_2 = rw.rw_uint16(self.count_2)
        self.count_3 = rw.rw_uint16(self.count_3)
        self.count_4 = rw.rw_uint16(self.count_4)
        rw.align(0x08, 0x10)
        
        self.offset_1 = rw.rw_pointer(self.offset_1)
        self.offset_2 = rw.rw_pointer(self.offset_2)
        self.offset_3 = rw.rw_pointer(self.offset_3)
        self.offset_4 = rw.rw_pointer(self.offset_4)
            
        rw.assert_is_zero(self.count_2)
        rw.assert_is_zero(self.count_3)
        rw.assert_is_zero(self.count_4)
        rw.assert_is_zero(self.offset_2)
        rw.assert_is_zero(self.offset_3)
        rw.assert_is_zero(self.offset_4)
        
class Data2(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.count_1 = None
        self.offset_1 = None
        
        self.unknown_0x10 = None
        self.unknown_0x14 = None
        
    def __repr__(self):
        return f"[KFMA::Data2] {self.unknown_0x00} {self.unknown_0x04} {self.count_1} "\
               f"{self.offset_1} {self.unknown_0x10} {self.unknown_0x14}"
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint16(self.unknown_0x04)
        rw.align(0x06, 0x0B)
        self.count_1      = rw.rw_uint8(self.count_1)
        self.offset_1     = rw.rw_pointer(self.offset_1)
        
        self.unknown_0x10 = rw.rw_uint16(self.unknown_0x10)
        rw.align(0x12, 0x14)
        self.unknown_0x14 = rw.rw_uint32(self.unknown_0x14)
                
class Data3(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.unknown_0x0A = None
        self.unknown_0x0C = None
        
    def __repr__(self):
        return f"[KFMA::Data3] {self.unknown_0x00} {self.unknown_0x04} {self.unknown_0x08} "\
               f"{self.unknown_0x0A} {self.unknown_0x0C}"
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint16(self.unknown_0x04)
        rw.align(0x06, 0x08)
        self.unknown_0x08 = rw.rw_uint16(self.unknown_0x08)
        self.unknown_0x0A = rw.rw_uint16(self.unknown_0x0A)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        
class Bone(Serializable):
    def __init__(self, context):
        super().__init__(context)

        self.flags = None
        self.animation_offset = None
        self.transform_offset = None
        
    def __repr__(self):
        return f"[KFMA::Bone] {self.flags} {self.animation_offset} {self.transform_offset}"
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        self.flags = rw.rw_uint64(self.flags)
        self.animation_offset = rw.rw_pointer(self.animation_offset)
        self.transform_offset = rw.rw_pointer(self.transform_offset)
        
    def get_count(self):
        count = 0
        val = self.flags
        for i in range(64):
            count += val & 1
            val >>= 1
        return count            
        
class FCurveDef(Serializable):
    def __init__(self, context):
        super().__init__(context)

        self.unknown_0x00 = None
        self.type         = None
        self.divisor      = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.offset       = None
        
        self.frame_data = []
        
    def __repr__(self):
        return f"[KFMA::FCurveDef] {self.unknown_0x00} {self.type} {self.divisor} {self.unknown_0x04} {self.unknown_0x08} {self.offset}"
    
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        
        self.unknown_0x00 = rw.rw_uint8(self.unknown_0x00)
        self.type         = rw.rw_uint8(self.type)
        self.divisor      = rw.rw_uint8(self.divisor)
        rw.align(0x03, 0x04)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.offset       = rw.rw_pointer(self.offset)

        rw.assert_equal(self.unknown_0x00, 1)
        rw.assert_is_zero(self.unknown_0x04)
        rw.assert_is_zero(self.unknown_0x08)

    def rw_framedata(self, rw, frame_count):
        divisor = self.divisor
        divisor = 2**divisor
        
        rw.assert_local_file_pointer_now_at("Frame Data", self.offset)
        
        if self.type == 1:
            op = rw.rw_float32s
        elif self.type == 2:
            op = lambda x, shape: rw.rw_ratio16s(x, divisor, shape)
        elif self.type == 3:
            op = lambda x, shape: rw.rw_ratio8s(x, divisor, shape)
        
        self.frame_data = op(self.frame_data, frame_count + 1)
