from pyValkLib.serialisation.BaseRW import BaseRW


class BatchRenderEntry(BaseRW):
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
        

    def read_write(self):
        self.rw_var("name_offset", "I")
        self.rw_var("t1_count", "I")
        self.rw_var("t1_offset", "I")
        self.rw_var("t2_count", "I")
        
        self.rw_var("t2_offset", "I")
        self.rw_var("t3_count", "I")
        self.rw_var("t3_offset", "I")
        self.rw_var("t4_count", "I")
        
        self.rw_var("t4_offset", "I")
        self.rw_var("padding_0x24", "I")
        self.rw_var("padding_0x28", "I")
        self.rw_var("padding_0x2C", "I")
        
        self.rw_var("padding_0x30", "I")
        self.rw_var("padding_0x34", "I")
        self.rw_var("padding_0x38", "I")
        self.rw_var("padding_0x3C", "I")
        
        self.assert_is_zero("padding_0x24")
        self.assert_is_zero("padding_0x28")
        self.assert_is_zero("padding_0x2C")
        
        self.assert_is_zero("padding_0x30")
        self.assert_is_zero("padding_0x34")
        self.assert_is_zero("padding_0x38")
        self.assert_is_zero("padding_0x3C")
        
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
        
class BatchRender_T1(BaseRW):
    def __init__(self, endianness):
        super().__init__(endianness)
        
        self.count_1 = 0
        self.offset_1 = 0
        self.count_2 = 0
        self.offset_2 = 0
        self.ID = 0
        
        self.local_component_ids_1 = []
        self.local_component_ids_2 = []

    def read_write(self):
        self.rw_var("count_1", "I")
        self.rw_var("offset_1", "I")
        self.rw_var("count_2", "I")
        self.rw_var("offset_2", "I")
        
        self.rw_var("ID", "I")
        self.rw_var("padding_0x14", "I")
        self.rw_var("padding_0x18", "I")
        self.rw_var("padding_0x1C", "I")
        
        self.assert_is_zero("padding_0x14")
        self.assert_is_zero("padding_0x18")
        self.assert_is_zero("padding_0x1C")
        
        
    def rw_data_1(self):
        self.rw_varlist("local_component_ids_1", "I", self.count_1)
        
    def rw_data_2(self):
        self.rw_varlist("local_component_ids_2", "I", self.count_2)
        

class ComponentReference(BaseRW):
    def __init__(self, endianness):
        super().__init__(endianness)
        
        self.table_component_id_1 = 0
        self.table_component_id_2 = 0
        self.count = 0
        self.offset = 0
        self.component_indices = []
    
    def read_write(self):
        self.rw_var("table_component_id_1", "I")
        self.rw_var("table_component_id_2", "I")
        self.rw_var("count", "I")
        self.rw_var("offset", "I")
        
        self.assert_equal("count", self.offset > 0)

    def rw_data(self):
        self.rw_varlist("component_indices", "I", self.count)
        

class BatchRender_T3(BaseRW):
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
    
    def read_write(self):
        self.rw_var("count_1", "I")
        self.rw_var("offset_1", "I")
        self.rw_var("count_2", "I")
        self.rw_var("offset_2", "I")
        
        self.rw_var("count_3", "I")
        self.rw_var("offset_3", "I")
        self.rw_var("count_4", "I")
        self.rw_var("offset_4", "I")
        
        self.rw_var("unknown_0x20", "I") # Can be 0 or 1
        self.rw_var("padding_0x24", "I")
        self.rw_var("padding_0x28", "I")
        self.rw_var("padding_0x2C", "I")
        
        self.rw_var("padding_0x30", "I")
        self.rw_var("padding_0x34", "I")
        self.rw_var("padding_0x38", "I")
        self.rw_var("padding_0x3C", "I")
        
        self.assert_is_zero("padding_0x24")
        self.assert_is_zero("padding_0x28")
        self.assert_is_zero("padding_0x2C")
        
        self.assert_is_zero("padding_0x30")
        self.assert_is_zero("padding_0x34")
        self.assert_is_zero("padding_0x38")
        self.assert_is_zero("padding_0x3C")

    def rw_data_1(self):
        self.rw_varlist("table_component_id", "I", self.count_1)
        
    def rw_data_2(self):
        self.rw_varlist("local_component_id", "I", self.count_2)
        
    def rw_data_3(self):
        self.rw_varlist("data_3", "I", self.count_3)
        
    def rw_data_4(self):
        self.rw_varlist("data_4", "I", self.count_4)
        