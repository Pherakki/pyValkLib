from pyValkLib.serialisation.Serializable import Serializable
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray


class PathingEntry(Serializable):
    __slots__ = ("name_offset", "graph_edges", "unused_nodes",
                 "node_count", "nodes_offset", "graph_nodes",
                 "edge_count", "edges_offset", "t2_data",
                 "graph_index_count", "graph_indices_offset", "graph_indices",
                 "unused_node_count", "unused_nodes_offset", "t4_data",
                 "padding_0x24", "padding_0x28", "padding_0x2C",
                 "padding_0x30", "padding_0x34", "padding_0x38", "padding_0x3C")

    def __init__(self, context):
        super().__init__(context)
        self.name_offset = 0
        self.node_count  = 0
        self.nodes_offset = 0
        self.edge_count  = 0
        self.edges_offset = 0
        self.graph_index_count  = 0
        self.graph_indices_offset = 0
        self.unused_node_count  = 0
        self.unused_nodes_offset = 0
        
        self.padding_0x24 = 0
        self.padding_0x28 = 0
        self.padding_0x2C = 0
        
        self.padding_0x30 = 0
        self.padding_0x34 = 0
        self.padding_0x38 = 0
        self.padding_0x3C = 0

        self.graph_nodes = []
        self.graph_edges = []
        self.graph_indices = [] # Will always be 1 or 0?
        self.unused_nodes = []

    def read_write(self, rw):
        self.name_offset  = rw.rw_pointer(self.name_offset)
        self.node_count   = rw.rw_uint32(self.node_count)
        self.nodes_offset = rw.rw_pointer(self.nodes_offset)
        self.edge_count   = rw.rw_uint32(self.edge_count)
        
        self.edges_offset         = rw.rw_pointer(self.edges_offset)
        self.graph_index_count    = rw.rw_uint32(self.graph_index_count)
        self.graph_indices_offset = rw.rw_pointer(self.graph_indices_offset)
        self.unused_node_count    = rw.rw_uint32(self.unused_node_count)
        
        self.unused_nodes_offset    = rw.rw_pointer(self.unused_nodes_offset)
        self.padding_0x24 = rw.rw_pad32(self.padding_0x24)
        self.padding_0x28 = rw.rw_pad32(self.padding_0x28)
        self.padding_0x2C = rw.rw_pad32(self.padding_0x2C)
        
        self.padding_0x30 = rw.rw_pad32(self.padding_0x30)
        self.padding_0x34 = rw.rw_pad32(self.padding_0x34)
        self.padding_0x38 = rw.rw_pad32(self.padding_0x38)
        self.padding_0x3C = rw.rw_pad32(self.padding_0x3C)

        rw.assert_is_zero(self.padding_0x24)
        rw.assert_is_zero(self.padding_0x28)
        rw.assert_is_zero(self.padding_0x2C)
        
        rw.assert_is_zero(self.padding_0x30)
        rw.assert_is_zero(self.padding_0x34)
        rw.assert_is_zero(self.padding_0x38)
        rw.assert_is_zero(self.padding_0x3C)

    def rw_data(self, rw):
        if self.nodes_offset:
            rw.assert_local_file_pointer_now_at("Node Headers:", self.nodes_offset)
            rw.rw_obj_method(self, self.rw_nodes)

        if self.edges_offset:
            rw.assert_local_file_pointer_now_at("Edge Headers:", self.edges_offset)
            rw.rw_obj_method(self, self.rw_edges)

        for node in self.graph_nodes:
            if node.next_edge_list_offset:
                rw.assert_local_file_pointer_now_at("Node Next Edges:", node.next_edge_list_offset)
                rw.rw_obj_method(node, node.rw_next_edge_ids)
            if node.prev_edge_list_offset:
                rw.assert_local_file_pointer_now_at("Node Prev Edges:", node.prev_edge_list_offset)
                rw.rw_obj_method(node, node.rw_prev_edge_ids)

        for edge in self.graph_edges:
            if edge.param_list_offset:
                rw.assert_local_file_pointer_now_at("Graph Edge Parameter List:", edge.param_list_offset)
                rw.rw_obj_method(edge, edge.rw_param_ids)

        rw.align(rw.local_tell(), 0x10)

        if self.graph_indices_offset:
            rw.assert_local_file_pointer_now_at("Graph Indices:", self.graph_indices_offset)
            rw.rw_obj_method(self, self.rw_graph_indices)
            for graph_index in self.graph_indices:
                if graph_index.node_list_offset:
                    rw.assert_local_file_pointer_now_at("Graph Index Nodes:", graph_index.node_list_offset)
                rw.rw_obj_method(graph_index, graph_index.rw_node_id_list)
                if graph_index.edge_list_offset:
                    rw.assert_local_file_pointer_now_at("Graph Index Edges:", graph_index.edge_list_offset)
                rw.rw_obj_method(graph_index, graph_index.rw_edge_id_list)
                if graph_index.start_node_offset:
                    rw.assert_local_file_pointer_now_at("Graph Index Start Nodes:", graph_index.start_node_offset)
                rw.rw_obj_method(graph_index, graph_index.rw_start_node_ids)
                if graph_index.end_node_offset:
                    rw.assert_local_file_pointer_now_at("Graph Index End Nodes:", graph_index.end_node_offset)
                rw.rw_obj_method(graph_index, graph_index.rw_end_node_ids)

        if self.unused_nodes_offset:
            rw.assert_local_file_pointer_now_at("Unused Graph Nodes:", self.unused_nodes_offset)
            rw.rw_obj_method(self, self.rw_unused_nodes)

        rw.align(rw.local_tell(), 0x10)

    def rw_nodes(self, rw):
        if rw.mode() == "read":
            self.graph_nodes = [PathNode(self.context) for _ in range(self.node_count)]
        for node in self.graph_nodes:
            rw.rw_obj(node)

    def rw_edges(self, rw):
        if rw.mode() == "read":
            self.graph_edges = [PathEdge(self.context) for _ in range(self.edge_count)]
        for edge in self.graph_edges:
            rw.rw_obj(edge)

    def rw_graph_indices(self, rw):
        if rw.mode() == "read":
            self.graph_indices = [GraphIndex(self.context) for _ in range(self.graph_index_count)]
        for graph_index in self.graph_indices:
            rw.rw_obj(graph_index)

    def rw_unused_nodes(self, rw):
        self.unused_nodes = rw.rw_uint32s(self.unused_nodes, self.unused_node_count)

        
