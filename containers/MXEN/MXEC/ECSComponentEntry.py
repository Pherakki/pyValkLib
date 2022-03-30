from pyValkLib.serialisation.BaseRW import BaseRW


class ComponentEntry(BaseRW):
    __slots__ = ("ID", "offset_1", "data_size", "offset_2")

    def __init__(self):
        super().__init__()
        self.ID = 0
        self.offset_1 = 0
        self.data_size = 0
        self.offset_2 = 0
        
        self.data_2 = None
        

    def read_write(self):
        self.rw_var("ID", "I", endianness=">")
        self.rw_var("offset_1", "I", endianness=">")
        self.rw_var("data_size", "I", endianness=">")
        self.rw_var("offset_2", "I", endianness=">")
        
    def rw_data_2(self, lookup_name):
        self.rw_readwriter(self.data_2)
        # getattr(self.data_2, self.rw_method)(self.bytestream)