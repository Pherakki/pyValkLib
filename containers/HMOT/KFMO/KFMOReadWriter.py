from pyValkLib.serialisation.ValkSerializable import Serializable, ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray, PointerIndexableArrayFloat32, PointerIndexableArrayPointer
from pyValkLib.serialisation.BufferViewArray import BufferViewArray

from .SceneNode import SceneNode
from .FCurveDef import FCurveDef
from .SceneNodeFCurves import SceneNodeFCurves
from .SceneNodeTransform import SceneNodeTransform
from pyValkLib.containers.Metadata.POF0.POF0ReadWriter import POF0ReadWriter
from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

from pyValkLib.containers.Metadata.POF0.POF0Compression import POF0Validator
from pyValkLib.containers.Metadata.ENRS.ENRSCompression import ENRSValidator


class KFMOReadWriter(ValkSerializable32BH):
    FILETYPE = "KFMO"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.flags = 0x18000000
        self.POF0 = POF0ReadWriter("<")
        self.ENRS = ENRSReadWriter("<")
        self.EOFC = EOFCReadWriter("<")
        
        self.contents              = Contents(self.context)    
        self.scene_node_flags      = []
        self.scene_nodes           = PointerIndexableArray(self.context)
        self.fcurve_defs           = PointerIndexableArray(self.context)
        self.unknown_bytes         = PointerIndexableArray(self.context)
        self.fcurve_offsets        = PointerIndexableArrayPointer(self.context)
        self.scene_node_transforms = PointerIndexableArrayFloat32(self.context)
        self.frame_data            = PointerIndexableArray(self.context)

    def get_subcontainers(self):
        return [self.POF0, self.ENRS, self.EOFC,
                ENRSValidator(self),
                POF0Validator(self)]
    
    def read_write_contents(self, rw):
        print("##################")
        print("#### NEW KFMO ####")
        print("##################")
        rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))
        
        rw.mark_new_contents_array()
        self.contents = rw.rw_obj(self.contents)
        print(self.contents)
        self.rw_scene_node_flags(rw)
        self.rw_scene_nodes(rw)
        self.rw_fcurve_defs(rw)
        self.rw_unknown_bytes(rw)
        self.rw_fcurve_offsets(rw)
        self.rw_scene_node_transforms(rw)
        self.rw_scene_node_fcurve_data(rw)
        rw.mark_new_contents_array()
        

    def rw_scene_node_flags(self, rw):
        rw.mark_new_contents_array()
        if self.contents.scene_node_flags_offset:
            rw.assert_local_file_pointer_now_at("Scene Node Flags", self.contents.scene_node_flags_offset)
            self.scene_node_flags = rw.rw_uint16s(self.scene_node_flags, self.contents.scene_node_count)
            print("SN Flags", self.scene_node_flags)
            rw.align(rw.local_tell(), 0x10)
            
    def rw_scene_nodes(self, rw):
        if self.contents.scene_nodes_offset:
            rw.assert_local_file_pointer_now_at("Scene Nodes", self.contents.scene_nodes_offset)
            if rw.mode() == "read":
                self.scene_nodes.data = [SceneNode(self.context) for _ in range(self.contents.scene_node_count)]
            rw.rw_obj(self.scene_nodes)
            print(self.scene_nodes)

    def rw_fcurve_defs(self, rw):
        if rw.mode() == "read":
            fcurve_count = (self.contents.fcurve_offsets_offset - rw.local_tell()) // 0x10
            self.fcurve_defs.data = [FCurveDef(self.context) for _ in range(fcurve_count)]
        rw.rw_obj(self.fcurve_defs)
        print(self.fcurve_defs)
        
    def rw_unknown_bytes(self, rw):
        if self.contents.fcurve_offsets_offset:
            rw.assert_local_file_pointer_now_at("Unknown Blob", self.contents.fcurve_offsets_offset)
            rw.mark_new_contents_array()
            if rw.mode() == "read":
                self.unknown_bytes.data = [UnknownSection(self.context) for _ in range(self.contents.unknown_0x08)]
            rw.rw_obj(self.unknown_bytes)
            print(self.unknown_bytes)
        
    def rw_fcurve_offsets(self, rw):
        offsets = sorted(set(sn.animation_offset + 4*i
                            for sn in self.scene_nodes 
                            for i in range(sn.get_count())
                            if sn.animation_offset > 0))
        
        if len(offsets):
            rw.assert_local_file_pointer_now_at("FCurve Offsets", offsets[0])
            rw.mark_new_contents_array()
            if rw.mode() == "read":
                self.fcurve_offsets.data = [None for _ in range(len(offsets))]
            self.fcurve_offsets = rw.rw_obj(self.fcurve_offsets)
            print(self.fcurve_offsets)

    def rw_scene_node_transforms(self, rw):
        offsets = sorted(set(sn.transform_offset + 4*i
                            for sn in self.scene_nodes 
                            for i in range(sn.get_count())
                            if sn.transform_offset > 0))
        
        if len(offsets):
            rw.assert_local_file_pointer_now_at("Scene Node Transforms", offsets[0])
            if rw.mode() == "read":
                self.scene_node_transforms.data = [None for _ in range(len(offsets))]
            self.scene_node_transforms = rw.rw_obj(self.scene_node_transforms)
            
        
    def rw_scene_node_fcurve_data(self, rw):
        if len(self.fcurve_defs):
            # Init loop
            sorted_fcurves = sorted(self.fcurve_defs, key=lambda x: x.offset)
            buffer_pos    = 0
            buffer_offset = 0
            working_type  = sorted_fcurves[0].type
            working_div   = sorted_fcurves[0].divisor
            if working_type == 1:
                working_size = 4
            elif working_type == 2:
                working_size = 2
            elif working_type == 3:
                working_size = 1
            else:
                raise NotImplementedError(f"FCurve Data Type '{working_type}' not known.")
            
            # R/W Data
            rw.mark_new_contents_array()
            offsets = set()
            for fcurve in sorted_fcurves:
                if not(fcurve.type == working_type):
                    offsets = sorted(offsets)
                    rw.assert_local_file_pointer_now_at("FCurve Frame Data", offsets[0])
                    buffer_pos, buffer_offset = self.rw_framedata_block(rw, fcurve, working_type, working_div, working_size, buffer_pos, buffer_offset, offsets)
                    
                    if fcurve.type != working_type:
                        rw.mark_new_contents_array()
                        rw.align(rw.local_tell(), 0x04)
                        
                    working_type = fcurve.type
                    working_div = fcurve.divisor
                    if working_type == 1:
                        working_size = 4
                    elif working_type == 2:
                        working_size = 2
                    elif working_type == 3:
                        working_size = 1
                    else:
                        raise NotImplementedError(f"FCurve Data Type '{working_type}' not known.")
    
                    offsets = set()
                    
                fcount = int(self.contents.frame_count) + 1
                offsets.update(fcurve.offset + working_size*i for i in range(fcount))
                    
            if len(offsets):
                offsets = sorted(offsets)
                rw.assert_local_file_pointer_now_at("FCurve Frame Data", offsets[0])
                self.rw_framedata_block(rw, fcurve, working_type, working_div, working_size, buffer_pos, buffer_offset, offsets)
            
        rw.align(rw.local_tell(), 0x10)
            
    def rw_framedata_block(self, rw, fcurve, working_type, working_div, working_size, buffer_pos, buffer_offset, offsets):
            count = len(offsets)
            if rw.mode() == "read":
                self.frame_data.data.extend(None for _ in range(count))
            
            op = fcurve.get_framedata_rw(rw, working_type, working_div)
            self.frame_data.data[buffer_pos:buffer_pos+count] = list(op(self.frame_data.data[buffer_pos:buffer_pos+count], count))
            for i in range(count):
                self.frame_data.ptr_to_idx[buffer_offset] = buffer_pos
                self.frame_data.idx_to_ptr[buffer_pos]    = buffer_offset
                buffer_offset += working_size
                buffer_pos += 1
                
            return buffer_pos, buffer_offset

    def __repr__(self):
        return f"KFMO Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains {', '.join(c.FILETYPE for c in self.get_subcontainers())}"

