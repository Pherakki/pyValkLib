from .HMDLReadWriter import HMDLReadWriter
from .KFMD.KFMDReadWriter import KFMDReadWriter
from .KFMD.KFMS.SceneNode import SceneNodeBinary
from .KFMD.KFMS.MeshDefinition import MeshDefinitionBinary
from .KFMD.KFMS.Skeleton import SkeletonBinary
from .KFMD.KFMS.Bone import BoneBinary
from .KFMD.KFMS.BoundingBox import BoundingBoxBinary
from .KFMD.KFMS.MeshGroup import MeshGroupBinary
from .KFMD.KFMS.Mesh import MeshBinary
from .KFMD.KFMS.Material import MaterialBinary
from .KFMD.KFMS.Texture import TextureBinary
from .KFMD.KFMS.UnknownIndices import UnknownIndicesBinary, UnknownIndexGroupBinary

from pyValkLib.serialisation.ReadWriter import OffsetTracker
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray


class KFMDInterface:
    def __init__(self):
        # Replace a SceneNode tree with an Armature where appropriate?
        # Can SceneNodes be mixed with Bones?
        # Meshes can be placed as leaf nodes of bones...
        self.flags           = None
        self.unknown_count_4 = None
        self.unknown_0x64    = None
        self.unknown_0x70    = None
        self.unknown_0x74    = None
        self.unknown_0x80    = None
        self.model_height    = None
    
        self.scene_node_flags = []
        self.scene_nodes     = []
        self.scene_node_transforms = []
        self.unknown_1s      = []
        self.unknown_2s      = []
        self.unknown_3s      = []
        self.mesh_defs       = []
        self.bounding_boxes  = [] # Should be calculable
        self.skeletons       = []
        self.bones           = []
        self.ibpms           = [] # Calculable, but not byte-exact to originals, so leave for now
        self.mesh_groups     = []
        self.materials       = []
        self.meshes          = []
        self.vertex_groups   = [] # Should be calculable
        self.textures        = []
        self.unknown_indices = None
        self.unknown_objects = []

    @classmethod
    def from_binary(cls, KFMD_binary):
        binary = KFMD_binary.KFMS
        
        # Unpack KFMG into verts / indices?
        instance = cls()
        instance.flags = binary.flags
        instance.unknown_count_4 = binary.unknown_count_4
        instance.unknown_0x64 = binary.unknown_0x64
        instance.unknown_0x6C = binary.unknown_0x6C
        instance.unknown_0x70 = binary.unknown_0x70
        instance.unknown_0x74 = binary.unknown_0x74
        instance.unknown_0x80 = binary.unknown_0x80
        
        # Calculable header variables
        instance.model_height    = binary.model_height

        # Contents
        instance.scene_nodes = [SceneNodeInterface.from_binary(sno, flag, transform, binary.scene_nodes, binary.mesh_groups, binary.skeletons, binary.bones, binary.bounding_boxes)
                                for flag, sno, transform in zip(binary.scene_node_flags, binary.scene_nodes, binary.scene_node_transforms)]
        instance.unknown_1s      = binary.unknown_chunk_1
        instance.unknown_2s      = binary.unknown_chunk_2
        instance.unknown_3s      = binary.unknown_chunk_3
        instance.mesh_defs       = binary.mesh_definitions
        instance.bounding_boxes  = binary.bounding_boxes
        instance.skeletons       = binary.skeletons
        instance.bones           = [BoneInterface.from_binary(bn, binary.bone_ibpms) for bn in binary.bones]
        instance.ibpms           = binary.bone_ibpms
        instance.mesh_groups     = [MeshGroupInterface.from_binary(mg, binary.meshes, binary.materials) for mg in binary.mesh_groups]
        instance.materials       = binary.materials
        instance.meshes          = binary.meshes
        instance.vertex_groups   = binary.vertex_groups
        instance.textures        = binary.textures
        instance.unknown_indices = UnknownIndicesInterface.from_binary(binary.unknown_indices)
        instance.unknown_objects = binary.unknown_objects
        


        # instance.skeletons  = [SkeletonInterface.from_binary(skel) for skel in binary.skeletons]
        # instance.bounding_boxes = [BoundingBoxInterface.from_binary(bbox) for bbox in binary.bounding_boxes]
        # instance.ibpms      = binary.bone_ibpms
        # instance.meshes     = [MeshInterface.from_binary(mesh, [], [], binary.vertex_groups) for mesh in binary.meshes]
        # instance.materials  = [MaterialInterface.from_binary(mat, binary.textures) for mat in binary.materials]
        # instance.vertex_groups = binary.vertex_groups
        # instance.textures   = [TextureInterface.from_binary(tex) for tex in binary.textures]
        return instance
        
    def to_binary(self, endianness, depth, ENRS, CCRS):
        KFMD_binary = KFMDReadWriter(endianness)
        
        # First dump KFMG
        # Fill me in!
        
        # Dump KFMS
        binary = KFMD_binary.KFMS
        ctx = binary.context

        
        #####################
        # GENERATE CONTENTS #
        #####################
        # Unknown variables
        binary.flags             = self.flags
        binary.unknown_count_4   = self.unknown_count_4
        binary.unknown_0x64      = self.unknown_0x64
        binary.unknown_0x6C      = self.unknown_0x6C
        binary.unknown_0x70      = self.unknown_0x70
        binary.unknown_0x74      = self.unknown_0x74
        binary.unknown_0x80      = self.unknown_0x80
        binary.model_height      = self.model_height

        # Contents
        binary.unknown_chunk_1  = self.unknown_1s
        binary.unknown_chunk_2  = self.unknown_2s
        binary.unknown_chunk_3  = self.unknown_3s
        binary.mesh_definitions = self.mesh_defs
        binary.bounding_boxes   = self.bounding_boxes
        binary.skeletons        = self.skeletons
        binary.bone_ibpms       = self.ibpms
        binary.materials        = self.materials
        binary.meshes           = self.meshes
        binary.vertex_groups    = self.vertex_groups
        binary.textures         = self.textures
        binary.unknown_indices = UnknownIndicesInterface.to_binary(ctx, self.unknown_indices)
        binary.unknown_objects = self.unknown_objects
        
        
        binary.scene_node_count  = len(self.scene_nodes)
        binary.bone_count        = len(self.bones)
        binary.material_count    = len(self.materials)
        binary.mesh_group_count  = len(self.mesh_groups)
        binary.mesh_count        = len(self.meshes)
        binary.unknown_obj_count = len(self.unknown_objects)
        binary.texture_count     = len(self.textures)
        binary.unknown_count_1   = len(self.unknown_1s)
        binary.unknown_count_2   = len(self.unknown_2s)
        binary.unknown_count_3   = len(self.unknown_3s)
        binary.mesh_defs_count   = len(self.mesh_defs)
        
        # # Fill in data
        
        # binary.skeletons.data  = [si.to_binary(ctx) for si in self.skeletons]
        # binary.meshes.data     = [mi.to_binary(ctx) for mi in self.meshes] # Need a PIA constructor that auto-gens pointers...
        # binary.materials.data  = [mi.to_binary(ctx) for mi in self.materials]
        # binary.textures.data   = [ti.to_binary(ctx) for ti in self.textures]
        
        # # Now construct derived objects
        
        
        #####################
        # CALCULATE OFFSETS #
        #####################
        # Start off by calculating header-level offsets
        # This could probably be done automatically with smart function calls
        # in the read_write_contents function of KFMSReadWriter...
        construct_PIA = PointerIndexableArray.from_placeholder_data
        ot = OffsetTracker()
        binary.header.read_write(ot)
        binary.rw_fileinfo(ot)
        
        binary.scene_node_flags_offset = ot.local_tell() if len(self.scene_nodes) else 0
        binary.scene_node_flags = [None]*len(self.scene_nodes)
        binary.rw_scene_node_flags(ot)
        
        binary.scene_nodes_offset = ot.local_tell() if len(self.scene_nodes) else 0
        binary.scene_nodes = construct_PIA(ctx, lambda: SceneNodeBinary(ctx), len(self.scene_nodes), binary.scene_nodes_offset, 0x60)
        binary.rw_scene_nodes(ot)
        
        binary.scene_node_transforms_offset = ot.local_tell() if len(self.scene_nodes) else 0
        binary.scene_node_transforms = [None]*len(self.scene_nodes)*12
        binary.rw_scene_node_transforms(ot)
        
        binary.unknown_offset_1 = ot.local_tell() if len(self.unknown_1s) else 0
        binary.rw_unknown_chunk_1(ot)
        binary.unknown_offset_2 = ot.local_tell() if len(self.unknown_2s) else 0
        binary.rw_unknown_chunk_2(ot)
        binary.unknown_offset_3 = ot.local_tell() if len(self.unknown_3s) else 0
        binary.rw_unknown_chunk_3(ot)
        
        binary.mesh_defs_offset = ot.local_tell() if len(self.mesh_defs) else 0
        binary.rw_mesh_definitions(ot)
        
        # Construct bounding boxes...!
        binary.rw_bounding_boxes(ot)
        binary.rw_skeletons(ot)
        
        binary.bones = construct_PIA(ctx, lambda: BoneBinary(ctx), len(self.bones), ot.local_tell(), 0x08)
        binary.rw_bones(ot)
        binary.rw_bone_ibpms(ot)
        
        binary.mesh_groups_offset = ot.local_tell() if len(self.mesh_groups) else 0
        binary.mesh_groups = construct_PIA(ctx, lambda: MeshGroupBinary(ctx), len(self.mesh_groups), ot.local_tell(), 0x20)
        binary.rw_mesh_groups(ot)
        
        binary.materials_offset = ot.local_tell() if len(self.materials) else 0
        binary.rw_materials(ot)
        
        binary.meshes_offset = ot.local_tell() if len(self.meshes) else 0
        binary.rw_meshes(ot)
        
        # Construct vertex groups...
        binary.rw_vertex_groups(ot)
        
        binary.textures_offset = ot.local_tell() if len(self.textures) else 0
        binary.rw_textures(ot)
        
        binary.unknown_indices_offset = ot.local_tell() if len(self.unknown_indices) else 0
        binary.rw_unknown_indices(ot)
        
        binary.unknown_objs_offset = ot.local_tell() if len(self.unknown_objects) else 0
        binary.rw_unknown_objects(ot)
        
        ##################
        # OBJECT OFFSETS #
        ##################
        # Scene Nodes
        sn_children = [[] for _ in range(len(self.scene_nodes))]
        for i, sni in enumerate(self.scene_nodes):
            if sni.parent_ID > -1:
                sn_children[sni.parent_ID].append(i)
        (
            binary.scene_node_flags,
            binary.scene_nodes.data,
            binary.scene_node_transforms
        ) = zip(*list(sni.to_binary(ctx, i, binary.scene_nodes, binary.mesh_groups, binary.skeletons, binary.bones, binary.bounding_boxes, sn_children) for i, sni in enumerate(self.scene_nodes)))
        
        # Bones
        sn_count = len(self.scene_nodes)
        binary.bones.data = [bone.to_binary(ctx, sn_count + i, binary.bone_ibpms) for i, bone in enumerate(self.bones)]
            
        # Mesh Groups
        binary.mesh_groups.data = [mg.to_binary(ctx, i, binary.meshes, binary.materials) 
                                   for i, mg in enumerate(self.mesh_groups)]


            
        #######################
        # HEADER AND METADATA #
        #######################
        binary.header.data_length = ot.local_tell() - binary.header.header_length
        binary.header.depth = depth + 1
        
        binary.POF0 = binary.POF0.from_obj(binary)
        binary.ENRS = ENRS
        binary.CCRS = CCRS
        binary.MTXS = binary.MTXS.from_obj(binary)
        binary.EOFC.header.depth = binary.header.depth + 1
        ot.rw_obj(binary.POF0)
        ot.rw_obj(binary.ENRS)
        ot.rw_obj(binary.CCRS)
        ot.rw_obj(binary.MTXS)
        ot.rw_obj(binary.EOFC)
        
        binary.header.contents_length = ot.local_tell() - binary.header.header_length
        
        return binary
    
