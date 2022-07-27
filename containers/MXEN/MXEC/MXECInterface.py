from collections import defaultdict
import os

from .MXECReadWriter import MXECReadWriter
from .AssetEntry import AssetEntry
from pyValkLib.serialisation.ReadWriter import OffsetTracker, POF0Builder, ENRSBuilder, CCRSBuilder
from pyValkLib.containers.POF0.POF0ReadWriter import compressPOF0
from pyValkLib.containers.ENRS.ENRSReadWriter import compressENRS
from pyValkLib.containers.CCRS.CCRSReadWriter import compressCCRS, toCCRSPackedRep

class ParameterInterface:
    def __init__(self):
        self.name = None
        self.ID = None
        self.param_type = None
        self.parameters = None
        self.subparameters = None
        
class EntityInterface:
    def __init__(self):
        self.name = None
        self.unknown = None
        self.controller_id = None
        self.subcomponents = []
        
class EntityComponentInterface:
    def __init__(self):
        self.name = None
        self.ID = None
        self.subcomponents = []

class NodeInterface:
    def __init__(self):
        self.param_id = None
        self.prev_edges = []
        self.next_edges = []
        
class EdgeInterface:
    def __init__(self):
        self.edge_param_ids = []
        self.prev_node = None
        self.next_node = None

class SubpathInterface:
    def __init__(self):
        self.is_loop = False
        self.node_ids = []
        self.edge_ids = []
        
