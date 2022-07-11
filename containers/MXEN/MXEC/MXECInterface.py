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
            str_name = mxec_rw.strings.at_ptr(param_set.name_offset).split(':')
            pi.name = str_name[-1]
            pi.ID = param_set.ID
            pi.param_type = param_set.data.struct_type
            pi.parameters = {}
            for (key, value), dtype in zip(param_set.data.data.items(), param_set.data.datatypes):
                if type(dtype) is str:
                    if dtype[1:] == "pad32" or dtype[1:] == "pad64":
                        continue
                    elif dtype[1:] == "sjis_string" or dtype[1:] == "utf8_string":
                        pi.parameters[key] = mxec_rw.strings.at_ptr(value)
                    else:
                        pi.parameters[key] = value
                else:
                    pi.parameters[key] = value
            instance.param_sets.append(pi)
            
        for entity in mxec_rw.entity_table.entries:
            ei = EntityInterface()
            ei.name = mxec_rw.strings.at_ptr(entity.name_offset)
            ei.ID = entity.ID
            ei.controller_id = entity.controller_entity_id
            if entity.unknown_data_ptr != 0:
                ei.unknown = mxec_rw.unknowns.at_ptr(entity.unknown_data_ptr)
                
                
            parameter_ids = iter(entity.data.data)
            for subentry in entity.data.subentries:
                parameters = [next(parameter_ids) for _ in range(subentry.count)]
                ei.subcomponents.append((mxec_rw.strings.at_ptr(subentry.name_offset), parameters ))
            instance.entities.append(ei)
            
            # Next assign the components of each entity 
            
        for path in mxec_rw.pathing_table.entries:
            pi = PathingInterface()
            pi.name = mxec_rw.strings.at_ptr(path.name_offset)
            
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
            folder_name = mxec_rw.strings.at_ptr(asset_entry.folder_name_ptr)
            file_name   = mxec_rw.strings.at_ptr(asset_entry.file_name_ptr)
            
            ai.ID = asset_entry.ID
            ai.filepath = folder_name + "/" + file_name
            ai.asset_type = asset_entry.filetype
            ai.unknown_id_1 = asset_entry.unknown_0x14
            ai.unknown_id_2 = asset_entry.unknown_0x24
            
            instance.assets.append(ai)
            
        return instance

    def to_subreader(self):
        pass