class SceneNodeInterface:
    def __init__(self):
        self.flags_1 = None
        self.flags_2 = None
        self.parent_ID = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        self.unknown_0x44 = None
        self.unknown_0x50 = None
        
        # Attached objects
        self.object_count_1 = None
        self.object_count_2 = None
        self.object_count_3 = None
        self.obj_ID_start_1 = None
        self.obj_ID_start_2 = None
        self.obj_ID_start_3 = None
        
        # Should ideally abstract these out to a dedicated Armature class
        self.skeleton_count = None
        self.skeleton_idxs  = None
        self.bone_type      = None # Only get type-2 bones when unknown_0x04 active on some bones?
        self.bone_idx       = None
        self.bounding_box_id = None
        
        # Transform information
        self.position = None
        self.rotation = None
        self.scale    = None
        
    @classmethod
    def from_binary(cls, binary, flag, transform, scene_nodes, mesh_group_binaries, skeleton_binaries, bone_binaries, bbox_binaries):
        instance = cls()
        instance.flags_1         = flag
        instance.flags_2         = binary.flags
        instance.parent_ID       = scene_nodes.ptr_to_idx.get(binary.parent_offset, -1)
        if instance.parent_ID > -1: assert instance.parent_ID == binary.parent_ID
        instance.unknown_0x08    = binary.unknown_0x08
        instance.unknown_0x0C    = binary.unknown_0x0C
        instance.unknown_0x44    = binary.unknown_0x44
        instance.unknown_0x50    = binary.unknown_0x50
        instance.object_count_1  = binary.object_count_1
        instance.object_count_2  = binary.object_count_2
        instance.object_count_3  = binary.object_count_3
        instance.skeleton_count  = binary.skeleton_count
        instance.obj_ID_start_1  = mesh_group_binaries.ptr_to_idx.get(binary.object_offset_1, -1)
        instance.obj_ID_start_2  = mesh_group_binaries.ptr_to_idx.get(binary.object_offset_2, -1)
        instance.obj_ID_start_3  = mesh_group_binaries.ptr_to_idx.get(binary.object_offset_3, -1)
        instance.skeleton_idxs   = skeleton_binaries.ptr_to_idx.get(binary.skeletons_offset, -1)
        instance.bone_type       = binary.bone_type
        instance.bone_idx        = bone_binaries.ptr_to_idx.get(binary.bone_data_offset, -1)
        instance.bounding_box_id = bbox_binaries.ptr_to_idx.get(binary.bounding_box_offset, -1)
        instance.position        = transform[0:3]
        instance.rotation        = transform[4:8]
        instance.scale           = transform[8:11]
        return instance
    
    def to_binary(self, context, idx, scene_node_binaries, mesh_group_binaries, skeleton_binaries, bone_binaries, bounding_box_binaries, sn_children):
        binary = SceneNodeBinary(context)
        binary.flags        = self.flags_2
        binary.unknown_0x08 = self.unknown_0x08
        binary.unknown_0x0C = self.unknown_0x0C
        binary.unknown_0x44 = self.unknown_0x44
        binary.unknown_0x50 = self.unknown_0x50
        binary.object_count_1 = self.object_count_1
        binary.object_count_2 = self.object_count_2
        binary.object_count_3 = self.object_count_3
        binary.skeleton_count = self.skeleton_count
        binary.bone_type      = self.bone_type
        
        binary.ID = idx
        binary.object_offset_1  = mesh_group_binaries.idx_to_ptr[self.obj_ID_start_1] if self.obj_ID_start_1 > -1 else 0
        binary.object_offset_2  = mesh_group_binaries.idx_to_ptr[self.obj_ID_start_2] if self.obj_ID_start_2 > -1 else 0
        binary.object_offset_3  = mesh_group_binaries.idx_to_ptr[self.obj_ID_start_3] if self.obj_ID_start_3 > -1 else 0
        binary.skeletons_offset = skeleton_binaries  .idx_to_ptr[self.skeleton_idxs]  if self.skeleton_idxs  > -1 else 0
        binary.bone_data_offset = bone_binaries      .idx_to_ptr[self.bone_idx]       if self.bone_idx       > -1 else 0
            
        binary.parent_ID        = self.parent_ID if self.parent_ID > -1 else 0
        binary.parent_offset    = scene_node_binaries.idx_to_ptr[self.parent_ID] if self.parent_ID > -1 else 0
            
        children = sn_children[idx]
        binary.first_child_offset  = scene_node_binaries.idx_to_ptr[children[0]] if len(children) > 0 else 0
            
        siblings = sn_children[self.parent_ID] if self.parent_ID > -1 else [idx]

        own_sibling_idx = siblings.index(idx)
        next_sibling_id = siblings[own_sibling_idx + 1] if own_sibling_idx < (len(siblings) - 1) else -1
        binary.next_sibling_offset = scene_node_binaries.idx_to_ptr[next_sibling_id] if next_sibling_id > -1 else 0
            
        binary.bounding_box_offset = bounding_box_binaries.idx_to_ptr[self.bounding_box_id]         if self.bounding_box_id > -1 else 0
        binary.bounding_box_vertex_count = bounding_box_binaries[self.bounding_box_id].vertex_count if self.bounding_box_id > -1 else 0
        
        return self.flags_1, binary, [*self.position, 0., *self.rotation, *self.scale, 0.]

