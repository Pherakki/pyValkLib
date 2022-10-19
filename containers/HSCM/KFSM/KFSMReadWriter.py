from pyValkLib.serialisation.ValkSerializable import Serializable, ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArrayFloat32
from pyValkLib.containers.Metadata.POF0.POF0ReadWriter import POF0ReadWriter
from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

from pyValkLib.containers.Metadata.POF0.POF0Compression import POF0Validator
from pyValkLib.containers.Metadata.ENRS.ENRSCompression import ENRSValidator

class KFSMReadWriter(ValkSerializable32BH):
    FILETYPE = "KFSM"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x18000000
        
        self.contents = Contents(self.context)
        self.bone = Bone(self.context)
        self.fcurve_defs = []
        self.fcurve_offsets = []
        self.bone_transform = []
        self.fcurve_data = []
        
        self.POF0 = POF0ReadWriter("<")
        self.ENRS = ENRSReadWriter("<")
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.POF0, self.ENRS, self.EOFC,
                ENRSValidator(self),
                POF0Validator(self)]
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))

        self.contents = rw.rw_obj(self.contents)
        
        self.rw_bone(rw)
        self.rw_fcurve_defs(rw)
        self.rw_fcurve_offsets(rw)
        self.rw_transform(rw)
        self.rw_fcurve_data(rw)
        
        rw.rw_bytestring(None, self.header.header_length + self.header.data_length - rw.local_tell())

    def rw_bone(self, rw):
        rw.mark_new_contents_array()
        rw.assert_local_file_pointer_now_at("Bone", self.contents.unknown_0x14)
        rw.rw_obj(self.bone)

    def rw_fcurve_defs(self, rw):
        rw.mark_new_contents_array()
        fcurve_def_count = (self.bone.animation_offset - rw.local_tell()) // 0x10
        self.fcurve_defs = rw.rw_obj_array(self.fcurve_defs, lambda: FCurveDef(self.context), fcurve_def_count)

    def rw_fcurve_offsets(self, rw):
        rw.mark_new_contents_array()
        if self.bone.animation_offset:
            rw.assert_local_file_pointer_now_at("FCurve Offsets", self.bone.animation_offset)
            self.fcurve_offsets = rw.rw_pointers(self.fcurve_offsets, self.bone.get_count())
            
    def rw_transform(self, rw):
        if self.bone.transform_offset:
            rw.assert_local_file_pointer_now_at("Bone Transform", self.bone.transform_offset)
            self.bone_transform = rw.rw_float32s(self.bone_transform, self.bone.get_count())
            
    def rw_fcurve_data(self, rw):
        offsets = sorted(set(o.offset + 4*i
                             for o in self.fcurve_defs
                             for i in range(int(self.contents.frame_count) + 1)))
        
        if len(offsets):
            rw.assert_local_file_pointer_now_at("FCurve Data", offsets[0])
            self.fcurve_data = rw.rw_float32s(self.fcurve_data, len(offsets))
        rw.align(rw.local_tell(), 0x10)

class Contents(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.flags        = 0x80000003
        self.unknown_0x04 = None
        self.frame_count  = None
        self.framerate    = None
        
        self.unknown_0x10 = None
        self.unknown_0x14 = None
        self.unknown_0x18 = None
        self.unknown_0x1C = None
        
    def __repr__(self):
        return f"[KFSM::Contents] " \
               f"{self.flags if self.flags is None else hex(self.flags)} "\
               f"{self.unknown_0x04} {self.frame_count} {self.framerate} " \
               f"{self.unknown_0x10} {self.unknown_0x14} {self.unknown_0x18} {self.unknown_0x1C}"
        
    def read_write(self, rw):
        rw.mark_new_contents_array()
        self.flags        = rw.rw_uint32(self.flags)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.frame_count  = rw.rw_float32(self.frame_count)
        self.framerate    = rw.rw_float32(self.framerate)
        
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_pointer(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_uint32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_uint32(self.unknown_0x1C)
        rw.align(rw.local_tell(), 0x60)
        
        
class Bone(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.flags = None
        self.animation_offset = None
        self.transform_offset = None
        
    def __repr__(self):
        return f"[KFSM::Bone] "\
               f"{self.flags if self.flags is None else hex(self.flags)} "\
               f"{self.animation_offset} {self.transform_offset}"
    
    def read_write(self, rw):
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
        self.type = None
        self.divisor = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.offset       = None

    def __repr__(self):
        return f"[KFSM::FCurveDef] {self.unknown_0x00} {self.type} {self.divisor} "\
               f"{self.unknown_0x04} {self.unknown_0x08} {self.offset}"

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint8(self.unknown_0x00)
        self.type         = rw.rw_uint8(self.type)
        self.divisor      = rw.rw_uint8(self.divisor)
        rw.align(rw.local_tell(), 0x04)
        
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.offset       = rw.rw_pointer(self.offset)

        rw.assert_equal(self.unknown_0x00, 1)
        rw.assert_is_zero(self.unknown_0x04)
        rw.assert_is_zero(self.unknown_0x08)
