from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH

from .KFMD.KFMDReadWriter import KFMDReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter


class HMDLReadWriter(ValkSerializable32BH):
    FILETYPE = "HMDL"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.flags = 0x10000000
        self.KFMD = KFMDReadWriter(endianness)
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.KFMD, self.EOFC]
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))

    def __repr__(self):
        return f"HMDL Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains KFMD."
