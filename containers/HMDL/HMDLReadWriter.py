from pyValkLib.serialisation.ValkSerializable import Context, Serializable, ValkSerializable32BH

from .KFMD.KFMDReadWriter import KFMDReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter


class HMDLReadWriter(ValkSerializable32BH):
    FILETYPE = "HMDL"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.flags = 0x10000000
        self.KFMDs = KFMDArray(endianness)
        self.EOFC  = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.KFMDs, self.EOFC]
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))

    def __repr__(self):
        return f"HMDL Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains KFMD."

class KFMDArray(Serializable):
    def __init__(self, endianness=None):
        super().__init__(Context())
        self.KFMDs = []
        if endianness is not None:
            self.context.endianness = endianness
        
    def read_write(self, rw):
        if rw.mode() == "read":
            ctr_type = rw.peek_bytestring(4)
            while ctr_type == b"KFMD":
                kfmd = KFMDReadWriter(self.context.endianness)
                self.KFMDs.append(kfmd)
                rw.rw_obj(kfmd)
                ctr_type = rw.peek_bytestring(4)
        else:
            for obj in self.KFMDs:
                rw.rw_obj(obj)
                
    def checkKFMDType(self, value):
        if type(value) is not KFMDReadWriter:
            raise TypeError(f"KFMDArray object expected a KFMDReadWriter, received '{type(value)}'.")
                
    def __iter__(self):
        for obj in self.KFMDs:
            yield obj
            
    def __len__(self):
        return len(self.KFMDs)

    def __getitem__(self, idx):
        return self.KFMDs[idx]
    
    def __setitem__(self, idx, value):
        self.checkKFMDType(value)
        self.KFMDs[idx] = value
        
    def append(self, value):
        self.checkKFMDType(value)
        self.KFMDs.append(value)
    