class MeshDefinitionInterface:
    def __init(self):
        self.flags = None
        
    @classmethod
    def from_binary(cls, binary):
        instance = cls()
        instance.flags = binary.flags
        return instance
    
    def to_binary(self, context):
        binary = MeshDefinitionBinary(context)
        binary.flags = self.flags
        return binary

class SkeletonInterface:
    def __init__(self):
        self.bone_ids = []
        
    @classmethod
    def from_binary(cls, binary):
        instance = cls()
        instance.bone_ids = binary.bone_ids
        return instance

    def to_binary(self, context):
        binary = SkeletonBinary(context)
        binary.id_count = len(self.bone_ids)
        binary.bone_ids = self.bone_ids
        return binary

class BoneInterface:
    def __init__(self):
        self.unknown_0x04 = None
        self.ibpm_idx     = None
        
    @classmethod
    def from_binary(cls, bone, ibpm_binaries):
        instance = cls()
        instance.unknown_0x04 = bone.unknown_0x04
        instance.ibpm_idx     = ibpm_binaries.ptr_to_idx[bone.ibpm_offset]
        return instance
    
    def to_binary(self, context, idx, ibpm_binaries):
        binary = BoneBinary(context)
        binary.ibpm_offset = ibpm_binaries.idx_to_ptr[self.ibpm_idx]
        binary.ID = idx
        binary.unknown_0x04 = self.unknown_0x04
        return binary

