from pyValkLib.serialisation.Serializable import Serializable
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray


class BatchRenderEntry(Serializable):
    __slots__ = ("name_offset", 
                 "t1_count", "t1_offset", "t1_data",
                 "t2_count", "t2_offset", "t2_data",
                 "t3_count", "t3_offset", "t3_data",
                 "t4_count", "t4_offset", "t4_data",)

    def __init__(self, endianness):
        super().__init__(endianness)
        self.name_offset = 0
        self.t1_count  = 0
        self.t1_offset = 0
        self.t2_count  = 0
        self.t2_offset = 0
        self.t3_count  = 0
        self.t3_offset = 0
        self.t4_count  = 0
        self.t4_offset = 0

        self.t1_data = []
        self.component_references = []
        self.t3_data = []
        self.unused_ids = []
        

    def read_write(self, rw):
        self.name_offset  = rw.rw_uint32(self.name_offset)
        self.t1_count     = rw.rw_uint32(self.t1_count)
        self.t1_offset    = rw.rw_uint32(self.t1_offset)
        self.t2_count     = rw.rw_uint32(self.t2_count)
        
        self.t2_offset    = rw.rw_uint32(self.t2_offset)
        self.t3_count     = rw.rw_uint32(self.t3_count)
        self.t3_offset    = rw.rw_uint32(self.t3_offset)
        self.t4_count     = rw.rw_uint32(self.t4_count)
        
        self.t4_offset    = rw.rw_uint32(self.t4_offset)
        self.padding_0x24 = rw.rw_uint32(self.padding_0x24)
        self.padding_0x28 = rw.rw_uint32(self.padding_0x28)
        self.padding_0x2C = rw.rw_uint32(self.padding_0x2C)
        
        self.padding_0x30 = rw.rw_uint32(self.padding_0x30)
        self.padding_0x34 = rw.rw_uint32(self.padding_0x34)
        self.padding_0x38 = rw.rw_uint32(self.padding_0x38)
        self.padding_0x3C = rw.rw_uint32(self.padding_0x3C)

        
        rw.assert_is_zero(self.padding_0x24)
        rw.assert_is_zero(self.padding_0x28)
        rw.assert_is_zero(self.padding_0x2C)
        
        rw.assert_is_zero(self.padding_0x30)
        rw.assert_is_zero(self.padding_0x34)
        rw.assert_is_zero(self.padding_0x38)
        rw.assert_is_zero(self.padding_0x3C)
        
    def rw_t1_data(self):
        if self.rw_method == "read":
            self.t1_data = [BatchRender_T1(self.endianness) for _ in range(self.t1_count)]
        for t1 in self.t1_data:
            self.rw_readwriter(t1)
            #getattr(t1, self.rw_method)(self.bytestream)
            

    def rw_t2_data(self):
        if self.rw_method == "read":
            self.component_references = [ComponentReference(self.endianness) for _ in range(self.t2_count)]
        for t2 in self.component_references:
            self.rw_readwriter(t2)
            #getattr(t2, self.rw_method)(self.bytestream)
            
    def rw_t3_data(self):
        if self.rw_method == "read":
            self.t3_data = [BatchRender_T3(self.endianness) for _ in range(self.t3_count)]
        for t3 in self.t3_data:
            self.rw_readwriter(t3)
            #getattr(t3, self.rw_method)(self.bytestream)
            
    def rw_t4_data(self):
        self.rw_varlist("unused_ids", "I", self.t4_count)
        
