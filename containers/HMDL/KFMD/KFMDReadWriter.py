from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH

from .KFMS.KFMSReadWriter import KFMSReadWriter
from .KFMG.KFMGReadWriter import KFMGReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter


class KFMDReadWriter(ValkSerializable32BH):
    FILETYPE = "KFMD"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.flags = 0x10000000
        self.KFMS = KFMSReadWriter(endianness)
        self.KFMG = KFMGReadWriter(self.KFMS, endianness)
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.KFMS, self.KFMG, self.EOFC]
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))

    def __repr__(self):
        return f"KFMD Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains KFMS, KFMG, EOFC."
