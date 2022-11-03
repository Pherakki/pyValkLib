from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from .ENRSCompression import buildENRS, toENRSPackedRep, compressENRS


class ENRSReadWriter(ValkSerializable32BH):
    FILETYPE = "ENRS"
    
    __slots__ = ("padding_0x20", "num_groups", "data")
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x10000000
        # Data holders
        self.padding_0x20 = 0
        self.num_groups = None
        self.data = []
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x : hex(x))
        
        self.padding_0x20 = rw.rw_uint32(self.padding_0x20, endianness='<')
        self.num_groups   = rw.rw_uint32(self.num_groups, endianness='<')
        rw.align(rw.local_tell(), 0x10)
        rw.assert_equal(self.padding_0x20, 0)
        
        self.data = rw.rw_uint8s(self.data, self.header.data_length - 0x10)
        rw.align(rw.local_tell(), 0x10)

    @classmethod
    def from_obj(cls, obj, endianness='<'):
        instance = cls(endianness)
        groups = toENRSPackedRep(buildENRS(obj))
        instance.num_groups = len(groups)
        instance.data = compressENRS(groups)
        
        data_length = len(instance.data)
        remainder = (0x10 - (data_length % 0x10)) % 0x10
        instance.data += [0]*remainder
        data_length += remainder
        
        instance.header.data_length = data_length + 0x10
        instance.header.contents_length = data_length + 0x10
        instance.header.depth = obj.header.depth + 1
        return instance
