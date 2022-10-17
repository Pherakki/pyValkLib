from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from .KFML.KFMLReadWriter import KFMLReadWriter
from .KFMM.KFMMReadWriter import KFMMReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

class HMRPReadWriter(ValkSerializable32BH):
    FILETYPE = "HMRP"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x10000004
        
        self.KFML = KFMLReadWriter(endianness)
        self.KFMM = KFMMReadWriter(endianness)
        
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.KFML, self.KFMM, self.EOFC]
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000004, lambda x: hex(x))
        

    def __repr__(self):
        return f"HMRP Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains KFML, KFMM."
        