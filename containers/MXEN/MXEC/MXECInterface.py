import os

from .MXECReadWriter import MXECReadWriter
from .AssetEntry import AssetEntry
from pyValkLib.serialisation.ReadWriter import OffsetTracker

class ParameterInterface:
    def __init__(self):
        self.name = None
        self.ID = None
        self.param_type = None
        self.parameters = None
        
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
              f"{len(self.batch_renders)} paths.\n"\
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
                if type(dtype) is str:
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
                else:
                    pi.parameters[key] = value
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

    def to_subreader(self):
        ot = OffsetTracker()
        mxec_rw = MXECReadWriter(endianness='>')
        
        # Init the variables we'll need to track as we perform the build
        sjis_strings = set()
        utf8_strings = set()
        
        # Will have to complete the header after the file data is sorted out
        # ...as well as a bunch of pointers
        mxec_rw.header.flags = 0x18000000
        
        # Fill in with dummy values for now
        mxec_rw.content_flags            = 0
        mxec_rw.parameter_sets_table_ptr = None
        mxec_rw.entity_table_ptr         = None
        mxec_rw.asset_table_ptr          = None
        
        mxec_rw.unknown_0x30             = 1
        mxec_rw.pathing_table_ptr        = None
        mxec_rw.texmerge_count           = 0
        mxec_rw.texmerge_ptrs_ptr        = 0
        
        mxec_rw.pvs_record_ptr           = 0
        mxec_rw.mergefile_record_ptr     = 0
        
        mxec_rw.rw_fileinfo(ot)
        
        # Create the parameter table
        mxec_rw.parameter_sets_table_ptr = ot.tell() if len(self.param_sets) else 0
        #self.make_params_table(ot, mxec_rw, sjis_strings, utf8_strings)
        #self.make_string_banks(sjis_strings, utf8_strings)
        
        return mxec_rw
    
    def make_params_table(self, ot, mxec_rw, sjis_strings, utf8_strings):
        # Skip to end of fileinfo
        mxec_rw.parameter_sets_table.entry_ptr = ot.tell()
        ot.rw_obj_method(mxec_rw.parameter_sets_table, mxec_rw.parameter_sets_table.rw_fileinfo)

        # Fill in fileinfo pointer
        mxec_rw.parameter_sets_table.entry_count = len(self.param_sets)
        mxec_rw.parameter_sets_table.entries.data = [mxec_rw.parameter_sets_table.entry_cls(mxec_rw.context) for _ in range(mxec_rw.parameter_sets_table.entry_count)]
        
        # Write headers?
        for param_set, prw in zip(self.param_sets, mxec_rw.parameter_sets_table.entries):
            type_prefix = param_set.param_type # Needs to have full entity string etc.
            sjis_strings.add(":".join([type_prefix, param_set.name]))
            
            # Fill in the structure
            prw.init_params(param_set.param_type)
            prw.ID          = param_set.ID
            prw.name_offset = None
            prw.data_size   = None
            prw.data_offset = None
            
            # Fill in the parameter data
            for param_name, param_type in zip(prw.data.data, prw.data.datatypes):
                if type(param_type) is str:
                    if param_type[1:] == "pad32" or param_type[1:] == "pad64":
                        prw.data.data[param_name] = 0
                    elif param_type[1:] == "sjis_string":
                        sjis_strings.add(param_set.parameters[param_name])
                        prw.data.data[param_name] = None
                    elif param_type[1:] == "utf8_string":
                        utf8_strings.add(param_set.parameters[param_name])
                        prw.data.data[param_name] = None
                    else:
                        prw.data.data[param_name] = param_set.parameters[param_name]
                elif type(param_type) is dict:
                    prw.data[param_name].count = len(param_set[param_name])
                    prw.data[param_name].ptr = None
                else:
                    raise Exception(f"Unrecognised parameter type {type(param_type)}.")
            
            prw.data.init_subparams()
                
        # Advance the pointer beyond the headers
        ot.rw_obj_method(mxec_rw.parameter_sets_table, mxec_rw.parameter_sets_table.rw_entry_headers)
        # Now get important pointers from within the parameter sets themselves
        for prw in mxec_rw.parameter_sets_table.entries:
            # Fill in Header data
            if prw.data.struct_type == "MxParameterTextureMerge":
               # If texmerge, fill in ptr...
                ...
            elif prw.data.struct_type == "MxParameterPvs":
                # If pvs, fill in ptr...
                ...
            elif prw.data.struct_type == "MxParameterMergeFile":
                ...
                # If mergefile, fill in ptr...
            
            ot.rw_obj_method(prw, prw.rw_data, None)
        #ot.rw_obj_method(self.parameter_sets_table, self.parameter_sets_table.rw_entries)
        
        
        
        
        
    def make_asset_table(self):
        ...
        # # Write out assets
        # mxec_rw.asset_table.padding_0x00 = 0
        # mxec_rw.asset_table.asset_reference_count = len(self.assets)
        # mxec_rw.asset_table.asset_use_count = None
        # mxec_rw.asset_table.padding_0x14 = 0
        # mxec_rw.asset_table.padding_0x18 = 0
        # mxec_rw.asset_table.padding_0x1C = 0
        
        # # Make sure pointer is updated
        # mxec_rw.asset_table.asset_references_offset = virtual_pointer
        # # Handle asset entries
        # for asset_entry in self.assets:
        #     # Need to sort out the pointers here
        #     ae = AssetEntry()
            
        #     ae.flags = 0x100 * (asset_entry.unknown_id_1 != -1) + 0x200 * (asset_entry.unknown_id_2 != -1)
        #     ae.ID = asset_entry.ID
        #     ae.folder_name_ptr, ae.file_name_ptr = os.path.split(asset_entry.filepath)
            
        #     ae.filetype = asset_entry.filetype
        #     ae.unknown_0x14 = asset_entry.unknown_id_1
        #     ae.unknown_0x18 = 0
        #     ae.padding_0x1C = 0
            
        #     ae.unknown_0x20 = (asset_entry.unknown_id_2 > -1) - 1
        #     ae.unknown_0x24 = asset_entry.unknown_id_2
        #     ae.padding_0x28 = 0
        #     ae.padding_0x2C = 0
            
        #     ae.padding_0x30 = 0
        #     ae.padding_0x34 = 0
        #     ae.padding_0x38 = 0
        #     ae.padding_0x3C = 0   
            
        #     mxec_rw.asset_table.entries.data.append(ae)

        # # Make sure pointer is updated
        # mxec_rw.asset_table.asset_use_offset = virtual_pointer
        # # Now need to loop over an array of pointers constructed from the parameters...
        
    def make_string_banks(self, sjis_strings, utf8_strings):
        ...