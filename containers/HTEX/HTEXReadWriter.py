from pyValkLib.serialisation.ValkSerializable import Context, Serializable, ValkSerializable32BH
from pyValkLib.containers.HTEX.HTSF.HTSFReadWriter import HTSFReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter


class HTEXReadWriter(ValkSerializable32BH):
    FILETYPE = "HTEX"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.data_length = 0
        self.header.flags = 0x10000000
        self.HTSFs = HTSFArray(endianness)
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.HTSFs, self.EOFC]
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))

    def __repr__(self):
        return f"HTEX Object [{self.header.depth}] [0x{self.header.flags:0>8x}]: Contains HTSF."

class HTSFArray(Serializable):
    def __init__(self, endianness=None):
        super().__init__(Context())
        self.HTSFs = []
        if endianness is not None:
            self.context.endianness = endianness
        
    def read_write(self, rw):
        if rw.mode() == "read":
            ctr_type = rw.peek_bytestring(4)
            while ctr_type == b"HTSF":
                htsf = HTSFReadWriter(self.context.endianness)
                rw.rw_obj(htsf)
                self.HTSFs.append(htsf)
                ctr_type = rw.peek_bytestring(4)
        else:
            for obj in self.HTSFs:
                rw.rw_obj(obj)
                
    def checkHTSFType(self, value):
        if type(value) is not HTSFReadWriter:
            raise TypeError(f"HTSFArray object expected an HTSFReadWriter, received '{type(value)}'.")
                
    def __iter__(self):
        for obj in self.HTSFs:
            yield obj
            
    def __len__(self):
        return len(self.HTSFs)

    def __getitem__(self, idx):
        return self.HTSFs[idx]
    
    def __setitem__(self, idx, value):
        self.checkHTSFType(value)
        self.HTSFs[idx] = value
        
    def append(self, value):
        self.checkHTSFType(value)
        self.HTSFs.append(value)
    