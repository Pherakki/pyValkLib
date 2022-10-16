from pyValkLib.serialisation import Serializable
from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH, Header32B


class POF0ReadWriter(ValkSerializable32BH):
    FILETYPE = "POF0"
    
    __slots__ = ("data_size", "data")
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        
        # Data holders
        self.data_size = None
        self.data = None
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))
        self.data_size = rw.rw_uint32(self.data_size, endianness='<')
        self.data      = rw.rw_uint8s(self.data, self.data_size - 4)
        rw.align(rw.local_tell(), 0x10)
