from pyValkLib.serialisation.ValkyriaBaseRW import ValkyriaBaseRW32BH


class EOFCReadWriter(ValkyriaBaseRW32BH):
    FILETYPE = "EOFC"
    
    __slots__ = tuple()
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        
    def read_write_contents(self):
        self.assert_equal("flags", 0x10000000, self.header, lambda x: hex(x))

    def __repr__(self):
        return f"EOFC Object [{self.header.depth}] [0x{self.header.flags:0>8x}]: Zero data."