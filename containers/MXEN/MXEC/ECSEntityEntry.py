from pyValkLib.serialisation.BaseRW import BaseRW
from pyValkLib.containers.MXEN.MXEC.StructureList import EntityData

    
class EntityEntry(BaseRW):
    __slots__ = ("ID", "name_offset", "count", "data_offset")

    def __init__(self, endianness):
        super().__init__(endianness)
        self.ID = 0
        self.name_offset = 0
        self.count = 0
        self.data_offset = 0
        
        self.data = None
        

    def read_write(self):
        self.rw_var("ID", "I")
        self.rw_var("name_offset", "I")
        self.rw_var("count", "I")
        self.rw_var("data_offset", "I")
        
        self.rw_var("padding_0x10", "I")
        self.rw_var("padding_0x14", "I")
        self.rw_var("count_4", "I")
        self.rw_var("padding_0x1C", "I")
        
        self.rw_var("padding_0x20", "I")
        self.rw_var("padding_0x24", "I")
        self.rw_var("unknown_0x28", "I")  # 0 or 1?
        self.rw_var("unknown_0x2C", "I")  # Ptr
        
        self.rw_var("padding_0x30", "I")
        self.rw_var("padding_0x34", "I")
        self.rw_var("padding_0x38", "I")
        self.rw_var("padding_0x3C", "I")
        
        self.assert_is_zero("padding_0x10")
        self.assert_is_zero("padding_0x14")
        self.assert_is_zero("padding_0x1C")
        
        self.assert_is_zero("padding_0x20")
        self.assert_is_zero("padding_0x24")
        
        self.assert_is_zero("padding_0x30")
        self.assert_is_zero("padding_0x34")
        self.assert_is_zero("padding_0x38")
        self.assert_is_zero("padding_0x3C")
        
    def rw_data(self, local_tell):
        if self.rw_method == "read":
            self.data = EntityData(self.count, local_tell - self.bytestream.tell())
        
        self.rw_readwriter(self.data)
        