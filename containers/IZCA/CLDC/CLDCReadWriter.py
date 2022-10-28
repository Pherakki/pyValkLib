from pyValkLib.serialisation.ValkSerializable import Context, Serializable, ValkSerializable32BH
from .LIPD.LIPDReadWriter import LIPDReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

class CLDCReadWriter(ValkSerializable32BH):
    FILETYPE = "CLDC"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.data_length = 0
        self.header.flags = 0x18000000
        
        self.contents = Contents(self.context)
        
        self.LIPDs = LIPDArray(endianness)
        self.EOFC = EOFCReadWriter("<")
        
        
    def get_subcontainers(self):
        return [self.LIPDs, self.EOFC]
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))
        rw.rw_obj(self.contents)
        self.LIPDs.set_count(self.contents.LIPD_count)

    def __repr__(self):
        return f"CLDC Object [{self.header.depth}] [0x{self.header.flags:0>8x}]."

class Contents(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.LIPD_count   = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        
    def __repr__(self):
        return f"[CLDC::Contents] {self.LIPD_count} {self.unknown_0x04} {self.unknown_0x08} {self.unknown_0x0C}"
        
    def read_write(self, rw):
        self.LIPD_count   = rw.rw_uint32(self.LIPD_count)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        
class LIPDArray(Serializable):
    FILETYPE = "LIPD"
    
    def __init__(self, endianness=None):
        super().__init__(Context())
        self.LIPDs = []
        self.__count = 0
        if endianness is not None:
            self.context.endianness = endianness
            
    def __repr__(self):
        return f"[CLDC::LIPDs] {self.LIPDs}"
        
    def set_count(self, count):
        self.__count = count
        
    def read_write(self, rw):
        if rw.mode() == "read":
            self.LIPDs = [LIPDReadWriter(self.context.endianness) for _ in range(self.__count)]
        
        for obj in self.LIPDs:
            rw.rw_obj(obj)
                
    def checkLIPDType(self, value):
        if type(value) is not LIPDReadWriter:
            raise TypeError(f"LIPDArray object expected a LIPDReadWriter, received '{type(value)}'.")
                
    def __iter__(self):
        for obj in self.LIPDs:
            yield obj
            
    def __len__(self):
        return len(self.LIPDs)

    def __getitem__(self, idx):
        return self.LIPDs[idx]
    
    def __setitem__(self, idx, value):
        self.checkLIPDType(value)
        self.LIPDs[idx] = value
        
    def append(self, value):
        self.checkLIPDType(value)
        self.LIPDs.append(value)