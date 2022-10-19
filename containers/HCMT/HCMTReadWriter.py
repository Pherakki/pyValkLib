from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from .KFCM.KFCMReadWriter import KFCMReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

class HCMTReadWriter(ValkSerializable32BH):
    FILETYPE = "HCMT"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x10000000
        
        self.KFCM = KFCMReadWriter(endianness)
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.KFCM, self.EOFC]
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))
