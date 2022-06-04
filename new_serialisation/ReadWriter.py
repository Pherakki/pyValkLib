import array
import struct

class Serializable:
    def read(self, filepath):
        with Reader(filepath) as rw:
            self.read_write(rw)
            
    def write(self, filepath):
        with Writer(filepath) as rw:
            self.read_write(rw)
            
    def read_write(self, rw):
        raise NotImplementedError

class ReadWriterBase:
    open_flags=None
    
    def __init__(self, filename):
        self.filename = filename
        self.endianness = "<"
        self.bytestream = None
        
    # Context managers are a decent approximation of RAII behaviour
    def __enter__(self):
        self.bytestream = open(self.filename, self.open_flags)
        return self
        
    def __exit__(self, exc_type, exc_val, traceback):
        self.bytestream.close()
        self.bytestream = None
        
    def _rw_single(self, typecode, size, value, endianness=None):
        raise NotImplementedError
        
    def rw_uint8(self, var, endianness=None):
        return self._rw_single("b", 1, var, endianness)
        
class Reader(ReadWriterBase):
    open_flags = "rb"
    
    def _rw_single(self, typecode, size, value, endianness=None):
        if endianness is None:
            endianness = self.endianness
        return struct.unpack(endianness + typecode, self.bytestream.read(size))
    
class Writer(ReadWriterBase):
    open_flags = "wb"
    
    def _rw_single(self, typecode, size, value, endianness=None):
        if endianness is None:
            endianness = self.endianness
        self.bytestream.write(struct.pack(endianness + typecode, value))
        return value
        