class BatchRender_T1(Serializable):
    def __init__(self, endianness):
        super().__init__(endianness)
        
        self.count_1 = 0
        self.offset_1 = 0
        self.count_2 = 0
        self.offset_2 = 0
        self.ID = 0
        
        self.local_component_ids_1 = []
        self.local_component_ids_2 = []

    def read_write(self, rw):
        self.count_1      = rw.rw_uint32(self.count_1)
        self.offset_1     = rw.rw_uint32(self.offset_1)
        self.count_2      = rw.rw_uint32(self.count_2)
        self.offset_2     = rw.rw_uint32(self.offset_2)
        
        self.ID           = rw.rw_uint32(self.ID)
        self.padding_0x14 = rw.rw_uint32(self.padding_0x14)
        self.padding_0x18 = rw.rw_uint32(self.padding_0x18)
        self.padding_0x1C = rw.rw_uint32(self.padding_0x1C)
        
        rw.assert_is_zero(self.padding_0x14)
        rw.assert_is_zero(self.padding_0x18)
        rw.assert_is_zero(self.padding_0x1C)
        
    def rw_data_1(self, rw):
        self.local_component_ids_1 = rw.rw_uint32s(self.local_component_ids_1, self.count_1)
        
    def rw_data_2(self, rw):
        self.local_component_ids_2 = rw.rw_uint32s(self.local_component_ids_2, self.count_2)
        

class ComponentReference(Serializable):
    def __init__(self, endianness):
        super().__init__(endianness)
        
        self.table_component_id_1 = 0
        self.table_component_id_2 = 0
        self.count = 0
        self.offset = 0
        self.component_indices = []
    
    def read_write(self, rw):     
        self.table_component_id_1 = rw.rw_uint32(self.table_component_id_1)
        self.table_component_id_2 = rw.rw_uint32(self.table_component_id_2)
        self.count                = rw.rw_uint32(self.count)
        self.offset               = rw.rw_uint32(self.offset)
        
        rw.assert_equal("count", self.offset > 0)

    def rw_data(self, rw):
        self.component_indices = rw.rw_uint32s(self.component_indices, self.count)
        

class BatchRender_T3(Serializable):
    def __init__(self, endianness):
        super().__init__(endianness)
        
        self.count_1 = 0
        self.offset_1 = 0
        self.count_2 = 0
        self.offset_2 = 0
        
        
        self.data_1 = None
        self.data_2 = None
        self.data_3 = None
        self.data_4 = None
    
    def read_write(self, rw):
        self.count_1  = rw.rw_uint32(self.count_1)
        self.offset_1 = rw.rw_uint32(self.offset_1)
        self.count_2  = rw.rw_uint32(self.count_2)
        self.offset_2 = rw.rw_uint32(self.offset_2)
        
        self.count_3  = rw.rw_uint32(self.count_3)
        self.offset_3 = rw.rw_uint32(self.offset_3)
        self.count_4  = rw.rw_uint32(self.count_4)
        self.offset_4 = rw.rw_uint32(self.offset_4)
        
        self.unknown_0x20 = rw.rw_uint32(self.unknown_0x20) # Can be 0 or 1
        self.padding_0x24 = rw.rw_uint32(self.padding_0x24)
        self.padding_0x28 = rw.rw_uint32(self.padding_0x28)
        self.padding_0x2C = rw.rw_uint32(self.padding_0x2C)
        
        self.padding_0x30 = rw.rw_uint32(self.padding_0x30)
        self.padding_0x34 = rw.rw_uint32(self.padding_0x34)
        self.padding_0x38 = rw.rw_uint32(self.padding_0x38)
        self.padding_0x3C = rw.rw_uint32(self.padding_0x3C)
        
        rw.assert_is_zero(self.padding_0x24)
        rw.assert_is_zero(self.padding_0x28)
        rw.assert_is_zero(self.padding_0x2C)
        
        rw.assert_is_zero(self.padding_0x30)
        rw.assert_is_zero(self.padding_0x34)
        rw.assert_is_zero(self.padding_0x38)
        rw.assert_is_zero(self.padding_0x3C)

    def rw_data_1(self, rw):
        self.table_component_id = rw.rw_uint32s(self.table_component_id, self.count_1)
        
    def rw_data_2(self, rw):
        self.local_component_id = rw.rw_uint32s(self.local_component_id, self.count_2)
        
    def rw_data_3(self, rw):
        self.data_3 = rw.rw_uint32s(self.data_3, self.count_3)
        
    def rw_data_4(self, rw):
        self.count_4 = rw.rw_uint32s(self.data_4, self.count_4)
        