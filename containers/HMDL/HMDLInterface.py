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
        self.materials       = []
        self.meshes          = MeshDataInterface()
        self.vertex_groups   = [] # Should be calculable
        self.textures        = []
        self.unknown_indices = None
        self.unknown_objects = []

    @classmethod
    def from_binary(cls, KFMD_binary):
        binary = KFMD_binary.KFMS
        KFMG_binary = KFMD_binary.KFMG
        
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
        instance.meshes          = MeshDataInterface.mesh_objects_from_binary(KFMG_binary, binary.mesh_groups, binary.meshes, binary.materials, binary.vertex_groups)
        instance.materials       = [MaterialInterface.from_binary(mat, binary.textures) for mat in binary.materials]
        instance.vertex_groups   = binary.vertex_groups
        instance.textures        = binary.textures
        instance.unknown_indices = UnknownIndicesInterface.from_binary(binary.unknown_indices)
        instance.unknown_objects = binary.unknown_objects
        


        # instance.skeletons  = [SkeletonInterface.from_binary(skel) for skel in binary.skeletons]
        # instance.bounding_boxes = [BoundingBoxInterface.from_binary(bbox) for bbox in binary.bounding_boxes]
        # instance.textures   = [TextureInterface.from_binary(tex) for tex in binary.textures]
        
        return instance
        
    def to_binary(self, endianness, depth, KFMG, ENRS, CCRS, validation_mode=False):
        KFMD_binary = KFMDReadWriter(endianness)
        KFMG_binary = KFMD_binary.KFMG
        
        # First dump KFMG
        # Fill me in!
        
        # Dump KFMS
        binary = KFMD_binary.KFMS
        ctx = binary.context
        ctx.endianness = ">" if self.flags & 1 == 1 else "<"

        
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
        binary.vertex_groups    = self.vertex_groups
        binary.textures         = self.textures
        binary.unknown_objects  = self.unknown_objects
        
        
        binary.scene_node_count  = len(self.scene_nodes)
        binary.bone_count        = len(self.bones)
        binary.material_count    = len(self.materials)
        binary.mesh_group_count  = len(self.meshes.groups)
        binary.mesh_count        = sum([len(bundle) for bundle in self.meshes.bundles])
        binary.unknown_obj_count = len(self.unknown_objects)
        binary.texture_count     = len(self.textures)
        binary.unknown_count_1   = len(self.unknown_1s)
        binary.unknown_count_2   = len(self.unknown_2s)
        binary.unknown_count_3   = len(self.unknown_3s)
        binary.mesh_defs_count   = len(self.mesh_defs)
        
        # # Fill in data
        
        # binary.skeletons.data  = [si.to_binary(ctx) for si in self.skeletons]
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
        
        binary.mesh_groups_offset = ot.local_tell() if len(self.meshes.groups) else 0
        binary.mesh_groups = construct_PIA(ctx, lambda: MeshGroupBinary(ctx), binary.mesh_group_count, ot.local_tell(), 0x20)
        binary.rw_mesh_groups(ot)
        
        binary.materials_offset = ot.local_tell() if len(self.materials) else 0
        binary.materials = construct_PIA(ctx, lambda: MaterialBinary(ctx), len(self.materials), ot.local_tell(), 0xA0)
        binary.rw_materials(ot)
        
        binary.meshes_offset = ot.local_tell() if len(self.meshes.bundles) else 0
        binary.meshes = construct_PIA(ctx, lambda: MeshBinary(ctx), binary.mesh_count, ot.local_tell(), 0x20)
        binary.rw_meshes(ot)
        
        # Construct vertex groups...
        binary.rw_vertex_groups(ot)
        
        binary.textures_offset = ot.local_tell() if len(self.textures) else 0
        binary.rw_textures(ot)
        
        binary.unknown_indices_offset = ot.local_tell() if len(self.unknown_indices.index_groups) else 0
        binary.unknown_indices = self.unknown_indices.to_binary(ctx, binary.unknown_indices_offset)
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

        # Materials
        binary.materials.data = [mat.to_binary(ctx, binary.textures) for mat in self.materials]
            
        # KFMG, Meshes, Mesh Groups
        if validation_mode:
            KFMD_binary.KFMG,\
            binary.meshes.data,\
            binary.mesh_groups.data = self.meshes.mesh_objects_to_validator_binary(ctx, KFMG_binary, binary.mesh_definitions[0], binary.meshes, binary.materials, binary.vertex_groups)
            
        else:
            KFMD_binary.KFMG,\
            binary.meshes.data,\
            binary.mesh_groups.data = self.meshes.mesh_objects_to_binary(ctx, KFMG_binary, binary.mesh_definitions[0], binary.meshes, binary.materials, binary.vertex_groups)
        
        ############################
        # KFMS HEADER AND METADATA #
        ############################
        binary.header.data_length = ot.local_tell() - binary.header.header_length
        binary.header.depth = depth + 1
        
        binary.POF0 = binary.POF0.from_obj(binary)
        if validation_mode:
            binary.ENRS = ENRS
            binary.CCRS = CCRS
        else:
            binary.ENRS = binary.ENRS.from_obj(binary)
            binary.CCRS = binary.CCRS.from_obj(binary)
        binary.MTXS = binary.MTXS.from_obj(binary)
        binary.EOFC.header.depth = binary.header.depth + 1
        
        ot.rw_obj(binary.POF0)
        ot.rw_obj(binary.ENRS)
        ot.rw_obj(binary.CCRS)
        ot.rw_obj(binary.MTXS)
        ot.rw_obj(binary.EOFC)
        
        binary.header.contents_length = ot.local_tell() - binary.header.header_length
        
        binary.context.endianness = endianness
        
        ############################
        # KFMG HEADER AND METADATA #
        ############################
        
        if validation_mode:
            KFMD_binary.KFMG = KFMG
            KFMG_binary = KFMD_binary.KFMG
        else:
            ot = OffsetTracker()
            KFMG_binary.KFMS_ref = binary
            KFMG_binary.header.read_write(ot)
            KFMG_binary.read_write_contents(ot)
                
            KFMG_binary.header.data_length = ot.local_tell() - KFMG_binary.header.header_length
            KFMG_binary.header.depth = depth + 1
            
            KFMG_binary.ENRS = KFMG_binary.ENRS.from_obj(KFMG_binary)
            KFMG_binary.CCRS = KFMG_binary.CCRS.from_obj(KFMG_binary)
            KFMG_binary.EOFC.header.depth = KFMG_binary.header.depth + 1
            
            ot.rw_obj(KFMG_binary.ENRS)
            ot.rw_obj(KFMG_binary.CCRS)
            ot.rw_obj(KFMG_binary.EOFC)
            
            KFMG_binary.header.contents_length = ot.local_tell() - KFMG_binary.header.header_length
            
            KFMG_binary.context.endianness = endianness
        
        ############################
        # KFMD HEADER AND METADATA #
        ############################
        
        KFMD_binary.header.data_length = 0
        KFMD_binary.header.depth = depth
        KFMD_binary.header.contents_length = sum(c.header.header_length + c.header.contents_length for c in KFMD_binary.get_subcontainers())
        KFMD_binary.EOFC.header.depth = depth + 1
        
        return KFMD_binary