class PathNode(Serializable):
    def __init__(self, endianness):
        super().__init__(endianness)
        
        self.next_edge_count       = 0
        self.next_edge_list_offset = 0
        self.prev_edge_count       = 0
        self.prev_edge_list_offset = 0
        self.node_param_id = 0
        self.padding_0x14  = 0
        self.padding_0x18  = 0
        self.padding_0x1C  = 0
        
        self.next_edges = []
        self.prev_edges = []

    def read_write(self, rw):
        self.next_edge_count       = rw.rw_uint32(self.next_edge_count)
        self.next_edge_list_offset = rw.rw_pointer(self.next_edge_list_offset)
        self.prev_edge_count       = rw.rw_uint32(self.prev_edge_count)
        self.prev_edge_list_offset = rw.rw_pointer(self.prev_edge_list_offset)
        
        self.node_param_id = rw.rw_uint32(self.node_param_id)
        self.padding_0x14  = rw.rw_pad32(self.padding_0x14)
        self.padding_0x18  = rw.rw_pad32(self.padding_0x18)
        self.padding_0x1C  = rw.rw_pad32(self.padding_0x1C)
        
        rw.assert_is_zero(self.padding_0x14)
        rw.assert_is_zero(self.padding_0x18)
        rw.assert_is_zero(self.padding_0x1C)
        
    def rw_next_edge_ids(self, rw):
        rw.assert_local_file_pointer_now_at("PathNode: Previous Edges: ", self.next_edge_list_offset)
        self.next_edges = rw.rw_uint32s(self.next_edges, self.next_edge_count)
        
    def rw_prev_edge_ids(self, rw):
        rw.assert_local_file_pointer_now_at("PathNode: Next Edges:", self.prev_edge_list_offset)
        self.prev_edges = rw.rw_uint32s(self.prev_edges, self.prev_edge_count)
        

