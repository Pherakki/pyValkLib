from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray, PointerIndexableArrayFloat32

from .StructureNode import StructureNode
from .FCurve import FCurve
from .StructureNodeFCurves import StructureNodeFCurves
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
        
        self.flags = None
        self.structure_node_count = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        self.unknown_0x10 = None
        self.unknown_0x14 = None
        self.unknown_0x18 = None
        self.structure_nodes_offset = None
        self.structure_node_flags_offset = None
        self.unknown_offset_3 = None
        
        self.structure_node_flags   = []
        self.structure_nodes        = PointerIndexableArray(self.context)
        self.fcurves                = PointerIndexableArray(self.context)
        self.unknown_bstring        = b''
        self.structure_node_fcurves = PointerIndexableArray(self.context)
        self.unknown_float_buffer   = PointerIndexableArrayFloat32(self.context)

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
        self.rw_unknown_float_buffer(rw)
        self.rw_animation_frame_data(rw)
        rw.mark_new_contents_array()
        
    def rw_fileinfo(self, rw):
        self.flags                       = rw.rw_uint32(self.flags)
        self.structure_node_count        = rw.rw_uint32(self.structure_node_count)
        self.unknown_0x08                = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C                = rw.rw_uint32(self.unknown_0x0C)
        self.frame_count                 = rw.rw_float32(self.unknown_0x10)
        self.frames_per_second           = rw.rw_float32(self.unknown_0x14)
        self.unknown_0x18                = rw.rw_float32(self.unknown_0x18)
        self.structure_nodes_offset      = rw.rw_pointer(self.structure_nodes_offset)
        self.structure_node_flags_offset = rw.rw_pointer(self.structure_node_flags_offset)
        self.unknown_offset_3            = rw.rw_pointer(self.unknown_offset_3)
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
            fcurve_count = (self.unknown_offset_3 - rw.local_tell()) // 0x10
            self.fcurves.data = [FCurve(self.context) for _ in range(fcurve_count)]
        rw.rw_obj(self.fcurves)
        
    def rw_structure_node_fcurves(self, rw):
        # Make these members of the structure nodes
        # Something isn't right here. It seems like the flags dictate which channels are active...
        # but this doesn't always lead to the correct numbers of fcurves being identified.
        # In fact, it often overruns.
        if self.unknown_offset_3:
            rw.assert_local_file_pointer_now_at("Structure Node FCurves", self.unknown_offset_3)
            self.unknown_bstring = rw.rw_bytestring(self.unknown_bstring, 0x10) # Not present in all files...
            if rw.mode() == "read":
                self.structure_node_fcurves.data = [StructureNodeFCurves(self.context, sn.flags) 
                                                    for sn in self.structure_nodes
                                                    if sn.offset_1 != 0]
            rw.rw_obj(self.structure_node_fcurves)

    def rw_unknown_float_buffer(self, rw):
        # This one feels really strange.
        # Some quats seem to be given the value (0, 0, 0, 0), which is not good.
        # Moreover, parts of the buffer seem to overlap with each other. Perhaps common numbers are
        # allowed to overlap as a form of compression.
        # Very confusing. Leave it as an unknown buffer for now.
        info = sorted(set((sn.offset_2, sn.flags) for sn in self.structure_nodes if sn.offset_2 != 0))
        first_ptr = info[0][0]
        final_ptr = info[-1][0]
        final_count = bin(info[-1][1]).count('1')
        
        rw.assert_local_file_pointer_now_at("Unknown Buffer", first_ptr)
        
        total_elements = (final_ptr - first_ptr + 4*final_count) // 4
        if rw.mode() == "read":
            self.unknown_float_buffer.data = [0 for _ in range(total_elements)]
        rw.rw_obj(self.unknown_float_buffer)
        
        # for idx, ptr in self.unknown_float_buffer.idx_to_ptr.items():
        #     print(">", idx, ptr, self.unknown_float_buffer[idx])
        
    def rw_animation_frame_data(self, rw):
        for fcurve in sorted(self.fcurves, key=lambda x: x.offset):
            print(">>", fcurve.offset)
            rw.assert_local_file_pointer_now_at("FCurve Data", fcurve.offset)
            rw.rw_obj_method(fcurve, fcurve.rw_framedata, int(self.frame_count))
        rw.align(rw.local_tell(), 0x10)
            

    def __repr__(self):
        return f"KFMO Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains {', '.join(c.FILETYPE for c in self.get_subcontainers())}"
