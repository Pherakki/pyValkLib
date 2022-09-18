from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray, PointerIndexableArrayFloat32
from pyValkLib.serialisation.BufferViewArray import BufferViewArray

from .StructureNode import StructureNode
from .FCurve import FCurve
from .StructureNodeFCurves import StructureNodeFCurves
from .StructureNodeTransform import StructureNodeTransform
from pyValkLib.containers.Metadata.POF0.POF0ReadWriter import POF0ReadWriter
from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter


class KFMOReadWriter(ValkSerializable32BH):
    FILETYPE = "KFMO"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.flags = 0x18000000
        self.POF0 = POF0ReadWriter("<")
        self.ENRS = ENRSReadWriter("<")
        self.EOFC = EOFCReadWriter("<")
        
        self.flags                       = None
        self.structure_node_count        = None
        self.unknown_0x08                = None
        self.unknown_0x0C                = None
        self.frame_count                 = None
        self.frames_per_second           = None
        self.unknown_0x18                = None
        self.structure_nodes_offset      = None
        self.structure_node_flags_offset = None
        self.fcurve_metadata_offset      = None
        
        self.structure_node_flags      = []
        self.structure_nodes           = PointerIndexableArray(self.context)
        self.fcurves                   = PointerIndexableArray(self.context)
        self.unknown_bstring           = b''
        self.structure_node_fcurves    = BufferViewArray(self.context, StructureNodeFCurves)
        self.structure_node_transforms = BufferViewArray(self.context, StructureNodeTransform)

    def get_subcontainers(self):
        return [self.POF0, self.ENRS, self.EOFC]
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))
        
        rw.mark_new_contents_array()
        self.rw_fileinfo(rw)
        self.rw_structure_node_flags(rw)
        self.rw_structure_nodes(rw)
        self.rw_fcurve_metadata(rw)
        self.rw_structure_node_fcurves(rw)
        self.rw_structure_node_static_transforms(rw)
        self.rw_structure_node_anim_transforms(rw)
        rw.mark_new_contents_array()
        
    def rw_fileinfo(self, rw):
        self.flags                       = rw.rw_uint32(self.flags)
        self.structure_node_count        = rw.rw_uint32(self.structure_node_count)
        self.unknown_0x08                = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C                = rw.rw_uint32(self.unknown_0x0C)
        self.frame_count                 = rw.rw_float32(self.frame_count)
        self.frames_per_second           = rw.rw_float32(self.frames_per_second)
        self.unknown_0x18                = rw.rw_float32(self.unknown_0x18)
        self.structure_nodes_offset      = rw.rw_pointer(self.structure_nodes_offset)
        self.structure_node_flags_offset = rw.rw_pointer(self.structure_node_flags_offset)
        self.fcurve_metadata_offset      = rw.rw_pointer(self.fcurve_metadata_offset)
        rw.align(rw.local_tell(), 0x60)
        
    def rw_structure_node_flags(self, rw):
        rw.mark_new_contents_array()
        if self.structure_node_flags_offset:
            rw.assert_local_file_pointer_now_at("Structure Node Flags", self.structure_node_flags_offset)
            self.structure_node_flags = rw.rw_uint16s(self.structure_node_flags, self.structure_node_count)
            rw.align(rw.local_tell(), 0x10)
            
    def rw_structure_nodes(self, rw):
        if self.structure_nodes_offset:
            rw.assert_local_file_pointer_now_at("Structure Nodes", self.structure_nodes_offset)
            if rw.mode() == "read":
                self.structure_nodes.data = [StructureNode(self.context) for _ in range(self.structure_node_count)]
            rw.rw_obj(self.structure_nodes)

    def rw_fcurve_metadata(self, rw):
        if rw.mode() == "read":
            fcurve_count = (self.fcurve_metadata_offset - rw.local_tell()) // 0x10
            self.fcurves.data = [FCurve(self.context) for _ in range(fcurve_count)]
        rw.rw_obj(self.fcurves)
        
    def rw_structure_node_fcurves(self, rw):
        if self.fcurve_metadata_offset:
            rw.assert_local_file_pointer_now_at("Structure Node FCurves", self.fcurve_metadata_offset)
            self.unknown_bstring = rw.rw_bytestring(self.unknown_bstring, 0x10) # Not present in all files...

            info = sorted(set((sn.animation_offset, sn.flags) for sn in self.structure_nodes if sn.animation_offset > 0))
            offsets = [s[0] for s in info]
            flags = [s[1] for s in info]
            flag_bitcount = bin(flags[-1]).count('1')
            buffer_size = (offsets[-1] - offsets[0] + 4*flag_bitcount) // 4
            
            self.structure_node_fcurves = rw.rw_obj(self.structure_node_fcurves,
                                                    buffer_size, offsets, zip(flags))
            

    def rw_structure_node_static_transforms(self, rw):
        info = sorted(set((sn.transform_offset, sn.flags) for sn in self.structure_nodes if sn.transform_offset != 0))
        offsets = [s[0] for s in info]
        flags = [s[1] for s in info]
        flag_bitcount = bin(flags[-1]).count('1')
        buffer_size = (offsets[-1] - offsets[0] + 4*flag_bitcount) // 4
        
        rw.assert_local_file_pointer_now_at("Structure Node Transforms", offsets[0])
        
        self.structure_node_transforms = rw.rw_obj(self.structure_node_transforms,
                                                   buffer_size, offsets, zip(flags))
        
    def rw_structure_node_anim_transforms(self, rw):
        for fcurve in sorted(self.fcurves, key=lambda x: x.offset):
            rw.local_seek(fcurve.offset)
            rw.assert_local_file_pointer_now_at("FCurve Data", fcurve.offset)
            rw.rw_obj_method(fcurve, fcurve.rw_framedata, int(self.frame_count))
        rw.align(rw.local_tell(), 0x10)
            

    def __repr__(self):
        return f"KFMO Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains {', '.join(c.FILETYPE for c in self.get_subcontainers())}"
