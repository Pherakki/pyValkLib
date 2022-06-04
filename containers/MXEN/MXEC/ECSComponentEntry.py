from pyValkLib.serialisation.Serializable import Serializable
from pyValkLib.containers.MXEN.MXEC.StructureList import data_types


class ComponentEntry(Serializable):
    __slots__ = ("ID", "name_offset", "data_size", "data_offset", "data")

    def __init__(self, endianness):
        super().__init__(endianness)
        self.ID = 0
        self.name_offset = 0
        self.data_size = 0
        self.data_offset = 0
        
        self.data = None
        
    def read_write(self, rw):
        self.ID          = rw.rw_uint32(self.ID)
        self.name_offset = rw.rw_uint32(self.name_offset)
        self.data_size   = rw.rw_uint32(self.data_size)
        self.data_offset = rw.rw_uint32(self.data_offset)
        
    def rw_data(self, lookup_name):
        if self.rw_method == "read":
            self.data = data_types[lookup_name]()
        self.rw_readwriter(self.data)