class BoundingBoxInterface:
    def __init__(self):
        self.vertices = []
        
    @classmethod
    def from_binary(cls, binary):
        instance = cls()
        instance.vertices = binary.vertices
        return instance
    
    def to_binary(self, context):
        binary = BoundingBoxBinary(context)
        binary.vertex_count = len(self.vertices)
        binary.vertices = self.vertices
        return binary

class MeshGroupInterface:
    def __init__(self):
        self.is_root            = None # Should be calculable...
        self.parent_bone_ID     = None
        self.unknown_0x0A       = None # ???
        self.material_ID        = None
        self.mesh_start_ID      = None
        self.mesh_count         = None
        
        self.vertex_offset      = None
        self.vertex_count       = None
        
    @classmethod
    def from_binary(cls, binary, mesh_binaries, material_binaries):
        instance = cls()
        instance.is_root        = binary.is_root
        instance.parent_bone_ID = binary.parent_bone_ID
        instance.unknown_0x0A   = binary.unknown_0x0A
        instance.material_ID    = material_binaries.ptr_to_idx[binary.material_offset]
        instance.mesh_start_ID  = mesh_binaries.ptr_to_idx[binary.meshes_offset]
        instance.mesh_count     = binary.mesh_count
        instance.vertex_offset  = binary.vertex_offset
        instance.vertex_count   = binary.vertex_count
        return instance
    
    def to_binary(self, context, idx, mesh_binaries, material_binaries):
        binary = MeshGroupBinary(context)
        binary.ID = idx
        binary.is_root        = self.is_root
        binary.parent_bone_ID = self.parent_bone_ID
        binary.unknown_0x0A   = self.unknown_0x0A
        binary.material_offset = material_binaries.idx_to_ptr[self.material_ID]
        binary.meshes_offset   = mesh_binaries.idx_to_ptr[self.mesh_start_ID]
        binary.mesh_count     = self.mesh_count
        binary.vertex_offset  = self.vertex_offset
        binary.vertex_count   = self.vertex_count
        return binary
        
