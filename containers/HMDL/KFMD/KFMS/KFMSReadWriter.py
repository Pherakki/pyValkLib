from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray, PointerIndexableArrayMatrix4x4

from pyValkLib.containers.Metadata.POF0.POF0ReadWriter import POF0ReadWriter
from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.CCRS.CCRSReadWriter import CCRSReadWriter
from pyValkLib.containers.Metadata.MTXS.MTXSReadWriter import MTXSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

from pyValkLib.containers.Metadata.POF0.POF0Compression import POF0Validator
from pyValkLib.containers.Metadata.ENRS.ENRSCompression import ENRSValidator
from pyValkLib.containers.Metadata.CCRS.CCRSCompression import CCRSValidator
from pyValkLib.containers.Metadata.MTXS.MTXSCompression import MTXSValidator

from .SceneNode import SceneNodeBinary
from .MeshDefinition import MeshDefinitionBinary
from .BoundingBox import BoundingBoxBinary
from .Skeleton import SkeletonBinary
from .Bone import BoneBinary
from .MeshGroup import MeshGroupBinary
from .Material import MaterialBinary
from .Mesh import MeshBinary
from .VertexGroup import VertexGroup
from .Texture import TextureBinary
from .UnknownIndices import UnknownIndicesBinary
from .UnknownObject import UnknownObject

