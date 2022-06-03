import array
import struct

class ReadWriterBase:
    def __init__(self, filename):
        self.filename = filename
        self.endianness = "<"
        self.bytestream = None
        
    # Context managers are a decent approximation of RAII behaviour
    def __enter__(self):
        self.bytestream = open(self.filename, 'rb')
        return self
        
    def __exit__(self, exc_type, exc_val, traceback):
        self.bytestream.close()
        self.bytestream = None
        
    def _rw_single(self, typecode, size, value, endianness=None):
        raise NotImplementedError
        
    def rw_uint8(self, var, endianness=None):
        return self._rw_single("b", 1, var, endianness)
        
class Reader(ReadWriterBase):
    def _rw_single(self, typecode, size, value, endianness=None):
        if endianness is None:
            endianness = self.endianness
        return struct.unpack(endianness + typecode, self.bytestream.read(size))
    
class Writer(ReadWriterBase):
    def _rw_single(self, typecode, size, value, endianness=None):
        if endianness is None:
            endianness = self.endianness
        return  self.bytestream.write(struct.pack(endianness + typecode, value))
        