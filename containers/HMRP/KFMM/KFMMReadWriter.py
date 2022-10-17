from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from .KFMI.KFMIReadWriter import KFMIReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter


class KFMMReadWriter(ValkSerializable32BH):
    FILETYPE = "KFMM"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x10000004
        
        self.KFMI = KFMIReadWriter(endianness)
        
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.KFMI, self.EOFC]
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000004, lambda x: hex(x))
        

    def __repr__(self):
        return f"KFMM Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains KFMI."
