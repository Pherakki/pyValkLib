from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from pyValkLib.containers.Metadata.POF0.POF0ReadWriter import POF0ReadWriter
from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

from pyValkLib.containers.Metadata.POF0.POF0Compression import POF0Validator
from pyValkLib.containers.Metadata.ENRS.ENRSCompression import ENRSValidator


class KFMHReadWriter(ValkSerializable32BH):
    FILETYPE = "KFMH"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x18000004
        
        self.unknown_0x00 = None
        self.count = None
        self.data_start_offset = None
        
        self.data = None
        
        self.POF0 = POF0ReadWriter("<")
        self.ENRS = ENRSReadWriter("<")
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.POF0, self.ENRS, self.EOFC, 
                POF0Validator(self),
                ENRSValidator(self)]
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x18000004, lambda x: hex(x))
        
        rw.mark_new_contents_array()
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.count = rw.rw_uint32(self.count)
        self.data_start_offset = rw.rw_pointer(self.data_start_offset)
        rw.align(rw.local_tell(), 0x10)
        
        rw.mark_new_contents_array()
        rw.assert_local_file_pointer_now_at("Data Start", self.data_start_offset)
        self.data = rw.rw_bytestrings(self.data, 16, self.count)
        
        rw.assert_equal(self.unknown_0x00, 2)
        

    def __repr__(self):
        return f"KFMH Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains POF0, ENRS."
