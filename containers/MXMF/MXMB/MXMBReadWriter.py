from pyValkLib.serialisation.ValkSerializable import Context, Serializable, ValkSerializable32BH

from .MXMI.MXMIReadWriter import MXMIReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter


class MXMBReadWriter(ValkSerializable32BH):
    FILETYPE = "MXMB"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.flags = 0x10000000
        self.MXMIs = MXMIArray(endianness)
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.MXMIs, self.EOFC]
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))

    def __repr__(self):
        return f"MXMB Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains MXMI, EOFC."


class MXMIArray(Serializable):
    def __init__(self, endianness=None):
        super().__init__(Context())
        self.MXMIs = []
        if endianness is not None:
            self.context.endianness = endianness
        
    def read_write(self, rw):
        if rw.mode() == "read":
            ctr_type = rw.peek_bytestring(4)
            while ctr_type == b"MXMI":
                mxmi = MXMIReadWriter(self.context.endianness)
                rw.rw_obj(mxmi)
                self.MXMIs.append(mxmi)
                ctr_type = rw.peek_bytestring(4)
        else:
            for obj in self.MXMIs:
                rw.rw_obj(obj)
                
    def checkMXMIType(self, value):
        if type(value) is not MXMIReadWriter:
            raise TypeError(f"MXMIArray object expected an MXMIReadWriter, received '{type(value)}'.")
                
    def __iter__(self):
        for obj in self.MXMIs:
            yield obj
            
    def __len__(self):
        return len(self.MXMIs)

    def __getitem__(self, idx):
        return self.MXMIs[idx]
    
    def __setitem__(self, idx, value):
        self.checkMXMIType(value)
        self.MXMIs[idx] = value
        
    def append(self, value):
        self.checkMXMIType(value)
        self.MXMIs.append(value)
    