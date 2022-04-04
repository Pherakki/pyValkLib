from pyValkLib.serialisation.BaseRW import BaseRW
from pyValkLib.containers.MXEN.MXEC.StructureList import data_types


class ComponentEntry(BaseRW):
    __slots__ = ("ID", "name_offset", "data_size", "data_offset", "data")

    def __init__(self, endianness):
        super().__init__(endianness)
        self.ID = 0
        self.name_offset = 0
        self.data_size = 0
        self.data_offset = 0
        
        self.data = None
        

    def read_write(self):
        self.rw_var("ID", "I")
        self.rw_var("name_offset", "I")
        self.rw_var("data_size", "I")
        self.rw_var("data_offset", "I")
        
    def rw_data(self, lookup_name):
        if self.rw_method == "read":
            self.data = data_types[lookup_name]()
        self.rw_readwriter(self.data)