class MeshInterface:
    def __init__(self):
        self.unknown_0x02       = None
        self.unknown_0x04       = None
        self.vertex_groups      = []
        self.vertices           = []
        self.face_indices       = []
        
    @classmethod
    def from_binary(cls, binary, vertex_bank, face_bank, vertex_group_binaries):
        instance = cls()
        instance.unknown_0x02  = binary.unknown_0x02
        instance.unknown_0x04  = binary.unknown_0x04
        instance.vertex_groups = []
        instance.vertices      = []
        instance.face_indices  = []
        return instance
    
    def to_binary(self, context):
        binary = MeshBinary(context)
        binary.vertex_group_count   = len(self.vertex_groups)
        binary.unknown_0x02         = self.unknown_0x02
        binary.unknown_0x04         = self.unknown_0x04
        binary.vertex_count         = len(self.vertices)
        binary.faces_count          = len(self.face_indices)
        # binary.vertex_groups_offset = None
        
        # self.kfmg_vertices_idx       = None
        # self.kfmg_faces_idx          = None
        # self.mesh_group_vertices_idx = None
        return binary


class MaterialInterface:
    def __init__(self):
        self.shader_ID        = None
        self.src_blend        = None
        self.dst_blend        = None
        self.backface_culling = None
        self.unknown_0x88     = None
        self.unknown_0x94     = None
        self.unknown_0x94     = None
        self.color_1          = None
        self.color_2          = None
        self.color_3          = None
        self.color_4          = None
        self.textures         = []
    
    @classmethod
    def from_binary(cls, binary, texture_binaries):
        instance = cls()
        instance.shader_ID        = binary.shader_ID
        instance.src_blend        = binary.src_blend
        instance.dst_blend        = binary.dst_blend
        instance.backface_culling = binary.backface_culling
        
        if binary.texture_1_offset:
            instance.textures.append(texture_binaries.ptr_to_idx[binary.texture_1_offset])
        if binary.texture_2_offset:
            instance.textures.append(texture_binaries.ptr_to_idx[binary.texture_2_offset])
        if binary.texture_3_offset:
            instance.textures.append(texture_binaries.ptr_to_idx[binary.texture_3_offset])
        
        instance.color_1         = binary.color_1
        instance.color_2         = binary.color_2
        instance.color_3         = binary.color_3
        instance.color_4         = binary.color_4
        instance.unknown_0x88    = binary.unknown_0x88
        instance.unknown_0x94    = binary.unknown_0x94
        instance.unknown_0x9C    = binary.unknown_0x9C
        
        return instance

    def to_binary(self, context):
        binary = MaterialBinary(context)
        
        # Need to fill in offsets after they'e been calculated
        binary.unknown_0x00     = 0
        binary.shader_ID        = self.shader_ID
        binary.num_textures     = len(self.textures)
        binary.src_blend        = self.src_blend
        binary.dst_blend        = self.dst_blend
        binary.backface_culling = self.backface_culling
        
        binary.color_1          = self.color_1
        binary.color_2          = self.color_2
        binary.color_3          = self.color_3
        binary.color_4          = self.color_4
        binary.unknown_0x88     = self.unknown_0x88
        binary.unknown_0x94     = self.unknown_0x94
        binary.unknown_0x9C     = self.unknown_0x9C
        
        return binary
        

class TextureInterface:
    def __init__(self):
        self.texture_ID = None
        self.blend_factor = None
        
    @classmethod
    def from_binary(cls, binary):
        instance = cls()
        instance.texture_ID = binary.texture_ID
        instance.blend_factor = binary.blend_factor
        return instance
    
    def to_binary(self, context):
        binary = TextureBinary(context)
        binary.unknown_0x00 = 0
        binary.texture_ID   = self.texture_ID
        binary.unknown_0x06 = 0
        binary.blend_factor = self.blend_factor
        binary.unknown_0x18 = 0.
        binary.unknown_0x1C = 0.
        binary.unknown_0x24 = 0
        return binary

class UnknownIndicesInterface:
    @staticmethod
    def from_binary(binary):
        return [list(o.indices) for o in binary.index_groups]
    
    @staticmethod
    def to_binary(context, lst):
        binary = UnknownIndicesBinary(context)
        for idx_list in lst:
            igb = UnknownIndexGroupBinary(context)
            igb.count = len(idx_list)
            igb.indices = idx_list
            binary.index_groups.append(igb)
        return binary
    