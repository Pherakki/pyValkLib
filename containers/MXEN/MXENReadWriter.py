from pyValkLib.serialisation.ValkyriaBaseRW import ValkyriaBaseRW32BH

class MXENReadWriter(ValkyriaBaseRW32BH):
    FILETYPE = "MXEN"
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        
        self.MXEC = containers["MXEC"](containers, endianness)
        
        self.subcontainers.extend([self.MXEC])
    
    def read_write_contents(self):
        self.assert_equal("flags", 0x10000005, self.header, lambda x: hex(x))
        
    def __repr__(self):
        return f"MXEN Object [{self.header.depth}] [0x{self.header.flags:0>8x}]: Contains MXEC."