class Contents(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.flags                   = None
        self.scene_node_count        = None
        self.unknown_0x08            = None
        self.unknown_0x0C            = None
        self.frame_count             = None
        self.framerate               = None
        self.unknown_0x18            = None
        self.scene_nodes_offset      = None
        self.scene_node_flags_offset = None
        self.fcurve_offsets_offset   = None
        self.unknown_0x38  = None
        self.unknown_0x3C  = None
        
    def __repr__(self):
        return f"[KFMO::Contents] " \
            f"{self.flags if self.flags is None else hex(self.flags)} "\
            f"{self.scene_node_count} {self.unknown_0x08} {self.unknown_0x0C} " \
            f"{self.frame_count} {self.framerate} {self.unknown_0x18} {self.scene_nodes_offset} " \
            f"{self.scene_node_flags_offset} {self.fcurve_offsets_offset}"
        
    def read_write(self, rw):
        self.flags                   = rw.rw_uint32(self.flags)
        self.scene_node_count        = rw.rw_uint32(self.scene_node_count)
        self.unknown_0x08            = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C            = rw.rw_uint32(self.unknown_0x0C)
        
        self.frame_count             = rw.rw_float32(self.frame_count)
        self.framerate               = rw.rw_float32(self.framerate)
        self.unknown_0x18            = rw.rw_float32(self.unknown_0x18)
        self.scene_nodes_offset      = rw.rw_pointer(self.scene_nodes_offset)
        
        self.scene_node_flags_offset = rw.rw_pointer(self.scene_node_flags_offset)
        self.fcurve_offsets_offset   = rw.rw_pointer(self.fcurve_offsets_offset)
        self.unknown_0x38            = rw.rw_uint32(self.unknown_0x38)
        self.unknown_0x3C            = rw.rw_uint32(self.unknown_0x3C)
        rw.align(rw.local_tell(), 0x60)
        
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)

class UnknownSection(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.count = None
        self.data  = None
        
    def __repr__(self):
        return f"[KFMO::UnknownSection] {self.count} {self.data}"
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        self.count  = rw.rw_uint16(self.count)
        self.data   = rw.rw_bytestring(self.data, 14)