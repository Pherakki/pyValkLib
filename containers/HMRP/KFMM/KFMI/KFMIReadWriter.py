from pyValkLib.serialisation.ValkSerializable import Serializable, ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArrayUint32, PointerIndexableArrayFloat32
from pyValkLib.containers.Metadata.POF0.POF0ReadWriter import POF0ReadWriter
from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

from pyValkLib.containers.Metadata.POF0.POF0Compression import POF0Validator
from pyValkLib.containers.Metadata.ENRS.ENRSCompression import ENRSValidator

class KFMIReadWriter(ValkSerializable32BH):
    FILETYPE = "KFMI"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x18000004
        
        self.unknown_0x00         = None
        self.anim_curve_count     = None
        self.unknown_0x08         = None
        self.frame_count          = None
        
        self.framerate            = None
        self.unknown_0x14         = None
        self.anim_curves_offset   = None
        self.frame_indices_offset = None
        
        self.unknown_0x20 = None
        self.unknown_0x24 = None
        self.unknown_0x28 = None
        
        self.anim_curves = []
        self.all_frames = []
        self.frame_indices = PointerIndexableArrayUint32(self.context)
        self.frame_values = PointerIndexableArrayFloat32(self.context)

        self.POF0 = POF0ReadWriter("<")
        self.ENRS = ENRSReadWriter("<")
        self.EOFC = EOFCReadWriter("<")

    def __repr__(self):
        return f"KFMM Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains POF0, ENRS."
    
    def get_subcontainers(self):
        return [self.POF0, self.ENRS, self.EOFC,
                POF0Validator(self),
                ENRSValidator(self)]
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x18000004, lambda x: hex(x))
        rw.mark_new_contents_array()
        
        self.unknown_0x00         = rw.rw_uint32(self.unknown_0x00)
        self.anim_curve_count     = rw.rw_uint32(self.anim_curve_count)
        self.unknown_0x08         = rw.rw_uint32(self.unknown_0x08)
        self.frame_count          = rw.rw_float32(self.frame_count)
        
        self.framerate            = rw.rw_float32(self.framerate)
        self.unknown_0x14         = rw.rw_float32(self.unknown_0x14)
        self.anim_curves_offset   = rw.rw_pointer(self.anim_curves_offset)
        self.frame_indices_offset = rw.rw_pointer(self.frame_indices_offset)
        
        self.unknown_0x20       = rw.rw_uint32(self.unknown_0x20)
        self.unknown_0x24       = rw.rw_uint32(self.unknown_0x24)
        self.unknown_0x28       = rw.rw_uint32(self.unknown_0x28)
        
        rw.align(rw.local_tell(), 0x20)
        
        self.rw_animation_curves(rw)
        self.rw_frame_indices(rw)
        self.rw_frame_values(rw)
        rw.align(rw.local_tell(), 0x10)

    def rw_animation_curves(self, rw):
        rw.mark_new_contents_array()
        rw.assert_local_file_pointer_now_at("Animation Curves", self.anim_curves_offset)
        self.anim_curves = rw.rw_obj_array(self.anim_curves, lambda: AnimationCurve(self.context), self.anim_curve_count)
        
    def rw_frame_indices(self, rw):
        rw.mark_new_contents_array()
        
        # Generate all offsets
        offsets = set()
        for o in self.anim_curves:
            offsets.update(set(o.frame_indices_offset + i*4 for i in range(o.frame_count+1)))
        offsets = sorted(offsets)
        first_offset = offsets[0]

        # Read the master list of frame indices
        rw.assert_local_file_pointer_now_at("List of All Frames", self.frame_indices_offset)
        count = (first_offset - self.frame_indices_offset) // 4
        self.all_frames = rw.rw_uint32s(self.all_frames, count)
        
        # Read the individual frame indices
        frame_count = len(offsets)
        if rw.mode() == "read":
            self.frame_indices.data = [None for _ in range(frame_count)]
        rw.rw_obj(self.frame_indices)
        
    def rw_frame_values(self, rw):
        # Generate all offsets
        offsets = set()
        for o in self.anim_curves:
            offsets.update(set(o.frame_values_offset + i*4 for i in range(o.frame_count+1)))
        offsets = sorted(offsets)
        first_offset = offsets[0]
        
        # Read the individual frame values
        rw.assert_local_file_pointer_now_at("Frame Values", first_offset)
        frame_count = len(offsets)
        if rw.mode() == "read":
            self.frame_values.data = [None for _ in range(frame_count)]
        rw.rw_obj(self.frame_values)


class AnimationCurve(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.frame_count          = None
        self.frame_indices_offset = None
        self.frame_values_offset  = None
        
    def __repr__(self):
        return f"[KFMI::Data1] {self.frame_count} {self.frame_indices_offset} {self.frame_values_offset}"
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        self.frame_count          = rw.rw_uint32(self.frame_count)
        self.frame_indices_offset = rw.rw_pointer(self.frame_indices_offset)
        self.frame_values_offset  = rw.rw_pointer(self.frame_values_offset)
        rw.align(rw.local_tell(), 0x10)