class PathingInterface:
    def __init__(self):
        self.name = None
        self.nodes = []
        self.edges = []
        
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
    def from_subreader(cls, mxec_rw):
        instance = cls()
        
        for i, param_set in enumerate(mxec_rw.parameter_sets_table.entries):
            assert param_set.ID == i, f"{param_set.ID} {i}"
            pi = ParameterInterface()
            str_name = mxec_rw.sjis_strings.at_ptr(param_set.name_offset).split(':')
            pi.name = str_name[-1]
            pi.ID = param_set.ID
            pi.param_type = param_set.data.struct_type
            pi.parameters = {}
            for (key, value), dtype in zip(param_set.data.data.items(), param_set.data.datatypes):
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
            for subparam_name, subparams in param_set.data.subparams.items():
                pi.subparameters[subparam_name] = subparams
                
            instance.param_sets.append(pi)
            
        for entity in mxec_rw.entity_table.entries:
            ei = EntityInterface()
            ei.name = mxec_rw.sjis_strings.at_ptr(entity.name_offset)
            ei.ID = entity.ID
            ei.controller_id = entity.controller_entity_id
            if entity.unknown_data_ptr != 0:
                ei.unknown = mxec_rw.unknowns.at_ptr(entity.unknown_data_ptr)
                
                
            parameter_ids = iter(entity.data.data)
            for subentry in entity.data.subentries:
                parameters = [next(parameter_ids) for _ in range(subentry.count)]
                ei.subcomponents.append((mxec_rw.sjis_strings.at_ptr(subentry.name_offset), parameters ))
            instance.entities.append(ei)
            
            # Next assign the components of each entity 
            
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
        sjis_string_lookup = dict()
        utf8_string_lookup = dict()
        
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
        mxec_rw.header.read_write(ot)
        mxec_rw.rw_fileinfo(ot)
        
        # Do Parameters
        mxec_rw.parameter_sets_table.entry_count = len(self.param_sets)
        mxec_rw.parameter_sets_table_ptr = ot.tell() if len(self.param_sets) else 0
        mxec_rw.parameter_sets_table.entries.data = [mxec_rw.parameter_sets_table.entry_cls(mxec_rw.context) for _ in range(mxec_rw.parameter_sets_table.entry_count)]
        
        def collect_param_strings(prw, param_set):
            sjis_strings.update(set([param_set.parameters[nm] for nm in prw.data.sjis_vars]))
            utf8_strings.update(set([param_set.parameters[nm] for nm in prw.data.utf8_vars]))
            for param_name, param_type in zip(prw.data.data, prw.data.datatypes):
                # Replace with loop over subparameters...
                if type(param_type) is dict:
                    count = len(param_set.parameters[param_name])
                    prw.data.data[param_type["count"]] = count
                    param_set.parameters[param_type["count"]] = count
                    
                    prw.init_subparam(param_name, param_type)
                    for sub_prw, sub_param_set in zip(prw.data[param_name], param_set.parameters[param_name]):
                        collect_param_strings(sub_prw, sub_param_set)
        
        mxec_rw.parameter_sets_table.rw_fileinfo(ot)
        mxec_rw.parameter_sets_table.entry_ptr = ot.tell()
        
        param_names = []
        for i, param_set in enumerate(self.param_sets):
            type_prefix = param_set.param_type
            pset_name = ":".join([type_prefix, param_set.name])
            
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
            collect_param_strings(prw, param_set)
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
                prw.data.data[subparam_def["ptr"]] = ot.tell()
                param_set.parameters[subparam_def["ptr"]] = ot.tell()
                prw.rw_subparam(ot, subparam_name, subparam_def)
            ot.align(ot.tell(), 0x10)
        
        ot.align(ot.tell(), 0x10)
        
        # Do Entities
        mxec_rw.entity_table_ptr = ot.tell() if len(self.entities) else 0
        
        # Do Paths
        mxec_rw.pathing_table_ptr = ot.tell() if len(self.path_graphs) else 0
        
        # Do Assets
        mxec_rw.asset_table_ptr = ot.tell() if len(self.assets) else 0
        ot.rw_obj_method(mxec_rw.asset_table, mxec_rw.asset_table.rw_fileinfo)
        mxec_rw.asset_table.asset_references_offset = ot.tell()
        mxec_rw.asset_table.asset_references_count = len(self.assets)
        mxec_rw.asset_table.init_structs()
        ot.rw_obj_method(mxec_rw.asset_table, mxec_rw.asset_table.rw_entry_headers)
        
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
        
        # Clean up header
        mxec_rw.header.flags = 0x18000000
        mxec_rw.header.data_length = ot.tell() - mxec_rw.header.header_length
        mxec_rw.header.depth = depth
        
        mxec_rw.content_flags +=                                  1 * 0x00000100
        mxec_rw.content_flags +=    (mxec_rw.texmerge_ptrs_ptr > 0) * 0x00000400
        mxec_rw.content_flags +=       (mxec_rw.pvs_record_ptr > 0) * 0x00001800
        mxec_rw.content_flags += (mxec_rw.mergefile_record_ptr > 0) * 0x01000000
        
        print(mxec_rw.content_flags)
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
        
        for prw, param_set, param_set_name in zip(mxec_rw.parameter_sets_table.entries, self.param_sets, param_names):
            prw.name_offset = sjis_string_lookup[param_set_name]
            fill_param_strings(prw, param_set, sjis_string_lookup, utf8_string_lookup)
            
        # Entities
        
        # Paths
        
        # Assets
        for i, asset in enumerate(self.assets):
            entry = mxec_rw.asset_table.entries[i]
            
            entry.flags           = 0x100 * (asset.unknown_id_1 > 0) + 0x200 * (asset.unknown_id_2 > 0)
            entry.ID              = i
            entry.folder_name_ptr,\
            entry.file_name_ptr   = asset.filepath.rsplit('/', 1)
            entry.filetype        = asset.asset_type
            
            entry.unknown_0x14    = asset.unknown_id_1
            entry.unknown_0x20    = (asset.unknown_id_1 > 0) - 1
            entry.unknown_0x24    = asset.unknown_id_2
            
        mxec_rw.asset_table.asset_offsets = asset_offsets
            
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
        ot.align(ot.tell(), 0x10)
        
        # Unknowns
        # Already handled
            
        
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
        
        eb_data = compressENRS(eb.pointers)
        eb_data += [0]*((0x10 - len(eb_data) % 0x10) % 0x10)
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
        cb_data += [0]*((0x10 - len(cb_data) % 0x10) % 0x10)
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
        
        mxec_rw.header.contents_length = ot.tell() - mxec_rw.header.header_length
        
        return mxec_rw
