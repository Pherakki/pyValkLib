from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH

from .MXMH.MXMHReadWriter import MXMHReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter


class MXMIReadWriter(ValkSerializable32BH):
    FILETYPE = "MXMI"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.flags = 0x10000000
        self.MXMH = MXMHReadWriter(endianness)
        self.EOFC = EOFCReadWriter("<")
        
        self.file_blob = b""

    def get_subcontainers(self):
        return [self.MXMH, self.EOFC]
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))
        self.file_blob = rw.rw_bytestring(self.file_blob, self.header.data_length)

    def __repr__(self):
        return f"MXMI Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains EOFC."
