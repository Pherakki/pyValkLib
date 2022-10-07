from pyValkLib.serialisation.ValkSerializable import Serializable, ValkSerializable32BH
from .KSPR.KSPRReadWriter import KSPRReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

class HSPRReadWriter(ValkSerializable32BH):
    FILETYPE = "HSPR"
    
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x10000000
        
        self.KSPR = KSPRReadWriter(endianness)
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.KSPR, self.EOFC]
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))
        

    def __repr__(self):
        return f"HSPR Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains KSPR."
