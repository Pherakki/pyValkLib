from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from .KFSM.KFSMReadWriter import KFSMReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

class HSCMReadWriter(ValkSerializable32BH):
    FILETYPE = "HSCM"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x10000000
        
        self.KFSM = KFSMReadWriter(endianness)
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.KFSM, self.EOFC]
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))