class PathEdge(Serializable):
    def __init__(self, endianness):
        super().__init__(endianness)
        
        self.prev_node     = 0
        self.next_node         = 0
        self.param_count       = 0
        self.param_list_offset = 0
        self.edge_param_ids    = []
    
    def read_write(self, rw):     
        self.prev_node         = rw.rw_uint32(self.prev_node)
        self.next_node         = rw.rw_uint32(self.next_node)
        self.param_count       = rw.rw_uint32(self.param_count)
        self.param_list_offset = rw.rw_pointer(self.param_list_offset)
        
        rw.assert_equal(self.param_count, self.param_list_offset > 0)

    def rw_param_ids(self, rw):
        rw.assert_local_file_pointer_now_at("Path Edges: ", self.param_list_offset)
        self.edge_param_ids = rw.rw_uint32s(self.edge_param_ids, self.param_count)


class GraphIndex(Serializable):
    def __init__(self, endianness):
        super().__init__(endianness)
        
        self.node_count        = 0
        self.node_list_offset  = 0
        self.edge_count        = 0
        self.edge_list_offset  = 0
        self.start_node_count  = 0
        self.start_node_offset = 0
        self.end_node_count    = 0
        self.end_node_offset   = 0
        
        self.is_loop      = 0
        self.padding_0x24 = 0
        self.padding_0x28 = 0
        self.padding_0x2C = 0
        
        self.padding_0x30 = 0
        self.padding_0x34 = 0
        self.padding_0x38 = 0
        self.padding_0x3C = 0
        
        self.node_id_list = None
        self.edge_id_list = None
        self.start_node_id_list = None
        self.end_node_id_list = None
    
    def read_write(self, rw):
        self.node_count       = rw.rw_uint32(self.node_count)
        self.node_list_offset = rw.rw_pointer(self.node_list_offset)
        self.edge_count       = rw.rw_uint32(self.edge_count)
        self.edge_list_offset = rw.rw_pointer(self.edge_list_offset)
        
        self.start_node_count  = rw.rw_uint32(self.start_node_count)
        self.start_node_offset = rw.rw_pointer(self.start_node_offset)
        self.end_node_count    = rw.rw_uint32(self.end_node_count)
        self.end_node_offset   = rw.rw_pointer(self.end_node_offset)
        
        self.is_loop      = rw.rw_uint32(self.is_loop)
        self.padding_0x24 = rw.rw_pad32(self.padding_0x24)
        self.padding_0x28 = rw.rw_pad32(self.padding_0x28)
        self.padding_0x2C = rw.rw_pad32(self.padding_0x2C)
        
        self.padding_0x30 = rw.rw_pad32(self.padding_0x30)
        self.padding_0x34 = rw.rw_pad32(self.padding_0x34)
        self.padding_0x38 = rw.rw_pad32(self.padding_0x38)
        self.padding_0x3C = rw.rw_pad32(self.padding_0x3C)
        
        rw.assert_is_zero(self.padding_0x24)
        rw.assert_is_zero(self.padding_0x28)
        rw.assert_is_zero(self.padding_0x2C)
        
        rw.assert_is_zero(self.padding_0x30)
        rw.assert_is_zero(self.padding_0x34)
        rw.assert_is_zero(self.padding_0x38)
        rw.assert_is_zero(self.padding_0x3C)

    def rw_node_id_list(self, rw):
        self.node_id_list = rw.rw_uint32s(self.node_id_list, self.node_count)
        
    def rw_edge_id_list(self, rw):
        self.edge_id_list = rw.rw_uint32s(self.edge_id_list, self.edge_count)
        
    def rw_start_node_ids(self, rw):
        self.start_node_id_list = rw.rw_uint32s(self.start_node_id_list, self.start_node_count)
        
    def rw_end_node_ids(self, rw):
        self.end_node_id_list = rw.rw_uint32s(self.end_node_id_list, self.end_node_count)
