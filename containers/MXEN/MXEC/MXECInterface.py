from collections import defaultdict
import os
import json
import struct

from .MXECReadWriter import MXECReadWriter
from .ECSEntityEntry import EntityEntry, EntityData, EntitySubEntry
from pyValkLib.serialisation.ReadWriter import OffsetTracker, POF0Builder, ENRSBuilder, CCRSBuilder
from pyValkLib.containers.POF0.POF0ReadWriter import compressPOF0
from pyValkLib.containers.ENRS.ENRSCompression import compressENRS, toENRSPackedRep
from pyValkLib.containers.CCRS.CCRSCompression import compressCCRS, toCCRSPackedRep


entity_structs = {}
struct_path = os.path.abspath("pyValkLib/configuration/MXE/Entities")
for file in os.listdir(struct_path):
    filename, fileext = os.path.splitext(file)
    if fileext == ".json":
        filepath = os.path.join(struct_path, file)
        with open(filepath, 'r') as F:
            entity_structs[filename] = json.load(F)
            if "SubEntities" not in entity_structs[filename]:
                raise Exception(f"Invalid Entity structure file {filename}: No 'SubEntities' member.")
            if "Parameters" not in entity_structs[filename]:
                raise Exception(f"Invalid Entity structure file {filename}: No 'Parameters' member.")


class ParameterInterface:
    def __init__(self):
        self.name = None
        self.ID = None
        self.param_type = None
        self.parameters = None
        self.subparameters = None

class EntityParameterReference:
    def __init__(self, type_, subtype_):
        self.param_id = None
        self.type = type_
        self.subtype = subtype_

class EntityComponentInferface:
    def __init__(self, type_):
        self.type = type_
        self.subentities = []
        self.parameters = []
        def_struct = entity_structs[type_]
        for en in def_struct["SubEntities"]:
            self.subentities.append(EntityComponentInferface(en))
        for subtype_, type_ in def_struct["Parameters"]:
            self.parameters.append(EntityParameterReference(type_, subtype_))
        
    def flat_decendants(self):
        out = []
        for subentity in self.subentities:
            out.append(subentity)
            for dec in subentity.flat_decendants():
                out.append(dec)
        return out
    
    def get_param_prefixes(self):
        out = {}
        
        # Append entity name to front of child's stack
        for subentity in self.subentities:
            name_strs = subentity.get_param_prefixes()
            for param_id, name_str in name_strs.items():
                out[param_id] = "!" + self.type + name_str
        
        # Add own parameters to stack
        for param in self.parameters:
            name_str = "!" + self.type + "!@" + param.subtype + "@"
            out[param.param_id] = name_str
            
        return out
        
class EntityInterface:
    def __init__(self):
        self.ID = None
        self.name = None
        self.unknown = None
        self.controller_id = None
        self.subcomponents = []
        self.entity = None
        
    def all_flat_entities(self):
        return [self.entity, *self.entity.flat_decendants()]
    
    def get_all_param_prefixes(self):
        return self.entity.get_param_prefixes()

class NodeInterface:
    def __init__(self):
        self.param_id = None
        self.next_edges = []
        
class EdgeInterface:
    def __init__(self):
        self.next_node = None
        self.param_ids = []

class SubgraphInterface:
    def __init__(self):
        self.nodes = []

class GraphInterface:
    def __init__(self):
        self.name = None
        self.subgraphs = []
        
class AssetInterface:
    """
    Main ID Order: ???
    Unknown ID 1 order: ??? Related to entity / parameter types?
    Unknown ID 2 assigned by sorting by extension, then filepath (or file?)
    """
    def __init__(self):
        self.ID = None
        self.filepath = None
        self.asset_type = None # Should be able to reconstruct this!!!
        self.unknown_id_1 = None
        self.unknown_id_2 = None
        
    def __repr__(self):
        return f"::Asset:: {self.asset_type} {self.unknown_id_1} {self.unknown_id_2} {self.filepath}"

