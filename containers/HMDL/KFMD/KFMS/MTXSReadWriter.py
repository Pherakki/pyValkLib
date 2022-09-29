from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH

class MTXSReadWriter(ValkSerializable32BH):
    FILETYPE = "MTXS"
    
    __slots__ = ("data_size", "data")
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        
        # Data holders
        self.data_size = None
        self.data = None
        
    def read_write_contents(self, rw):
        # Figure out what this is when you've collected a few
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))
        self.data      = rw.rw_bytestring(self.data, self.header.data_length)
        rw.align(rw.local_tell(), 0x10)
    
    def __repr__(self):
        return f"MTXS Object [{self.header.depth}] [0x{self.header.flags:0>8x}]."