class KFMSReadWriter(ValkSerializable32BH):
    FILETYPE = "KFMS"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.flags = 0x18000000
        self.POF0 = POF0ReadWriter("<")
        self.ENRS = ENRSReadWriter("<")
        self.CCRS = CCRSReadWriter("<")
        self.MTXS = MTXSReadWriter("<")
        self.EOFC = EOFCReadWriter("<")
        
        
        self.flags                        = None
        self.scene_node_count             = None
        self.bone_count                   = None
        self.unknown_0x0C                 = 0
        
        self.model_height                 = None
        self.scene_nodes_offset           = None
        self.scene_node_flags_offset      = None
        self.scene_node_transforms_offset = None
        
        self.material_count               = None
        self.materials_offset             = None
        self.mesh_group_count             = None
        self.mesh_groups_offset           = None
        
        self.mesh_count                   = None
        self.meshes_offset                = None
        self.unknown_obj_count            = None
        self.unknown_objs_offset          = None
        
        self.texture_count                = None
        self.textures_offset              = None
        self.unknown_count_1              = None
        self.unknown_count_2              = None
        self.unknown_count_3              = None
        self.unknown_count_4              = None
        
        self.unknown_offset_1             = None
        self.unknown_offset_2             = None
        self.unknown_offset_3             = None
        self.mesh_defs_count              = None
        
        self.mesh_defs_offset             = None
        self.unknown_0x64                 = None
        self.unknown_indices_offset       = None
        self.unknown_0x6C                 = None
        
        self.unknown_0x70                 = None
        self.unknown_0x74                 = None
        self.unknown_0x78                 = 0
        self.unknown_0x7C                 = 0
        
        self.unknown_0x80                 = None
        self.unknown_0x84                 = 0
        self.unknown_0x88                 = 0
        self.unknown_0x8C                 = 0
        
        self.fileinfo_pads                = [0]*0x1F
        
        #
        self.scene_node_flags      = []
        self.scene_nodes           = PointerIndexableArray(self.context)
        self.scene_node_transforms = []
        self.unknown_chunk_1       = []
        self.unknown_chunk_2       = []
        self.unknown_chunk_3       = []
        self.mesh_definitions      = PointerIndexableArray(self.context)
        self.bounding_boxes        = PointerIndexableArray(self.context)
        self.skeletons             = PointerIndexableArray(self.context)
        self.bones                 = PointerIndexableArray(self.context)
        self.bone_ibpms            = PointerIndexableArrayMatrix4x4(self.context)
        self.mesh_groups           = PointerIndexableArray(self.context)
        self.materials             = PointerIndexableArray(self.context)
        self.meshes                = PointerIndexableArray(self.context)
        self.vertex_groups         = PointerIndexableArray(self.context)
        self.textures              = PointerIndexableArray(self.context)
        self.unknown_indices       = UnknownIndicesBinary(self.context)
        self.unknown_objects       = PointerIndexableArray(self.context)

    def get_subcontainers(self):
        return [
            self.POF0, self.ENRS, self.CCRS, self.MTXS, self.EOFC,
            #ENRSValidator(self),
            POF0Validator(self),
            CCRSValidator(self),
            MTXSValidator(self)
        ]
    
    def read_write_contents(self, rw):
        self.rw_fileinfo(rw)
        self.rw_scene_node_flags(rw)
        self.rw_scene_nodes(rw)
        self.rw_scene_node_transforms(rw)
        self.rw_unknown_chunk_1(rw)
        self.rw_unknown_chunk_2(rw)
        self.rw_unknown_chunk_3(rw)
        self.rw_mesh_definitions(rw)
        self.rw_bounding_boxes(rw)
        self.rw_skeletons(rw)
        self.rw_bones(rw)
        self.rw_bone_ibpms(rw)
        self.rw_mesh_groups(rw)
        self.rw_materials(rw)
        self.rw_meshes(rw)
        self.rw_vertex_groups(rw)
        self.rw_textures(rw)
        self.rw_unknown_indices(rw)
        self.rw_unknown_objects(rw)
        rw.mark_new_contents_array()
        

    def rw_fileinfo(self, rw):
        rw.mark_new_contents_array()
        
        self.flags                        = rw.rw_int32(self.flags)
        is_big_endian = self.flags & 1 == 1
        self.context.endianness = '>' if is_big_endian else '<'
        self.unknown_indices.context.endianness = self.context.endianness
        
        if self.header.data_length and is_big_endian:
            rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))
        else:
            rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))

        
        self.scene_node_count             = rw.rw_int32(self.scene_node_count)
        self.bone_count                   = rw.rw_int32(self.bone_count)
        self.unknown_0x0C                 = rw.rw_int32(self.unknown_0x0C)
        
        self.model_height                 = rw.rw_float32(self.model_height)
        self.scene_nodes_offset           = rw.rw_pointer(self.scene_nodes_offset)
        self.scene_node_flags_offset      = rw.rw_pointer(self.scene_node_flags_offset)
        self.scene_node_transforms_offset = rw.rw_pointer(self.scene_node_transforms_offset)
        
        self.material_count               = rw.rw_int32(self.material_count)
        self.materials_offset             = rw.rw_pointer(self.materials_offset)
        self.mesh_group_count             = rw.rw_int32(self.mesh_group_count)
        self.mesh_groups_offset           = rw.rw_pointer(self.mesh_groups_offset)
        
        self.mesh_count                   = rw.rw_int32(self.mesh_count)
        self.meshes_offset                = rw.rw_pointer(self.meshes_offset)
        self.unknown_obj_count            = rw.rw_int32(self.unknown_obj_count)
        self.unknown_objs_offset          = rw.rw_pointer(self.unknown_objs_offset)
        
        self.texture_count                = rw.rw_int32(self.texture_count)
        self.textures_offset              = rw.rw_pointer(self.textures_offset)
        self.unknown_count_1              = rw.rw_int16(self.unknown_count_1)
        self.unknown_count_2              = rw.rw_int16(self.unknown_count_2)
        self.unknown_count_3              = rw.rw_int16(self.unknown_count_3)
        self.unknown_count_4              = rw.rw_int16(self.unknown_count_4)
        
        self.unknown_offset_1             = rw.rw_pointer(self.unknown_offset_1)
        self.unknown_offset_2             = rw.rw_pointer(self.unknown_offset_2)
        self.unknown_offset_3             = rw.rw_pointer(self.unknown_offset_3)
        self.mesh_defs_count              = rw.rw_int32(self.mesh_defs_count)
        
        self.mesh_defs_offset             = rw.rw_pointer(self.mesh_defs_offset)
        self.unknown_0x64                 = rw.rw_int32(self.unknown_0x64)
        self.unknown_indices_offset       = rw.rw_pointer(self.unknown_indices_offset)
        self.unknown_0x6C                 = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70                 = rw.rw_int32(self.unknown_0x70)
        self.unknown_0x74                 = rw.rw_int32(self.unknown_0x74)
        self.unknown_0x78                 = rw.rw_pad32(self.unknown_0x78)
        self.unknown_0x7C                 = rw.rw_pad32(self.unknown_0x7C)

        self.unknown_0x80                 = rw.rw_uint32(self.unknown_0x80) # This one sometimes has no ENRS
        self.fileinfo_pads                = rw.rw_pad32s(self.fileinfo_pads, 0x1F)
        
        rw.assert_equal(list(self.fileinfo_pads), [0]*0x1F)
        
    def rw_scene_node_flags(self, rw):
        rw.mark_new_contents_array()
        
        if self.scene_node_flags_offset:
            rw.assert_local_file_pointer_now_at("Scene Node Flags", self.scene_node_flags_offset)
            self.scene_node_flags = rw.rw_uint16s(self.scene_node_flags, self.scene_node_count)
            rw.align(rw.local_tell(), 0x10)
        
    def rw_scene_nodes(self, rw):
        if self.scene_nodes_offset:
            rw.assert_local_file_pointer_now_at("Scene Nodes", self.scene_nodes_offset)
            if rw.mode() == "read":
                self.scene_nodes.data = [SceneNodeBinary(self.context) for _ in range(self.scene_node_count)]
            rw.rw_obj(self.scene_nodes)
        
    def rw_scene_node_transforms(self, rw):
        rw.mark_new_contents_array()
        
        # This looks like pos, XYZW Quat, Scale
        if self.scene_node_transforms_offset:
            rw.assert_local_file_pointer_now_at("Scene Node Transform List", self.scene_node_transforms_offset)
            self.scene_node_transforms = rw.rw_float32s(self.scene_node_transforms, (self.scene_node_count, 12))
        
    def rw_unknown_chunk_1(self, rw):
        rw.mark_new_contents_array()
        if self.unknown_offset_1:
            rw.assert_local_file_pointer_now_at("Unknown Chunk 1", self.unknown_offset_1)
            self.unknown_chunk_1 = rw.rw_uint16s(self.unknown_chunk_1, self.unknown_count_1)
            
    def rw_unknown_chunk_2(self, rw):
        rw.mark_new_contents_array()
        if self.unknown_offset_2:
            rw.assert_local_file_pointer_now_at("Unknown Chunk 2", self.unknown_offset_2)
            self.unknown_chunk_2 = rw.rw_uint16s(self.unknown_chunk_2, self.unknown_count_2)
            
    def rw_unknown_chunk_3(self, rw):
        rw.mark_new_contents_array()
        if self.unknown_offset_3:
            rw.assert_local_file_pointer_now_at("Unknown Chunk 3", self.unknown_offset_3)
            self.unknown_chunk_3 = rw.rw_uint16s(self.unknown_chunk_3, self.unknown_count_3)
        rw.align(rw.local_tell(), 0x10)
        
    def rw_mesh_definitions(self, rw):
        if self.mesh_defs_offset:
            rw.assert_local_file_pointer_now_at("Mesh Definitions", self.mesh_defs_offset)
            if rw.mode() == "read":
                self.mesh_definitions.data = [MeshDefinitionBinary(self.context) for _ in range(self.mesh_defs_count)]
            rw.rw_obj(self.mesh_definitions)
        
    def rw_bounding_boxes(self, rw):
        info = sorted(set([(bm.bounding_box_offset, bm.bounding_box_vertex_count) for bm in self.scene_nodes if bm.bounding_box_offset != 0]))
        if rw.mode() == "read":
            self.bounding_boxes.data = [BoundingBoxBinary(count, self.context) for offset, count in info]
        if len(info):
            first_offset = info[0][0]
            rw.assert_local_file_pointer_now_at("Bounding Boxes", first_offset)
            rw.rw_obj(self.bounding_boxes)
        
    def rw_skeletons(self, rw):
        info = sorted(set([(sn.skeletons_offset, sn.skeleton_count) for sn in self.scene_nodes if sn.skeletons_offset != 0]))
        if rw.mode() == "read":
            self.skeletons.data = [SkeletonBinary(count, self.context) for offset, count in info]
        if len(info):
            first_offset = info[0][0]
            rw.assert_local_file_pointer_now_at("Skeletons", first_offset)
            rw.rw_obj(self.skeletons)
            rw.align(rw.local_tell(), 0x10)
    
    def rw_bones(self, rw):
        if rw.mode() == "read":
            self.bones.data = [BoneBinary(self.context) for _ in range(self.bone_count)]
        rw.rw_obj(self.bones)
        rw.align(rw.local_tell(), 0x10)
    
    def rw_bone_ibpms(self, rw):
        rw.mark_new_contents_array()
        
        ptrs = sorted(set([bone.ibpm_offset for bone in self.bones if bone.ibpm_offset != 0]))
        if len(ptrs):
            rw.assert_local_file_pointer_now_at("IBPMs", ptrs[0])
            if rw.mode() == "read":
                self.bone_ibpms.data = [None for _ in ptrs]
            rw.rw_obj(self.bone_ibpms)
        
    def rw_mesh_groups(self, rw):
        if self.mesh_groups_offset:
            rw.assert_local_file_pointer_now_at("Mesh Groups", self.mesh_groups_offset)
            if rw.mode() == "read":
                self.mesh_groups.data = [MeshGroupBinary(self.context) for _ in range(self.mesh_group_count)]
            rw.rw_obj(self.mesh_groups)
        
    def rw_materials(self, rw):
        if self.materials_offset:
            rw.assert_local_file_pointer_now_at("Materials", self.materials_offset)
            if rw.mode() == "read":
                self.materials.data = [MaterialBinary(self.context) for _ in range(self.material_count)]
            rw.rw_obj(self.materials)
            
    def rw_meshes(self, rw):
        if self.meshes_offset:
            rw.assert_local_file_pointer_now_at("Meshes", self.meshes_offset)
            if rw.mode() == "read":
                self.meshes.data = [MeshBinary(self.context) for _ in range(self.mesh_count)]
            rw.rw_obj(self.meshes)
        
    def rw_vertex_groups(self, rw):
        info = sorted(set([(mesh.vertex_groups_offset, mesh.vertex_group_count) for mesh in self.meshes if mesh.vertex_groups_offset != 0]))
        if len(info):
            if rw.mode() == "read":
                self.vertex_groups.data = [VertexGroup(self.context) for _ in range(sum(vg[1] for vg in info))]
            rw.rw_obj(self.vertex_groups)
            rw.align(rw.local_tell(), 0x10)
        
    def rw_textures(self, rw):
        if self.textures_offset:
            rw.assert_local_file_pointer_now_at("Textures", self.textures_offset)
            if rw.mode() == "read":
                self.textures.data = [TextureBinary(self.context) for _ in range(self.texture_count)]
            rw.rw_obj(self.textures)

    def rw_unknown_indices(self, rw):
        # There's probably a setting somewhere that tells the HMDL to skip
        # these indices
        # All others try to read it and find a 0 count and 0 offset - hence the 
        # 0x10 row of blanks found in many HMDLs?
        if self.unknown_indices_offset:
            rw.assert_local_file_pointer_now_at("Unknown Indices", self.unknown_indices_offset)
            rw.rw_obj(self.unknown_indices)
        else: # Works for all MLXs, but not for HMDLs - see dummy_grass.hmd
            rw.align(0x10, 0x20)

            
    def rw_unknown_objects(self, rw):
        if self.unknown_objs_offset:
            rw.assert_local_file_pointer_now_at("Unknown Objects", self.unknown_objs_offset)
            if rw.mode() == "read":
                self.unknown_objects.data = [UnknownObject(self.context) for _ in range(self.unknown_obj_count)]
            rw.rw_obj(self.unknown_objects)
            
    def __repr__(self):
        return f"KFMS Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains {', '.join(c.FILETYPE for c in self.get_subcontainers())}."
