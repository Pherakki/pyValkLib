from pyValkLib.serialisation.ValkSerializable import Serializable, ValkSerializable32BH
from pyValkLib.containers.Metadata.POF0.POF0ReadWriter import POF0ReadWriter
from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

class LIPDReadWriter(ValkSerializable32BH):
    FILETYPE = "LIPD"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.data_length = 0
        self.header.flags = 0x18000000
        
        self.contents = Contents(self.context)
        self.data_1 = []
        self.data_2 = []
        
        self.POF0 = POF0ReadWriter("<")
        self.ENRS = ENRSReadWriter("<")
        self.EOFC = EOFCReadWriter("<")
        
    def get_subcontainers(self):
        return []
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))
        rw.rw_obj(self.contents)
        self.data_1 = rw.rw_uint32s(self.data_1, self.contents.count_1)
        self.data_2 = rw.rw_uint32s(self.data_2, self.contents.count_2)
        
        rw.align(rw.local_tell(), 0x10)

    def __repr__(self):
        return f"LIPD Object [{self.header.depth}] [0x{self.header.flags:0>8x}]."

class Contents(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.id           = None
        self.count_1      = None
        self.count_2      = None
        self.unknown_0x0C = None
        
    def __repr__(self):
        return f"[LIPD::Contents] {self.id} {self.count_1} {self.count_2} {self.unknown_0x0C}"
        
    def read_write(self, rw):
        self.id           = rw.rw_uint32(self.id)
        self.count_1      = rw.rw_uint32(self.count_1)
        self.count_2      = rw.rw_uint32(self.count_2)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