class MeshDataInterface:
    def __init__(self):
        self.groups = None
        self.bundles = None
        
    @classmethod
    def mesh_objects_from_binary(cls, KFMG_binary, mesh_group_binaries, mesh_binaries, material_binaries, vertex_group_binaries):
        face_bank = KFMG_binary.faces
        vertex_bank = KFMG_binary.vertices
        
        instance = cls()
        mg_ids = {
            i : (mg.meshes_offset, mg.mesh_count)
            for i, mg in enumerate(mesh_group_binaries)
        }
        mb_ids = {key: i for i, key in enumerate(sorted(set(mg_ids.values())))}
        
        keylist = sorted([(mesh_binaries.ptr_to_idx[key[0]], key[1]) for key in mb_ids.keys()])
        for (mk1, mi1), (mk2, _) in zip(keylist, keylist[1:]):
            if mk1 + mi1 != mk2: raise ValueError("Malformed mesh groups: meshes are shared between groups.")

        instance.bundles = [
            [
                MeshInterface.from_binary(mesh_binaries[i], vertex_bank, face_bank, vertex_group_binaries)
                for i in range(mk, mk+mi)
            ]
            for mk, mi in keylist
        ]
        
        instance.groups = [
            MeshGroupInterface.from_binary(mg, mb_ids, instance.bundles, material_binaries)
            for mg in mesh_group_binaries
        ]
        
        
        return instance
    
    def mesh_objects_to_validator_binary(self, context, KFMG_binary, mesh_def, mesh_binaries, material_binaries, vertex_group_binaries):
        mbs         = []
        mgs         = []
        
        bundle_idx_to_mesh_info = []
        for bundle in self.bundles:
            initial_idx, initial_count = len(mbs), len(bundle)
            vtx_count = 0
            for mb in bundle:
                mbs.append(mb.to_validator_binary(context, vtx_count, vertex_group_binaries))
                vtx_count += len(mb.vertices)
            
            bundle_idx_to_mesh_info.append((initial_idx, initial_count, bundle[0].kfmg_vertices_idx*mesh_def.bytes_per_vertex, vtx_count))
            
        mgs = [mg.to_binary(context, idx, bundle_idx_to_mesh_info, mesh_binaries, material_binaries) for idx, mg in enumerate(self.groups)]
        
        return KFMG_binary, mbs, mgs
                
    def mesh_objects_to_binary(self, context, KFMG_binary, mesh_def, mesh_binaries, material_binaries, vertex_group_binaries):
        mbs         = []
        mgs         = []
        KFMG_binary.vertices.data = []
        KFMG_binary.faces.data = []

        bundle_idx_to_mesh_info = []
        total_vtx_count = 0
        total_face_count = 0
        for bundle in self.bundles:
            initial_idx, initial_count = len(mbs), len(bundle)
            vtx_count = 0
            face_count = 0
            for mb in bundle:
                mbs.append(mb.to_binary(context, total_vtx_count, total_face_count, vtx_count, vertex_group_binaries))
                vtx_count += len(mb.vertices)
                face_count += len(mb.face_indices)
                
                KFMG_binary.vertices.data += mb.vertices
                KFMG_binary.faces.data += mb.face_indices
            
            bundle_idx_to_mesh_info.append((initial_idx, initial_count, total_vtx_count*mesh_def.bytes_per_vertex, vtx_count))
            
            total_vtx_count += vtx_count
            total_face_count += face_count
            
        mgs = [mg.to_binary(context, idx, bundle_idx_to_mesh_info, mesh_binaries, material_binaries) for idx, mg in enumerate(self.groups)]
        mesh_def.faces_offset = 0
        mesh_def.vertices_offset = len(KFMG_binary.faces)*2
        mesh_def.vertices_offset += (0x10 - (mesh_def.vertices_offset % 0x10)) % 0x10
        mesh_def.faces_count = len(KFMG_binary.faces)
        mesh_def.vertices_count = len(KFMG_binary.vertices)
        
        return KFMG_binary, mbs, mgs
        
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
        self.bundle_ID          = None
        
        self.vertex_offset      = None
        self.vertex_count       = None
        
    @classmethod
    def from_binary(cls, binary, mesh_bundle_ids, mesh_bundles, material_binaries):
        instance = cls()
        instance.is_root        = binary.is_root
        instance.parent_bone_ID = binary.parent_bone_ID
        instance.unknown_0x0A   = binary.unknown_0x0A
        instance.material_ID    = material_binaries.ptr_to_idx[binary.material_offset]
        instance.bundle_ID      = mesh_bundle_ids[(binary.meshes_offset, binary.mesh_count)]
        instance.vertex_offset  = binary.vertex_offset
        instance.vertex_count   = binary.vertex_count
        return instance
    
    def to_binary(self, context, idx, bundle_ID_to_mesh_info, mesh_binaries, material_binaries):
        binary = MeshGroupBinary(context)
        binary.ID = idx
        binary.is_root        = self.is_root
        binary.parent_bone_ID = self.parent_bone_ID
        binary.unknown_0x0A   = self.unknown_0x0A
        binary.material_offset = material_binaries.idx_to_ptr[self.material_ID]
        
        ID, count, vertex_offset, vertex_count = bundle_ID_to_mesh_info[self.bundle_ID]
        
        binary.meshes_offset  = mesh_binaries.idx_to_ptr[ID]
        binary.mesh_count     = count
        binary.vertex_offset  = vertex_offset
        binary.vertex_count   = vertex_count
        return binary
        
