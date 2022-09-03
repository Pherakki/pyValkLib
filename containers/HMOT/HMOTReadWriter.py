from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH

from .KFMO.KFMOReadWriter import KFMOReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter


class HMOTReadWriter(ValkSerializable32BH):
    FILETYPE = "HMOT"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.flags = 0x10000000
        self.KFMO = KFMOReadWriter(endianness)
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.KFMO, self.EOFC]
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))

    def __repr__(self):
        return f"HMOT Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains KFMO."
