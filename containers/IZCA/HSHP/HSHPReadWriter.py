from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from .KFSH.KFSHReadWriter import KFSHReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

class HSHPReadWriter(ValkSerializable32BH):
    FILETYPE = "HSHP"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x10000000
        
        self.KFSH = KFSHReadWriter(endianness)
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.KFSH, self.EOFC]
        
    def read_write_contents(self, rw):
        print("### NEW HSHP ###")
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))
        

    def __repr__(self):
        return f"HSHP Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains KFSH."
        