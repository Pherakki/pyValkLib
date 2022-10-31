from .HMDLReadWriter import HMDLReadWriter
from .KFMD.KFMDReadWriter import KFMDReadWriter
from .KFMD.KFMS.SceneNode import SceneNodeBinary
from .KFMD.KFMS.MeshDefinition import MeshDefinitionBinary
from .KFMD.KFMS.Skeleton import SkeletonBinary
from .KFMD.KFMS.Bone import BoneBinary
from .KFMD.KFMS.MeshGroup import MeshGroupBinary
from .KFMD.KFMS.Mesh import MeshBinary
from .KFMD.KFMS.Material import MaterialBinary
from .KFMD.KFMS.Texture import TextureBinary
from .KFMD.KFMS.UnknownIndices import UnknownIndicesBinary, UnknownIndexGroupBinary

from pyValkLib.serialisation.ReadWriter import OffsetTracker

class KFMDInterface:
    def __init__(self):
        # Replace a SceneNode tree with an Armature where appropriate?
        # Can SceneNodes be mixed with Bones?
        # Meshes can be placed as leaf nodes of bones...
        self.flags = None
        self.unknown_count_4 = None
        self.unknown_0x64 = None
        self.unknown_0x70 = None
        self.unknown_0x74 = None
        self.unknown_0x80 = None
        self.scene_nodes = []
        self.unknown_1s  = []
        self.unknown_2s  = []
        self.unknown_3s  = []
        self.mesh_defs   = []
        self.skeletons   = []
        self.bones       = []
        self.meshes      = []
        self.materials   = []
        self.textures    = []
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
        instance.scene_nodes = [SceneNodeInterface.from_binary(sno, flag, transform, binary.mesh_groups, binary.skeletons, binary.bones)
                                for flag, sno, transform in zip(binary.scene_node_flags, binary.scene_nodes, binary.scene_node_transforms)]
        instance.unknown_1s = binary.unknown_chunk_1
        instance.unknown_2s = binary.unknown_chunk_2
        instance.unknown_3s = binary.unknown_chunk_3
        instance.skeletons = [SkeletonInterface.from_binary(skel) for skel in binary.skeletons]
        instance.bones     = [BoneInterface.from_binary(bone) for bone in binary.bones]
        instance.meshes    = [MeshInterface.from_binary(mesh, [], [], binary.vertex_groups) for mesh in binary.meshes]
        instance.materials = [MaterialInterface.from_binary(mat, binary.textures) for mat in binary.materials]
        instance.textures  = [TextureInterface.from_binary(tex) for tex in binary.textures]
        instance.unknown_indices = UnknownIndicesInterface.from_binary(binary.unknown_indices)
        instance.unknown_objects = [o for o in binary.unknown_objects]
        return instance
        
    def to_binary(self, endianness):
        KFMD_binary = KFMDReadWriter(endianness)
        
        # First dump KFMG
        # Fill me in!
        
        # Dump KFMS
        binary = KFMD_binary.KFMS
        ctx = binary.context
        
        binary.scene_node_flags,
        binary.scene_nodes,
        binary.scene_node_transforms = zip(sni.to_binary(ctx) for sni in self.scene_nodes)
        binary.unknown_chunk_1 = self.unknown_1s
        binary.unknown_chunk_2 = self.unknown_2s
        binary.unknown_chunk_3 = self.unknown_3s
        binary.skeletons.data  = [si.to_binary(ctx) for si in self.skeletons]
        binary.bones.data      = [bi.to_binary(ctx) for bi in self.bones]
        binary.meshes.data     = [mi.to_binary(ctx) for mi in self.meshes] # Need a PIA constructor that auto-gens pointers...
        binary.materials.data  = [mi.to_binary(ctx) for mi in self.materials]
        binary.textures.data   = [ti.to_binary(ctx) for ti in self.textures]
        binary.unknown_indices = UnknownIndicesInterface.to_binary(ctx, self.unknown_indices)
        binary.unknown_objects = [ui.to_binary(ctx) for ui in self.unknown_objects]
        
        binary.flags             = self.flags
        binary.unknown_count_4   = self.unknown_count_4
        binary.unknown_0x64      = self.unknown_0x64
        binary.unknown_0x6C      = self.unknown_0x6C
        binary.unknown_0x70      = self.unknown_0x70
        binary.unknown_0x74      = self.unknown_0x74
        binary.unknown_0x80      = self.unknown_0x80
        binary.scene_node_count  = len(self.scene_nodes)
        binary.bone_count        = len(self.bones)
        
        binary.material_count    = len(self.materials)
        binary.mesh_group_count  = len(self.mesh_groups)
        binary.mesh_count        = len(self.meshes)
        binary.unknown_obj_count = len(self.unknown_objects)
        binary.texture_count     = len(self.textures)
        binary.unknown_count_1   = len(self.unknown_chunk_1)
        binary.unknown_count_2   = len(self.unknown_chunk_2)
        binary.unknown_count_3   = len(self.unknown_chunk_3)
        binary.mesh_defs_count   = len(self.mesh_defs)
        
        # Now construct derived objects
        
        # Now fill in offsets...
        ot = OffsetTracker()
        binary.header.read_write(ot)
        binary.rw_fileinfo(ot)
        
        binary.scene_node_flags_offset = ot.local_tell()
        binary.rw_scene_node_flags(ot)
        
        binary.scene_nodes_offset = ot.local_tell()
        binary.rw_scene_nodes(ot)
        
        binary.scene_node_transforms_offset = ot.local_tell()
        binary.rw_scene_node_transforms(ot)
        
        binary.unknown_offset_1 = ot.local_tell()
        binary.rw_unknown_chunk_1(ot)
        binary.unknown_offset_2 = ot.local_tell()
        binary.rw_unknown_chunk_2(ot)
        binary.unknown_offset_3 = ot.local_tell()
        binary.rw_unknown_chunk_3(ot)
        
        binary.mesh_defs_offset = ot.local_tell()
        binary.rw_mesh_definitions(ot)
        
        # Construct bounding boxes...!
        binary.rw_bounding_boxes(ot)
        binary.rw_skeletons(ot)
        binary.rw_bones(ot)
        binary.rw_bone_ibpms(ot)
        
        binary.mesh_groups_offset = ot.local_tell()
        binary.rw_mesh_groups(ot)
        
        binary.materials_offset = ot.local_tell()
        binary.rw_materials(ot)
        
        binary.meshes_offset = ot.local_tell()
        binary.rw_meshes(ot)
        
        # Construct vertex groups...
        binary.rw_vertex_groups(ot)
        
        binary.textures_offset = ot.local_tell()
        binary.rw_textures(ot)
        
        binary.unknown_indices_offset = ot.local_tell()
        binary.rw_unknown_indices(ot)
        
        binary.unknown_objs_offset = ot.local_tell()
        binary.rw_unknown_objects(ot)
        
        binary.model_height = None
        
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
        self.obj_IDs_1 = None
        self.obj_IDs_2 = None
        self.obj_IDs_3 = None
        
        # Should ideally abstract these two out to a dedicated Armature class
        self.is_skeleton = None
        self.is_bone = None
        
        # Transform information
        self.position = None
        self.rotation = None
        self.scale    = None
        
    @classmethod
    def from_binary(cls, binary, flag, transform, mesh_group_binaries, skeleton_binaries, bone_binaries):
        instance = cls()
        instance.flags_1       = flag
        instance.flags_2       = binary.flags
        instance.parent_ID     = binary.parent_ID
        instance.unknown_0x08  = binary.unknown_0x08
        instance.unknown_0x0C  = binary.unknown_0x0C
        instance.unknown_0x44  = binary.unknown_0x44
        instance.unknown_0x50  = binary.unknown_0x50
        obj_idx_1 = mesh_group_binaries.ptr_to_idx.get(binary.object_offset_1, -1)
        instance.obj_IDs_1     = list(range(obj_idx_1, obj_idx_1 + binary.object_count_1))
        obj_idx_2 = mesh_group_binaries.ptr_to_idx.get(binary.object_offset_2, -1)
        instance.obj_IDs_2     = list(range(obj_idx_2, obj_idx_2 + binary.object_count_2))
        obj_idx_3 = mesh_group_binaries.ptr_to_idx.get(binary.object_offset_3, -1)
        instance.obj_IDs_3     = list(range(obj_idx_3, obj_idx_3 + binary.object_count_3))
        skel_idx = skeleton_binaries.ptr_to_idx.get(binary.skeletons_offset, -1)
        instance.skeleton_idxs = list(range(skel_idx, skel_idx + binary.skeleton_count))
        instance.bone_idx      = bone_binaries.ptr_to_idx.get(binary.bone_data_offset, -1)
        instance.position      = transform[0:3]
        instance.rotation      = transform[4:8]
        instance.scale         = transform[8:11]
        return instance
    
    def to_binary(self, context):
        binary = SceneNodeBinary(context)
        binary.flags        = self.flags_2
        binary.parent_ID    = self.parent_ID
        binary.unknown_0x08 = self.unknown_0x08
        binary.unknown_0x0C = self.unknown_0x0C
        binary.unknown_0x44 = self.unknown_0x44
        binary.unknown_0x50 = self.unknown_0x50
        binary.object_count_1 = len(self.obj_IDs_1)
        binary.object_count_2 = len(self.obj_IDs_2)
        binary.object_count_3 = len(self.obj_IDs_3)
        binary.skeleton_count = len(self.skeleton_idxs)
        
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
        
    @classmethod
    def from_binary(cls, bone):
        instance = cls()
        instance.unknown_0x04 = bone.unknown_0x04
        return instance
    
    def to_binary(self, context):
        binary = BoneBinary(context)
        binary.unknown_0x04 = self.unknown_0x04
        return binary

class MeshGroupInterface:
    def __init__(self):
        self.is_root            = None # Should be calculable...
        self.parent_bone_ID     = None
        self.unknown_0x0A       = None
        self.material_ID        = None
        self.mesh_IDs           = None
        
    @classmethod
    def from_binary(cls, binary, mesh_binaries, material_binaries):
        instance = cls()
        instance.is_root = binary.is_root
        instance.parent_bone_ID = binary.parent_bone_ID
        instance.unknown_0x0A = binary.unknown_0x0A
        instance.material_ID = material_binaries.ptr_to_idx[binary.material_offset]
        mesh_start_idx = mesh_binaries.ptr_to_idx[binary.meshes_offset]
        instance.mesh_IDs = list(range(mesh_start_idx, mesh_start_idx + binary.mesh_count))
        return instance
    
    def to_binary(self, context):
        binary = MeshGroupBinary(context)
        binary.is_root = self.is_root
        binary.parent_bone_ID = self.parent_bone_ID
        binary.unknown_0x0A = self.unknown_0x0A
        # Material offset
        # Mesh offset
        binary.mesh_count = len(self.mesh_IDs)
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