from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from .KFMA.KFMAReadWriter import KFMAReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

class HMMTReadWriter(ValkSerializable32BH):
    FILETYPE = "HMMT"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x10000000
        
        self.KFMA = KFMAReadWriter(endianness)
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.KFMA, self.EOFC]
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))

        