class MeshInterface:
    def __init__(self):
        self.unknown_0x02            = None
        self.unknown_0x04            = None
        self.vertex_group_count      = None
        self.vertex_group_start_ID   = None
        self.vertex_count            = None
        self.kfmg_vertices_idx       = None
        self.faces_count             = None
        self.kfmg_faces_idx          = None
        self.mesh_group_vertices_idx = None
        
        self.vertices              = []
        self.face_indices          = []
        
    @classmethod
    def from_binary(cls, binary, vertex_bank, face_bank, vertex_group_binaries):
        instance = cls()
        instance.unknown_0x02          = binary.unknown_0x02
        instance.unknown_0x04          = binary.unknown_0x04
        instance.vertex_group_start_ID = vertex_group_binaries.ptr_to_idx.get(binary.vertex_groups_offset, -1)
        instance.vertex_group_count    = binary.vertex_group_count
        
        # Ver 1
        instance.vertex_count            = binary.vertex_count
        instance.kfmg_vertices_idx       = binary.kfmg_vertices_idx
        instance.faces_count             = binary.faces_count
        instance.kfmg_faces_idx          = binary.kfmg_faces_idx
        instance.mesh_group_vertices_idx = binary.mesh_group_vertices_idx
        
        # Ver 2
        instance.vertices      = vertex_bank[binary.kfmg_vertices_idx:binary.kfmg_vertices_idx+binary.vertex_count]
        instance.face_indices  = face_bank[binary.kfmg_faces_idx:binary.kfmg_faces_idx+binary.faces_count]
        
        return instance
    
    def to_binary(self, context, prev_verts, prev_faces, vtx_count, vertex_group_binaries):
        binary = MeshBinary(context)
        binary.vertex_group_count   = self.vertex_group_count
        binary.unknown_0x02         = self.unknown_0x02
        binary.unknown_0x04         = self.unknown_0x04
        
        binary.unknown_0x02          = self.unknown_0x02
        binary.unknown_0x04          = self.unknown_0x04
        binary.vertex_groups_offset  = vertex_group_binaries.idx_to_ptr[self.vertex_group_start_ID] if self.vertex_group_start_ID > -1 else 0
        binary.vertex_group_count    = self.vertex_group_count

        binary.vertex_count            = len(self.vertices)
        binary.faces_count             = len(self.face_indices)
        binary.kfmg_vertices_idx       = prev_verts
        binary.kfmg_faces_idx          = prev_faces
        binary.mesh_group_vertices_idx = vtx_count
        
        return binary
    
    def to_validator_binary(self, context, vtx_count, vertex_group_binaries):
        binary = MeshBinary(context)
        binary.vertex_group_count   = self.vertex_group_count
        binary.unknown_0x02         = self.unknown_0x02
        binary.unknown_0x04         = self.unknown_0x04
        
        binary.unknown_0x02          = self.unknown_0x02
        binary.unknown_0x04          = self.unknown_0x04
        binary.vertex_groups_offset  = vertex_group_binaries.idx_to_ptr[self.vertex_group_start_ID] if self.vertex_group_start_ID > -1 else 0
        binary.vertex_group_count    = self.vertex_group_count
        
        binary.vertex_count            = self.vertex_count
        binary.kfmg_vertices_idx       = self.kfmg_vertices_idx
        binary.faces_count             = self.faces_count
        binary.kfmg_faces_idx          = self.kfmg_faces_idx
        binary.mesh_group_vertices_idx = vtx_count
        
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
        self.texture_1_ID     = None
        self.texture_2_ID     = None
        self.texture_3_ID     = None
    
    @classmethod
    def from_binary(cls, binary, texture_binaries):
        instance = cls()
        instance.unknown_0x00     = binary.unknown_0x00
        instance.shader_ID        = binary.shader_ID
        instance.src_blend        = binary.src_blend
        instance.dst_blend        = binary.dst_blend
        instance.backface_culling = binary.backface_culling
        
        instance.texture_1_ID = texture_binaries.ptr_to_idx.get(binary.texture_1_offset, -1)
        instance.texture_2_ID = texture_binaries.ptr_to_idx.get(binary.texture_2_offset, -1)
        instance.texture_3_ID = texture_binaries.ptr_to_idx.get(binary.texture_3_offset, -1)
        
        instance.color_1         = binary.color_1
        instance.color_2         = binary.color_2
        instance.color_3         = binary.color_3
        instance.color_4         = binary.color_4
        instance.unknown_0x88    = binary.unknown_0x88
        instance.unknown_0x94    = binary.unknown_0x94
        instance.unknown_0x9C    = binary.unknown_0x9C
        
        return instance

    def to_binary(self, context, texture_binaries):
        binary = MaterialBinary(context)
        
        # Need to fill in offsets after they'e been calculated
        binary.unknown_0x00     = self.unknown_0x00
        binary.shader_ID        = self.shader_ID
        binary.num_textures     = sum([t > -1 for t in [self.texture_1_ID, self.texture_2_ID, self.texture_3_ID]])
        binary.src_blend        = self.src_blend
        binary.dst_blend        = self.dst_blend
        binary.backface_culling = self.backface_culling
        
        binary.texture_1_offset = texture_binaries.idx_to_ptr[self.texture_1_ID] if self.texture_1_ID > -1 else 0
        binary.texture_2_offset = texture_binaries.idx_to_ptr[self.texture_2_ID] if self.texture_2_ID > -1 else 0
        binary.texture_3_offset = texture_binaries.idx_to_ptr[self.texture_3_ID] if self.texture_3_ID > -1 else 0
        
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
    def __init__(self):
        self.index_groups = []
    
    @classmethod
    def from_binary(cls, binary):
        instance = cls()
        instance.index_groups = [list(o.indices) for o in binary.index_groups]
        return instance
    
    def to_binary(self, context, start_offset):
        binary = UnknownIndicesBinary(context)
        binary.unknown_objs_offset = start_offset + 0x10
        accumulated_offset = start_offset + 0x10 + len(self.index_groups)*0x08
        accumulated_offset += (0x10 - (accumulated_offset % 0x10)) % 0x10
        for idx_group in self.index_groups:
            igb = UnknownIndexGroupBinary(context)
            igb.count   = len(idx_group)
            igb.indices = idx_group
            igb.offset  = accumulated_offset
            binary.index_groups.append(igb)
            accumulated_offset += igb.count*0x08
        return binary
    