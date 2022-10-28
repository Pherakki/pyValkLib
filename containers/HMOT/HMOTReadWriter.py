from pyValkLib.serialisation.ValkSerializable import Context, Serializable, ValkSerializable32BH

from .KFMO.KFMOReadWriter import KFMOReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter


class HMOTReadWriter(ValkSerializable32BH):
    FILETYPE = "HMOT"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.flags = 0x10000000
        self.KFMOs = KFMOArray(endianness)
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.KFMOs, self.EOFC]
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))

    def __repr__(self):
        return f"HMOT Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains KFMO."

class KFMOArray(Serializable):
    def __init__(self, endianness=None):
        super().__init__(Context())
        self.KFMOs = []
        if endianness is not None:
            self.context.endianness = endianness
    
    def __repr__(self):
        return f"[HMOT::KFMOArray] {self.KFMOs}"
        
    def read_write(self, rw):
        if rw.mode() == "read":
            ctr_type = rw.peek_bytestring(4)
            while ctr_type == b"KFMO":
                kfmo = KFMOReadWriter(self.context.endianness)
                self.KFMOs.append(kfmo)
                rw.rw_obj(kfmo)
                ctr_type = rw.peek_bytestring(4)
        else:
            for obj in self.KFMDs:
                rw.rw_obj(obj)
                
    def checkKFMOType(self, value):
        if type(value) is not KFMOReadWriter:
            raise TypeError(f"KFMOArray object expected a KFMOReadWriter, received '{type(value)}'.")
                
    def __iter__(self):
        for obj in self.KFMOs:
            yield obj
            
    def __len__(self):
        return len(self.KFMOs)

    def __getitem__(self, idx):
        return self.KFMOs[idx]
    
    def __setitem__(self, idx, value):
        self.checkKFMOType(value)
        self.KFMOs[idx] = value
        
    def append(self, value):
        self.checkKFMOType(value)
        self.KFMOs.append(value)
    