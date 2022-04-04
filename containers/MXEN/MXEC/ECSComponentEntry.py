from pyValkLib.serialisation.BaseRW import BaseRW


class ComponentEntry(BaseRW):
    __slots__ = ("ID", "name_offset", "data_size", "data_offset")

    def __init__(self, endianness):
        super().__init__(endianness)
        self.ID = 0
        self.offset_1 = 0
        self.data_size = 0
        self.data_offset = 0
        
        self.data_2 = None
        

    def read_write(self):
        self.rw_var("ID", "I")
        self.rw_var("name_offset", "I")
        self.rw_var("data_size", "I")
        self.rw_var("data_offset", "I")
        
    def rw_data_2(self, lookup_name):
        self.rw_readwriter(self.data_2)
        # getattr(self.data_2, self.rw_method)(self.bytestream)