from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from .KFMH.KFMHReadWriter import KFMHReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

class KFMLReadWriter(ValkSerializable32BH):
    FILETYPE = "KFML"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x10000004
        
        self.KFMH = KFMHReadWriter(endianness)
        
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.KFMH, self.EOFC]
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000004, lambda x: hex(x))
        

    def __repr__(self):
        return f"KFML Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains KFMH."
        