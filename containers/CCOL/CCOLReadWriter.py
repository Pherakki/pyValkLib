from pyValkLib.serialisation.ValkSerializable import Context, Serializable, ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray

from pyValkLib.containers.Metadata.POF0.POF0ReadWriter import POF0ReadWriter
from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

class Collider(Serializable):
    def __init__(self, endianness=None):
        super().__init__(Context())
        if endianness is not None:
            self.context.endianness = endianness
        
        self.filetype = None
        self.contents = []
        
    def read_write(self, rw):
        self.filetype = rw.rw_str(self.filetype, 4)
        self.contents = rw.rw_uint32s(self.contents, 0x0F)
        
    def __repr__(self):
        return f"{self.filetype} {self.contents}"

class ColliderData(Serializable):
    def __init__(self, endianness=None):
        super().__init__(Context())
        if endianness is not None:
            self.context.endianness = endianness
        
        self.header = []
        self.contents = []
        
    def read_write(self, rw, count):
        self.header = rw.rw_float32s(self.header, 8)
        self.contents = rw.rw_float32s(self.contents, 4*count)
        
    def __repr__(self):
        return f"{self.header} {self.contents}"

class CCOLReadWriter(ValkSerializable32BH):
    FILETYPE = "CCOL"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.data_length = 0
        self.header.flags = 0x18000000
        self.POF0 = POF0ReadWriter("<")
        self.ENRS = ENRSReadWriter("<")
        self.EOFC = EOFCReadWriter("<")
        
        self.unknown_1       = None
        self.container_count = None
        self.unknown_3       = None
        self.unknown_4       = None
        
        self.colliders = []
        self.collider_data = PointerIndexableArray(self.context)

    def get_subcontainers(self):
        return [self.POF0, self.ENRS, self.EOFC]
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))
        
        self.unknown_1       = rw.rw_uint32(self.unknown_1)
        self.container_count = rw.rw_uint32(self.container_count) # Container count
        self.unknown_3       = rw.rw_uint32(self.unknown_3)
        self.unknown_4       = rw.rw_uint32(self.unknown_4)
        
        if rw.mode() == "read":
            self.colliders = [Collider(self.context.endianness) for _ in range(self.container_count)]
        for ctr in self.colliders:
            rw.rw_obj(ctr)

        prev_ptr = 0
        i = 0
        for ctr in sorted(self.colliders, key=lambda x: x.contents[3]):
            ptr = ctr.contents[3]
            if ptr == prev_ptr:
                continue
            
            rw.assert_local_file_pointer_now_at(f"Collider Data {i}:", ptr)
            if rw.mode() == "read":
                self.collider_data.data.append(ColliderData(self.context.endianness))
                self.collider_data.idx_to_ptr[i] = ptr
                self.collider_data.ptr_to_idx[ptr] = i
            rw.rw_obj(self.collider_data.data[i], ctr.contents[2])
            
            prev_ptr = ptr
            i += 1
            
    def __repr__(self):
        return f"CCOL Object [{self.header.depth}] [0x{self.header.flags:0>8x}]."

