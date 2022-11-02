from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from .POF0Compression import buildPOF0, compressPOF0

class POF0ReadWriter(ValkSerializable32BH):
    FILETYPE = "POF0"
    
    __slots__ = ("data_size", "data")
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        self.header.flags = 0x10000000
        
        # Data holders
        self.data_size = None
        self.data = None
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))
        self.data_size = rw.rw_uint32(self.data_size, endianness='<')
        self.data      = rw.rw_uint8s(self.data, self.data_size - 4)
        rw.align(rw.local_tell(), 0x10)

    @classmethod
    def from_obj(cls, obj):
        instance = cls({})
        data = compressPOF0(buildPOF0(obj))
        data_size = len(data)
        remainder = (0x04 - (data_size % 0x04)) % 0x04
        instance.data_size = data_size + 4
        instance.data_size += remainder
        instance.data = data + [0]*remainder
        
        instance.header.data_length = instance.data_size
        instance.header.data_length += (0x10 - (instance.header.data_length % 0x10)) % 0x10
        instance.header.contents_length = instance.header.data_length
        instance.header.depth = obj.header.depth + 1
        return instance
        