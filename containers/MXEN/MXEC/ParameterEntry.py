from pyValkLib.serialisation.Serializable import Serializable
from pyValkLib.containers.MXEN.MXEC.StructureList import data_types


class ParameterEntry(Serializable):
    __slots__ = ("name", "ID", "name_offset", "data_size", "data_offset", "parameter_type", "data")

    def __init__(self, context):
        super().__init__(context)
        self.ID = 0
        self.name_offset = 0
        self.data_size = 0
        self.data_offset = 0
        
        self.parameter_type = None
        
        self.data = None
        
    def read_write(self, rw):
        self.ID          = rw.rw_uint32(self.ID)
        self.name_offset = rw.rw_pointer(self.name_offset)
        self.data_size   = rw.rw_uint32(self.data_size)
        self.data_offset = rw.rw_pointer(self.data_offset)
        
    def rw_data(self, rw, lookup_name):
        if rw.mode() == "read":
            self.data = data_types[lookup_name](self.context)
        rw.rw_obj(self.data)
        rw.align(rw.local_tell(), 0x10)
