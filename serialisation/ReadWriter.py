import array
import struct

if (__name__ == "__main__"):
    from Utils import chunk_list, flatten_list
else:
    from .Utils import chunk_list, flatten_list


class ReadWriterBase:
    open_flags=None
    
    type_sizes = {
        'x': 1,  # pad byte
        'c': 1,  # char
        'b': 1,  # int8
        'B': 1,  # uint8
        '?': 1,  # bool
        'h': 2,  # int16
        'H': 2,  # uint16
        'i': 4,  # int32
        'I': 4,  # uint32
        'l': 4,  # int32
        'L': 4,  # uint32
        'q': 8,  # int64
        'Q': 8,  # uint64
        'e': 2,  # half-float
        'f': 4,  # float
        'd': 8   # double
    }
    
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
        
    # Interface functions
    
    def rw_obj(self, obj):
        obj.read_write(self)
        
    def tell(self):
        return self.bytestream.tell()
    
    def seek(self, offset):
        self.bytestream.seek(offset)
        
    def rw_single(self, typecode, value, endianness=None):
        self._rw_single(typecode, self.type_sizes[typecode], value, endianness)
        
    def rw_multiple(self, typecode, value, shape, endianness=None):
        self._rw_multiple(typecode, self.type_sizes[typecode], value, shape, endianness)
        
    def align_with(self, offset, alignment, typecode, value, endianness=None):
        if endianness is None:
            endianness = self.endianness
        padval = struct.pack(typecode, value)
        self.align(offset, alignment, padval)
        
    def align_to(self, offset, width, typecode, value, endianness=None):
        alignment = width * self.type_sizes[typecode]
        self.align_with(offset, alignment, typecode, value, endianness)
        
    # Pure virtual functions
    
    def _rw_single(self, typecode, size, value, endianness=None):
        raise NotImplementedError
        
    def _rw_multiple(self, typecode, size, value, shape, endianness=None):
        raise NotImplementedError
        
    def _rw_str(self, value, length, encoding='ascii'):
        raise NotImplementedError
        
    def _rw_cstr(self, value, encoding='ascii'):
        raise NotImplementedError

    def align(self, offset, alignment, padval=b'\x00'):
        raise NotImplementedError

    def is_at_eof(self):
        raise NotImplementedError
        
    # RW functions (should be defined in a loop...)
    def rw_int8   (self, value, endianness=None): self._rw_single('b', 1, value, endianness)
    def rw_uint8  (self, value, endianness=None): self._rw_single('B', 1, value, endianness)
    def rw_int16  (self, value, endianness=None): self._rw_single('h', 2, value, endianness)
    def rw_uint16 (self, value, endianness=None): self._rw_single('H', 2, value, endianness)
    def rw_int32  (self, value, endianness=None): self._rw_single('i', 4, value, endianness)
    def rw_uint32 (self, value, endianness=None): self._rw_single('I', 4, value, endianness)
    def rw_int64  (self, value, endianness=None): self._rw_single('q', 8, value, endianness)
    def rw_uint64 (self, value, endianness=None): self._rw_single('Q', 8, value, endianness)
    def rw_float16(self, value, endianness=None): self._rw_single('e', 2, value, endianness)
    def rw_float32(self, value, endianness=None): self._rw_single('f', 4, value, endianness)
    def rw_float64(self, value, endianness=None): self._rw_single('d', 8, value, endianness)
    
    def rw_int8s   (self, value, shape, endianness=None): self._rw_multiple('b', 1, value, shape, endianness)
    def rw_uint8s  (self, value, shape, endianness=None): self._rw_multiple('B', 1, value, shape, endianness)
    def rw_int16s  (self, value, shape, endianness=None): self._rw_multiple('h', 2, value, shape, endianness)
    def rw_uint16s (self, value, shape, endianness=None): self._rw_multiple('H', 2, value, shape, endianness)
    def rw_int32s  (self, value, shape, endianness=None): self._rw_multiple('i', 4, value, shape, endianness)
    def rw_uint32s (self, value, shape, endianness=None): self._rw_multiple('I', 4, value, shape, endianness)
    def rw_int64s  (self, value, shape, endianness=None): self._rw_multiple('q', 8, value, shape, endianness)
    def rw_uint64s (self, value, shape, endianness=None): self._rw_multiple('Q', 8, value, shape, endianness)
    def rw_float16s(self, value, shape, endianness=None): self._rw_multiple('e', 2, value, shape, endianness)
    def rw_float32s(self, value, shape, endianness=None): self._rw_multiple('f', 4, value, shape, endianness)
    def rw_float64s(self, value, shape, endianness=None): self._rw_multiple('d', 8, value, shape, endianness)
    
class Reader(ReadWriterBase):
    open_flags = "rb"
    
    def _rw_single(self, typecode, size, value, endianness=None):
        if endianness is None:
            endianness = self.endianness
        return struct.unpack(endianness + typecode, self.bytestream.read(size))
        
    def _rw_multiple(self, typecode, size, value, shape, endianness=None):
        if endianness is None:
            endianness = self.endianness
            
        if not hasattr(shape, "__getitem__"):
            shape = (shape,)
        n_to_read = 1
        for elem in shape:
            n_to_read *= elem
            
        data = array.array(typecode, struct.unpack(endianness + typecode*n_to_read, self.bytestream.read(size*n_to_read)))
        # Group the lists up
        # Skip the outer index because we don't need it (we'll automatically
        # get an end result of that length) and create groups by iterating
        # over the shape in reverse
        for subshape in shape[1::][::-1]:
            data = chunk_list(data, subshape)
        return data
        
    def _rw_str(self, value, length, encoding='ascii'):
        return self.bytestream.read(length).decode(encoding)
        
    def _rw_cstr(self, value, encoding='ascii'):
        out = b""
        while ((val := self.bytearray.read(1)) != b'\x00'):
            out += val
        return out.decode(encoding)
    
    def align(self, offset, alignment, padval=b'\x00'):
        n_to_read = (alignment - (offset % alignment)) % alignment
        data = self.bytestream.read(n_to_read)
        expected = padval * (len(data) // len(padval))
        assert data == expected, f"Unexpected padding: Expected {expected}, read {data}."
        
class Writer(ReadWriterBase):
    open_flags = "wb"
    
    def _rw_single(self, typecode, size, value, endianness=None):
        if endianness is None:
            endianness = self.endianness
        self.bytestream.write(struct.pack(endianness + typecode, value))
        return value
            
    def _rw_multiple(self, typecode, size, value, shape, endianness=None):
        if endianness is None:
            endianness = self.endianness
        
        if not hasattr(shape, "__getitem__"):
            shape = (shape,)
        n_to_read = 1
        for elem in shape:
            n_to_read *= elem
            
        data = value # Shouldn't need to deepcopy since flatten_list will copy
        for _ in range(len(shape)-1):
            data = flatten_list(data)
        self.bytestream.write(endianness + typecode*n_to_read, *data)
        return value
        
    def _rw_str(self, value, length, encoding='ascii'):
        self.bytestream.write(value.encode(encoding))
        return value
        
    def _rw_cstr(self, value, encoding='ascii'):
        out = value.encode(encoding) + b'\x00'
        self.bytestream.write(out)
        return value
    
    def align(self, offset, alignment, padval=b'\x00'):
        n_to_read = (alignment - (offset % alignment)) % alignment
        data = padval * (n_to_read // len(padval))
        self.bytestream.write(data)
        