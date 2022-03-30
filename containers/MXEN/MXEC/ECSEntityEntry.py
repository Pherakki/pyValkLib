from pyValkLib.serialisation.BaseRW import BaseRW

    
class EntityEntry(BaseRW):
    __slots__ = ("ID", "offset_1", "count", "offset_2")

    def __init__(self):
        super().__init__()
        self.ID = 0
        self.offset_1 = 0
        self.count = 0
        self.offset_2 = 0
        
        self.data_2 = None
        

    def read_write(self):
        self.rw_var("ID", "I", endianness=">")
        self.rw_var("offset_1", "I", endianness=">")
        self.rw_var("count", "I", endianness=">")
        self.rw_var("offset_2", "I", endianness=">")
        
        self.rw_var("padding_0x10", "I", endianness=">")
        self.rw_var("padding_0x14", "I", endianness=">")
        self.rw_var("count_4", "I", endianness=">")
        self.rw_var("padding_0x1C", "I", endianness=">")
        
        self.rw_var("padding_0x20", "I", endianness=">")
        self.rw_var("padding_0x24", "I", endianness=">")
        self.rw_var("unknown_0x28", "I", endianness=">")  # 0 or 1?
        self.rw_var("unknown_0x2C", "I", endianness=">")  # Ptr
        
        self.rw_var("padding_0x30", "I", endianness=">")
        self.rw_var("padding_0x34", "I", endianness=">")
        self.rw_var("padding_0x38", "I", endianness=">")
        self.rw_var("padding_0x3C", "I", endianness=">")
        
        self.assert_is_zero("padding_0x10")
        self.assert_is_zero("padding_0x14")
        self.assert_is_zero("padding_0x1C")
        
        self.assert_is_zero("padding_0x20")
        self.assert_is_zero("padding_0x24")
        
        self.assert_is_zero("padding_0x30")
        self.assert_is_zero("padding_0x34")
        self.assert_is_zero("padding_0x38")
        self.assert_is_zero("padding_0x3C")
        
    def rw_data_2(self, lookup_name, local_tell):
        lookup_part = lookup_name.split(":")[0]
        if self.rw_method == "read":
            self.data_2 = data_types[lookup_part](self.count, self.offset_2, local_tell - self.bytestream.tell())
        
        self.rw_readwriter(self.data_2)
        #getattr(self.data_2, self.rw_method)(self.bytestream)
        