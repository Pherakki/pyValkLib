from pyValkLib.serialisation.ValkSerializable import Serializable, ValkSerializable48BH
from .KFSS.KFSSReadWriter import KFSSReadWriter
from .KFSG.KFSGReadWriter import KFSGReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter


class KFSHReadWriter(ValkSerializable48BH):
    FILETYPE = "KFSH"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x10010000
        
        self.KFSS = KFSSReadWriter(endianness)
        self.KFSG = KFSGReadWriter(self.KFSS, endianness)
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.KFSS, self.KFSG, self.EOFC]
    
    def __repr__(self):
        return f"KFSH Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains KFSS, KFSG."    
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10010000, lambda x: hex(x))
