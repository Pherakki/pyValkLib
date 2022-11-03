from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from .MTXSCompression import buildMTXS, toMTXSPackedRep, compressMTXS


class MTXSReadWriter(ValkSerializable32BH):
    FILETYPE = "MTXS"
    
    __slots__ = ("padding_0x20", "num_groups", "data")
    
    def __init__(self, endianness=None):
        super().__init__(endianness)
        self.header.flags = 0x10000000
        
        # Data holders
        self.padding_0x20 = 0
        self.num_groups = None
        self.data = None
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))
        self.padding_0x20 = rw.rw_uint32(self.padding_0x20)
        self.num_groups   = rw.rw_uint32(self.num_groups)
        rw.align(rw.local_tell(), 0x10)
        
        rw.assert_is_zero(self.padding_0x20)
        self.data = rw.rw_uint8s(self.data, self.header.data_length - 0x10)

    @classmethod
    def from_obj(cls, obj, endianness='<'):
        instance = cls(endianness)
        groups = toMTXSPackedRep(buildMTXS(obj))
        instance.num_groups = len(groups)
        instance.data = compressMTXS(groups)
        
        data_length = len(instance.data)
        remainder = (0x10 - (data_length % 0x10)) % 0x10
        instance.data += [0]*remainder
        data_length += remainder
        
        instance.header.data_length = data_length + 0x10
        instance.header.contents_length = data_length + 0x10
        instance.header.depth = obj.header.depth + 1
        return instance