class MXECInterface:
    def __init__(self):
        self.param_sets = []
        self.entities = []
        self.path_graphs = []
        self.assets = []
        
    def __repr__(self):
        return "::MXECInterface Object::\n"\
              f"{len(self.param_sets)} parameter sets.\n"\
              f"{len(self.entities)} entities.\n"\
              f"{len(self.path_graphs)} paths.\n"\
              f"{len(self.assets)} assets.\n"
    
    @classmethod
    def generate_param_interface(cls, mxec_rw, param_set):
        pi = ParameterInterface()
        pi.name = None
        pi.ID = None
        pi.param_type = None
        pi.parameters = {}
        for (key, value), dtype in zip(param_set.data.items(), param_set.datatypes):
            if dtype[1:] == "pad32" or dtype[1:] == "pad64":
                continue
            elif dtype[1:] == "sjis_string":
                try:
                    pi.parameters[key] = mxec_rw.sjis_strings.at_ptr(value)
                except Exception as e:
                    print(pi.param_type, key)
                    raise e
            elif dtype[1:] == "utf8_string":
                try:
                    pi.parameters[key] = mxec_rw.utf8_strings.at_ptr(value)
                except Exception as e:
                    print(pi.param_type, key)
                    raise e
            else:
                pi.parameters[key] = value
                
            pi.subparameters = {}
            for subparam_name, subparams in param_set.subparams.items():
                pi.subparameters[subparam_name] = []
                for subparam in subparams:
                    pi.subparameters[subparam_name].append(cls.generate_param_interface(mxec_rw, subparam))
        return pi
    
    @classmethod
    def from_subreader(cls, mxec_rw):
        instance = cls()
        
        for i, param_set in enumerate(mxec_rw.parameter_sets_table.entries):
            #assert param_set.ID == i, f"{param_set.ID} {i}"
            pi = cls.generate_param_interface(mxec_rw, param_set.data)
            str_name = mxec_rw.sjis_strings.at_ptr(param_set.name_offset).split(':')
            pi.name = str_name[-1]
            pi.ID = param_set.ID
            pi.param_type = param_set.data.struct_type
            
            instance.param_sets.append(pi)
        
        for entity in mxec_rw.entity_table.entries:
            ei = EntityInterface()
            ei.name = mxec_rw.sjis_strings.at_ptr(entity.name_offset)
            ei.ID = entity.ID
            ei.controller_id = entity.controller_entity_id
            if entity.unknown_data_ptr != 0:
                ei.unknown = mxec_rw.unknowns.at_ptr(entity.unknown_data_ptr)
                
                
            parameter_ids = iter(entity.data.data)
            ei.entity = EntityComponentInferface(mxec_rw.sjis_strings.at_ptr(entity.data.subentries[-1].name_offset))
            
            for canon_subentry, data_subentry in zip(ei.all_flat_entities()[::-1], entity.data.subentries):
                data_name_type = mxec_rw.sjis_strings.at_ptr(data_subentry.name_offset)
                if canon_subentry.type != data_name_type or len(ei.all_flat_entities()[::-1]) != len(entity.data.subentries):
                    all_canon_names = [ce.type for ce in ei.all_flat_entities()[::-1]]
                    all_data_names = [mxec_rw.sjis_strings.at_ptr(de.name_offset) for de in entity.data.subentries]
                    
                    print("ERROR: Mismatch between entity definition and data.")
                    print(all_canon_names)
                    print(all_data_names)
                    raise ValueError()
                    
                parameters = [next(parameter_ids) for _ in range(data_subentry.count)]
                for canon_param, data_param in zip(canon_subentry.parameters, parameters):
                    assert instance.param_sets[data_param].param_type == canon_param.type
                    canon_param.param_id = data_param
            instance.entities.append(ei)
            
        for path in mxec_rw.pathing_table.entries:
            pi = PathingInterface()
            pi.name = mxec_rw.sjis_strings.at_ptr(path.name_offset)
            
            nodes_in_use = [n_id for subgraph in path.graph_indices for n_id in subgraph.node_id_list]
            unique_node_ids = set(nodes_in_use)
            node_lookup = {v : i for i, v in enumerate(sorted(unique_node_ids))}
            for i, node in enumerate(path.graph_nodes):
                if node.next_edge_count or node.prev_edge_count or i in unique_node_ids:
                    ni = NodeInterface()
                    ni.param_id = node.node_param_id
                    ni.prev_edges = node.prev_edges
                    ni.next_edges = node.next_edges
                    pi.nodes.append(ni)
            for edge in path.graph_edges:
                ei = EdgeInterface()
                ei.edge_param_ids = edge.edge_param_ids
                ei.prev_node = edge.prev_node
                ei.next_node = edge.next_node
                pi.edges.append(ei)
            for graph_index in path.graph_indices:
                spi = SubpathInterface()
                spi.is_loop = graph_index.is_loop
                spi.node_ids = [node_lookup[id_] for id_ in graph_index.node_id_list]
                spi.edge_ids = graph_index.edge_id_list
            
            instance.path_graphs.append(pi)

        for asset_entry in sorted(mxec_rw.asset_table.entries, key=lambda entry: entry.ID):
            ai = AssetInterface()
            folder_name = mxec_rw.sjis_strings.at_ptr(asset_entry.folder_name_ptr)
            file_name   = mxec_rw.sjis_strings.at_ptr(asset_entry.file_name_ptr)
            
            ai.ID = asset_entry.ID
            ai.filepath = folder_name + "/" + file_name
            ai.asset_type = asset_entry.filetype
            ai.unknown_id_1 = asset_entry.unknown_0x14
            ai.unknown_id_2 = asset_entry.unknown_0x24
            
            instance.assets.append(ai)
            
        return instance

    def to_subreader(self, depth):
        ot = OffsetTracker()
        mxec_rw = MXECReadWriter(endianness=">")
        
        sjis_strings = set()
        utf8_strings = set()
        unknowns     = set()
        sjis_string_lookup = dict()
        utf8_string_lookup = dict()
        unknowns_lookup    = dict()
        
        # Execute this in FIVE passes:
        # 1) First, construct the data structures you need,
        #    find the offsets of major sections,
        #    and fill in offsets of major sections
        # 2) Next, actually fill in the main data in those structures
        # 3) Collect POF0 data
        # 4) Collect ENRS data
        # 5) Collect CCRS data
        
        ######################################################################
        #                               PASS 1                               #
        ######################################################################
        # Generate data structures (also create all needed offsets?)
        # Would it not be better to include offset-linkage automatically inside
        # the read/write function definition?
        # -> Would then allow to you run read/write in another mode: Offset-generator
        mxec_rw.header.read_write(ot)
        mxec_rw.rw_fileinfo(ot)
        
        # Do Parameters
        mxec_rw.parameter_sets_table.entry_count = len(self.param_sets)
        mxec_rw.parameter_sets_table_ptr = ot.tell() if len(self.param_sets) else 0
        mxec_rw.parameter_sets_table.entries.data = [mxec_rw.parameter_sets_table.entry_cls(mxec_rw.context) for _ in range(mxec_rw.parameter_sets_table.entry_count)]
        
        def collect_param_strings(prw, param_set):     
            sjis_strings.update(set([param_set.parameters[nm] for nm in prw.sjis_vars]))
            utf8_strings.update(set([param_set.parameters[nm] for nm in prw.utf8_vars]))
            
            if "subparams" in prw.struct_obj:
                for param_name, param_type in prw.struct_obj["subparams"].items():
                    count = len(param_set.subparameters[param_name])
                    prw.data[param_type["count"]] = count
                    param_set.parameters[param_type["count"]] = count
                    
                    prw.init_subparam(param_name, param_type)
                    for sub_prw, sub_param_set in zip(prw.subparams[param_name], param_set.subparameters[param_name]):
                        collect_param_strings(sub_prw, sub_param_set)
        
        # 1) INTERATE THROUGH ENTITIES
        # 2) CREATE ENTITY STACK FOR EACH PARAM LINKED TO AN ENTITY
        # 3) ACCUMULATE STRING
        # 4) ADD STRING TO ARRAY
        # 5) LOOK UP STRING IN ARRAY WHEN IT NEEDS TO BE LOOKED UP
        parameter_name_prefixes = {}
        for entity in self.entities:
            parameter_name_prefixes.update(entity.get_all_param_prefixes())
        
        print("Virtual params read, at", hex(ot.tell()))
        mxec_rw.parameter_sets_table.rw_fileinfo(ot)
        mxec_rw.parameter_sets_table.entry_ptr = ot.tell()
        
        param_names = []
        for i, param_set in enumerate(self.param_sets):
            type_prefix = param_set.param_type
            pset_name = ":".join([type_prefix, param_set.name])
            pset_name = parameter_name_prefixes.get(i, '') + pset_name
            sjis_strings.add(pset_name)
            param_names.append(pset_name)
        
        asset_offsets = []
        texmerge_offsets = []
        mxec_rw.parameter_sets_table.rw_entry_headers(ot)
        for param_set, prw in zip(self.param_sets, mxec_rw.parameter_sets_table.entries):
            prw.init_params(param_set.param_type)

            # Collect PVS, MergeFile, TextureMerge
            if param_set.param_type == "MxParameterPvs":
                if mxec_rw.pvs_record_ptr == 0:
                    mxec_rw.pvs_record_ptr = ot.tell()
                else:
                    assert 0, "More than one MxParameterPvs in MXE."
            elif param_set.param_type == "MxParameterMergeFile":
                if mxec_rw.mergefile_record_ptr == 0:
                    mxec_rw.mergefile_record_ptr = ot.tell()
                else:
                    assert 0, "More than one MxParameterMergeFile in MXE."
            elif param_set.param_type == "MxParameterTextureMerge":
                texmerge_offsets.append(ot.tell())

            # Get strings inside the parameters themselves
            collect_param_strings(prw.data, param_set)
            prw.data_offset = ot.tell()
            
            for pname, ptype in zip(prw.data.data, prw.data.datatypes):
                endianness, typecode = ptype[0], ptype[1:]
                if typecode == "asset":
                    asset_offsets.append(ot.tell())
                prw.data.rw_element(ot, typecode, pname, endianness)
            
            prw.data_size = ot.tell() - prw.data_offset
            # Now rw subreaders
            struct_obj = prw.data.struct_obj
            for subparam_name, subparam_def in struct_obj.get("subparams", {}).items():
                prw.data.data[subparam_def["pointer"]] = ot.tell()
                param_set.parameters[subparam_def["pointer"]] = ot.tell()               
                prw.data.rw_subparam(ot, subparam_name, subparam_def)
            ot.align(ot.tell(), 0x10)
        
        ot.align(ot.tell(), 0x10)
        
        # Do Entities
        mxec_rw.entity_table_ptr = ot.tell() if len(self.entities) else 0
        if len(self.entities):
            mxec_rw.entity_table.entry_count = len(self.entities)
            mxec_rw.entity_table.entries.data = [EntityEntry(mxec_rw.context) for _ in range(mxec_rw.entity_table.entry_count)]
            
            ot.rw_obj_method(mxec_rw.entity_table, mxec_rw.entity_table.rw_fileinfo)
            mxec_rw.entity_table.entry_ptr = ot.tell()
            ot.rw_obj_method(mxec_rw.entity_table, mxec_rw.entity_table.rw_entry_headers)
            for i, (entity_rw, entity) in enumerate(zip(mxec_rw.entity_table.entries, self.entities)):
                sjis_strings.add(entity.name)
                entity_rw.data_offset = ot.tell()
                entity_rw.count = len(entity.all_flat_entities())
                
                if entity.unknown is not None:
                    unknowns.add(entity.unknown)
                    
                entity_rw.data = EntityData(entity_rw.count, entity_rw.context)
                entity_rw.data.subentries.data = [EntitySubEntry(entity_rw.data.context) for _ in range(entity_rw.count)]
                
                #ot.rw_obj_method(entity_rw.data, entity_rw.data.read_write)
                ot.rw_obj_method(entity_rw.data.subentries, entity_rw.data.subentries.read_write)
                
                entity_rw.data.data.data = []
                idx = 0
                ref_offset = ot.tell()
                
                for dec_rw, dec in zip(entity_rw.data.subentries, entity.all_flat_entities()[::-1]):
                    entity_rw.data.data.data.extend([0]*len(dec.parameters))
                    sjis_strings.add(dec.type)
                    dec_rw.count = len(dec.parameters)
                    dec_rw.offset = (ref_offset + idx*4) if dec_rw.count else 0

                    idx += dec_rw.count
                
                ot.rw_obj_method(entity_rw.data.data, entity_rw.data.data.read_write)
            
        ot.align(ot.tell(), 0x10)
        
        # Do Paths
        mxec_rw.pathing_table_ptr = ot.tell() if len(self.path_graphs) else 0
        
        # Do Assets
        mxec_rw.asset_table_ptr = ot.tell() if len(self.assets) else 0
        if len(self.assets):
            ot.rw_obj_method(mxec_rw.asset_table, mxec_rw.asset_table.rw_fileinfo)
            mxec_rw.asset_table.asset_references_offset = ot.tell()
            mxec_rw.asset_table.asset_references_count = len(self.assets)
            mxec_rw.asset_table.init_structs()
            ot.rw_obj_method(mxec_rw.asset_table, mxec_rw.asset_table.rw_entry_headers)
            for asset in self.assets:
                folder_name, file_name = asset.filepath.rsplit('/', 1)
                sjis_strings.add(folder_name)
                sjis_strings.add(file_name)
            
            mxec_rw.asset_table.asset_use_offset = ot.tell()
            mxec_rw.asset_table.asset_use_count = len(asset_offsets)
            ot.rw_obj_method(mxec_rw.asset_table, mxec_rw.asset_table.rw_asset_slot_offsets)

        # Do texmerge ptrs
        if len(texmerge_offsets):
            mxec_rw.texmerge_ptrs_ptr = ot.tell()
            mxec_rw.texmerge_ptr = texmerge_offsets
            mxec_rw.texmerge_count = len(texmerge_offsets)
        ot.align(ot.tell(), 0x10)
        
        # Do Strings
        for i, string_val in enumerate(sorted(sjis_strings)):
            str_bytes = string_val.encode("cp932")
            offset = ot.tell()
            sjis_string_lookup[string_val] = offset
            ot.seek(offset + len(str_bytes) + 1)
        ot.align(ot.tell(), 0x10)
        for i, string_val in enumerate(sorted(utf8_strings)):
            str_bytes = string_val.encode("utf8")
            offset = ot.tell()
            utf8_string_lookup[string_val] = offset
            ot.seek(offset + len(str_bytes) + 1)
        ot.align(ot.tell(), 0x10)
        
        # Do Unknowns
        for i, unknowns_val in enumerate(sorted(unknowns, key=lambda x: struct.unpack('<Q', struct.pack('>Q', x)))):
            offset = ot.tell()
            unknowns_lookup[unknowns_val] = offset
            ot.seek(offset + 8)
        ot.align(ot.tell(), 0x10)
        
        
        # Clean up header
        mxec_rw.header.flags = 0x18000000
        mxec_rw.header.data_length = ot.tell() - mxec_rw.header.header_length
        mxec_rw.header.depth = depth
        
        mxec_rw.content_flags +=                                  1 * 0x00000100
        mxec_rw.content_flags +=    (mxec_rw.texmerge_ptrs_ptr > 0) * 0x00000400
        mxec_rw.content_flags +=       (mxec_rw.pvs_record_ptr > 0) * 0x00001800
        mxec_rw.content_flags += (mxec_rw.mergefile_record_ptr > 0) * 0x01000000
        
        ######################################################################
        #                               PASS 2                               #
        ######################################################################
        # Fill in data
        
        # Fill in Parameter Sets
        def fill_param_strings(prw, param_set, sjis_lookup, utf8_lookup):
            for param_name, param_type in zip(prw.data.data, prw.data.datatypes):
                if type(param_type) is str:
                    if param_type[1:] == "sjis_string":
                        prw.data.data[param_name] = sjis_lookup[param_set.parameters[param_name]]
                    elif param_type[1:] == "utf8_string":
                        prw.data.data[param_name] = utf8_lookup[param_set.parameters[param_name]]
                    elif param_type[1:] == "pad32" or param_type[1:] == "pad64":
                        prw.data.data[param_name] = 0
                    elif param_type[1:] == "pointer":
                        pass # Should have already been handled
                    else:
                        prw.data.data[param_name] = param_set.parameters[param_name]
                elif type(param_type) is dict:
                    for sub_prw, sub_param_set in zip(prw.data[param_name], param_set.parameters[param_name]):
                        fill_param_strings(sub_prw, sub_param_set, sjis_lookup, utf8_lookup)
        
        for i, (prw, param_set, param_set_name) in enumerate(zip(mxec_rw.parameter_sets_table.entries, self.param_sets, param_names)):
            prw.ID = i
            prw.name_offset = sjis_string_lookup[param_set_name]
            fill_param_strings(prw, param_set, sjis_string_lookup, utf8_string_lookup)
            
        # Entities
        for entity_rw, entity in zip(mxec_rw.entity_table.entries, self.entities):
            entity_rw.ID = entity.ID
            entity_rw.name_offset = sjis_string_lookup[entity.name]
            entity_rw.controller_entity_id = entity.controller_id
            entity_rw.has_unknown_data     = (entity.unknown is not None)
            entity_rw.unknown_data_ptr = unknowns_lookup[entity.unknown] if entity_rw.has_unknown_data else 0
            
            idx = 0
            for dec_rw, dec in zip(entity_rw.data.subentries, entity.all_flat_entities()[::-1]):
                dec_rw.name_offset = sjis_string_lookup[dec.type]
                for param in dec.parameters:
                    entity_rw.data.data.data[idx] = param.param_id
                    idx += 1
        # Paths
        
        # Assets
        for i, asset in enumerate(self.assets):
            entry = mxec_rw.asset_table.entries[i]
            folder_name, file_name = asset.filepath.rsplit('/', 1)
            
            entry.flags           = 0x100 * (asset.unknown_id_1 > 0) + 0x200 * (asset.unknown_id_2 > 0)
            entry.ID              = i
            entry.folder_name_ptr = sjis_string_lookup[folder_name]
            entry.file_name_ptr   = sjis_string_lookup[file_name]
            entry.filetype        = asset.asset_type
            
            entry.unknown_0x14    = asset.unknown_id_1
            entry.unknown_0x20    = (asset.unknown_id_1 > 0) - 1
            entry.unknown_0x24    = asset.unknown_id_2
            
        mxec_rw.asset_table.asset_slot_offsets = asset_offsets
            
        # Strings
        for string_val, offset in sjis_string_lookup.items():
            idx = len(mxec_rw.sjis_strings)
            mxec_rw.sjis_strings.data.append(string_val)
            mxec_rw.sjis_strings.ptr_to_idx[offset] = idx
            mxec_rw.sjis_strings.idx_to_ptr[idx] = offset
        for string_val, offset in utf8_string_lookup.items():
            idx = len(mxec_rw.utf8_strings)
            mxec_rw.utf8_strings.data.append(string_val)
            mxec_rw.utf8_strings.ptr_to_idx[offset] = idx
            mxec_rw.utf8_strings.idx_to_ptr[idx] = offset
        
        
        # Unknowns
        for unknown, offset in unknowns_lookup.items():
            idx = len(mxec_rw.unknowns)
            mxec_rw.unknowns.data.append(unknown)
            mxec_rw.unknowns.ptr_to_idx[offset] = idx
            mxec_rw.unknowns.idx_to_ptr[idx] = offset
            
        
        ######################################################################
        #                               PASS 3                               #
        ######################################################################
        # POF0
        
        # Create POF0 data
        pb = POF0Builder()
        pb.virtual_offset = mxec_rw.header.header_length
        mxec_rw.read_write_contents(pb)
        
        pb_data = compressPOF0(pb.pointers)
        mxec_rw.POF0.data_size = len(pb_data) + 4
        mxec_rw.POF0.data = pb_data
        
        # Create POF0 header data
        pb_ot = OffsetTracker()
        mxec_rw.POF0.read_write_contents(pb_ot)
        
        mxec_rw.POF0.header.flags = 0x10000000
        mxec_rw.POF0.header.depth = depth + 1
        mxec_rw.POF0.header.data_length = pb_ot.tell()
        mxec_rw.POF0.header.contents_length = pb_ot.tell()
        
        mxec_rw.POF0.read_write(ot)
        
        ######################################################################
        #                               PASS 4                               #
        ######################################################################
        # ENRS
        # Create POF0 data
        eb = ENRSBuilder(mxec_rw.context.endianness)
        eb.anchor_pos = -mxec_rw.header.header_length
        mxec_rw.read_write_contents(eb)
        
        eb_rawdata = toENRSPackedRep(eb.pointers)
        eb_data = compressENRS(eb_rawdata)
        mxec_rw.ENRS.num_groups = len(eb.pointers)
        mxec_rw.ENRS.data = eb_data
        
        # Create ENRS header data
        mxec_rw.ENRS.header.data_length = len(eb_data) + 0x10
        mxec_rw.ENRS.header.contents_length = len(eb_data) + 0x10
        
        mxec_rw.ENRS.header.flags = 0x10000000
        mxec_rw.ENRS.header.depth = depth + 1
        
        mxec_rw.ENRS.read_write(ot)
        
        ######################################################################
        #                               PASS 5                               #
        ######################################################################
        # CCRS
        cb = CCRSBuilder()
        cb.anchor_pos = -mxec_rw.header.header_length
        mxec_rw.read_write_contents(cb)
        
        cb_rawdata = toCCRSPackedRep(cb.pointers)
        cb_data = compressCCRS(cb_rawdata)
        mxec_rw.CCRS.num_groups = len(cb.pointers)
        mxec_rw.CCRS.data = cb_data
        
        # Create CCRS header data
        mxec_rw.CCRS.header.data_length = len(cb_data) + 0x10
        mxec_rw.CCRS.header.contents_length = len(cb_data) + 0x10
        
        mxec_rw.CCRS.header.flags = 0x10000000
        mxec_rw.CCRS.header.depth = depth + 1
        
        mxec_rw.CCRS.read_write(ot)
        
        ######################################################################
        #                              CLEANUP                               #
        ######################################################################
        # Finish with EOFC
        mxec_rw.EOFC.header.flags           = 0x10000000
        mxec_rw.EOFC.header.depth           = depth + 1
        mxec_rw.EOFC.header.data_length     = 0
        mxec_rw.EOFC.header.contents_length = 0
        
        mxec_rw.header.contents_length = ot.tell()
        
        return mxec_rw
