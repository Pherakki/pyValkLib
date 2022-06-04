import io
import struct

class ViolatedAssumptionError(Exception):
    pass

def chunk_list(lst, chunksize):
    """
    Splits a 1D list into sub-lists of size 'chunksize', return returns those sub-lists inside a new 2D list.

    Inputs
    ------
    lst -- a 1D list
    chunksize -- the size of each sub-list of the result

    Returns
    ------
    THe 1D input 'lst' converted to a 2D list, where each sub-list has length 'chunksize'.
    """
    return [lst[i:i + chunksize] for i in range(0, len(lst), chunksize)]

def flatten_list(lst):
    return [subitem for item in lst for subitem in item]


class BaseRW:
    """
    This is a base class for bytestream parsing, intended to be able to read/write (RW) these bytestreams to/from files.
    """
    pad_byte = b'\x00'

    type_buffers = {
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

    def __init__(self, endianness=None):
        self.bytestream = None
        self.endianness = endianness if endianness is not None else '<'
        
        self.rw_var = None
        self.rw_varlist = None
        self.rw_listoflists = None
        self.rw_varobject = None
        self.rw_readwriter = None
        self.rw_ascii = None
        self.rw_bytes = None
        self.rw_method = None
        self.cleanup_ragged_chunk = None


    ################
    # INIT HELPERS #
    ################
    def set_file_rw(self, io_object):
        assert (type(io_object) == io.BufferedReader) or (type(io_object) == io.BufferedWriter), \
            f"Read-write object was instantiated with a {type(io_object)}, not a {io.BufferedReader} or " \
            f"{io.BufferedWriter}. Ensure you are instantiating this object with a file opened in 'rb' or 'wb' mode."
        self.bytestream = io_object
        
    def setup_rw(self, dtype, src, endianness):
        if len(dtype) != 1:
            raise ValueError(f"'dtype' must be a single character, received {dtype}.")
        if src is None:
            src = self
        if endianness is None:
            endianness = self.endianness
        return src, endianness

    ##################
    # STRUCT OVERLAY #
    ##################
    def unpack(self, dtype, endianness=None):
        if endianness is None:
            endianness = self.endianness
        buf = sum([self.type_buffers[dt] for dt in dtype])
        return struct.unpack(f"{endianness}{dtype}", self.bytestream.read(buf))
    
    def pack(self, value, dtype, endianness=None):
        if endianness is None:
            endianness = self.endianness
        return struct.pack(f"{endianness}{dtype}", *value)

    ##########
    # RW VAR #
    ##########
    def read_var(self, variable, dtype, endianness=None, src=None):
        src, endianness = self.setup_rw(dtype, src, endianness)
        setattr(src, variable, self.unpack(dtype, endianness)[0])

    def write_var(self, variable, dtype, endianness=None, src=None):
        src, endianness = self.setup_rw(dtype, src, endianness)
        
        val = getattr(src, variable)
        to_write = self.pack((val,), dtype, endianness)
        self.bytestream.write(to_write)

    ##############
    # RW VARLIST #
    ##############
    def read_varlist(self, variable, dtype, n_vars, endianness=None, src=None):
        src, endianness = self.setup_rw(dtype, src, endianness)
        setattr(src, variable, self.unpack(dtype*n_vars, endianness))

    def write_varlist(self, variable, dtype, n_vars, endianness=None, src=None):
        src, endianness = self.setup_rw(dtype, src, endianness)
        
        val = getattr(src, variable)
        to_write = self.pack(val, dtype*n_vars, endianness)
        self.bytestream.write(to_write)

    # ###############
    # # RW VARLISTS #
    # ###############
    def read_listoflists(self, variable, dtype, item_size, endianness=None):
        val = chunk_list(self.unpack(dtype*item_size, endianness), len(dtype))
        setattr(self, variable, val)
        
    def write_listoflists(self, variable, dtype, item_size, endianness=None):
        val = getattr(self, variable)
        to_write = self.pack(flatten_list(val), dtype*item_size, endianness)
        self.bytestream.write(to_write)
        
    #################
    # RW READWRITER #
    #################
    def read_readwriter(self, rw):
        rw.read(self.bytestream)
        
    def write_readwriter(self, rw):
        rw.write(self.bytestream)
    
    ############
    # RW ASCII #
    ############
    def read_ascii(self, variable, num_bytes=None, src=None):
        if src is None:
            src = self
        bytes_to_read = [] if num_bytes is None else [num_bytes]
        val = self.bytestream.read(*bytes_to_read).decode('ascii')
        setattr(src, variable, val)

    def write_ascii(self, variable, num_bytes=None, src=None):
        if src is None:
            src = self
        val = getattr(src, variable)
        if num_bytes is not None:
            assert len(val) == num_bytes, f"String to write [{val}] is not equal to the number of bytes [{num_bytes}]."
        self.bytestream.write(val.encode('ascii'))

    ############
    # RW BYTES #
    ############
    def read_bytes(self, variable, num_bytes=None, src=None):
        if src is None:
            src = self
        bytes_to_read = [] if num_bytes is None else [num_bytes]
        val = self.bytestream.read(*bytes_to_read)
        setattr(src, variable, val)

    def write_bytes(self, variable, num_bytes=None, src=None):
        if src is None:
            src = self
        val = getattr(src, variable)
        if num_bytes is not None:
            assert len(val) == num_bytes, "Bytes to write is not equal to the number of bytes."
        self.bytestream.write(val)

    #################
    # CLEANUP CHUNK #
    #################
    def cleanup_ragged_chunk_read(self, position, chunksize, stepsize=1, bytevalue=b'\x00'):
        """
        If 'position' is partially through a chunk, this function will check that the remaining bytes in the chunk
        are pad bytes.
        """
        bytes_read_from_final_chunk = position % chunksize
        # The modulo maps {bytes_read_from_final_chunk == 0} to {0} rather than {chunksize}
        num_bytes_left_to_read = (chunksize - bytes_read_from_final_chunk) % chunksize
        should_be_value_bytes = self.bytestream.read(num_bytes_left_to_read)
        assert should_be_value_bytes == bytevalue * (num_bytes_left_to_read // stepsize), f"Assumed padding data was not {bytevalue}: {should_be_value_bytes}"

    def cleanup_ragged_chunk_write(self, position, chunksize, stepsize=1, bytevalue=b'\x00'):
        """
        If 'position' is partially through a chunk, this function will complete the chunk with pad bytes.
        """
        bytes_read_from_final_chunk = position % chunksize
        # The modulo maps {bytes_read_from_final_chunk == 0} to {0} rather than {chunksize}
        num_bytes_left_to_read = (chunksize - bytes_read_from_final_chunk) % chunksize
        self.bytestream.write(bytevalue * (num_bytes_left_to_read // stepsize))

    #######################
    # INTERFACE FUNCTIONS #
    #######################
    def set_template_methods(self, bytestream, rw_method):
        if rw_method == "read":
            self.set_read_template_methods()
        elif rw_method == "write":
            self.set_write_template_methods()
        else:
            assert 0, f"Unknown rw method {rw_method}."
        self.set_file_rw(bytestream)
    
    def set_read_template_methods(self):
        self.rw_var = self.read_var
        self.rw_varlist = self.read_varlist
        self.rw_listoflists = self.read_listoflists
        self.rw_readwriter = self.read_readwriter
        self.rw_ascii = self.read_ascii
        self.rw_bytes = self.read_bytes
        self.cleanup_ragged_chunk = self.cleanup_ragged_chunk_read
        self.rw_method = "read"
        
    def read(self, bytestream, *args, method=None, **kwargs):
        if method == None:
            method = self.read_write
            
        # Set Template methods
        self.set_file_rw(bytestream)
        self.set_read_template_methods()
        
        try:
            method(*args, **kwargs)
        finally:
            self.reset_rw_functions()
            
    def set_write_template_methods(self):
        self.rw_var = self.write_var
        self.rw_varlist = self.write_varlist
        self.rw_listoflists = self.write_listoflists
        self.rw_readwriter = self.write_readwriter
        self.rw_ascii = self.write_ascii
        self.rw_bytes = self.write_bytes
        self.cleanup_ragged_chunk = self.cleanup_ragged_chunk_write
        self.rw_method = "write"
        
    def write(self, bytestream, *args, method=None, **kwargs):
        if method == None:
            method = self.read_write
            
        # Set Template methods
        self.set_file_rw(bytestream)
        self.set_write_template_methods()
        
        try:
            method(*args, **kwargs)
        finally:
            self.reset_rw_functions()
        
    def read_write(self):
        """
        Virtual function to be overridden by subclasses.
        """
        raise NotImplementedError
        
    def reset_rw_functions(self):
        self.bytestream = None
        self.rw_var = None
        self.rw_varlist = None
        self.rw_listoflists = None
        self.rw_readwriter = None
        self.rw_ascii = None
        self.rw_bytes = None
        self.cleanup_ragged_chunk = None
        self.rw_method = None
                
    def run_rw_method(self, method, *args, **kwargs):
        # Set Template methods
        obj = method.__self__
        obj.set_file_rw(self.bytestream)
        obj.set_template_methods(self.bytestream, self.rw_method)
        
        try:
            method(*args, **kwargs)
        finally:
            obj.reset_rw_functions()
            
    #############################
    # DATA VALIDATION FUNCTIONS #
    #############################
    def assert_file_pointer_now_at(self, location, file_pointer_location=None, use_hex=False):
        if file_pointer_location is None:
            file_pointer_location = self.bytestream.tell()
        if file_pointer_location != location:
            if use_hex:
                size = lambda x : len(f'{x:0x}')
                formatter = lambda x: f"0x{x:0{size(x) + (((size(x) + 1)//2) - (size(x) // 2))}x}"
            else:
                formatter = lambda x: x
            raise ViolatedAssumptionError(f"File pointer at {formatter(file_pointer_location)}, not at {formatter(location)}.")
            
    def assert_equal(self, varname, value, obj=None, formatter=lambda x: x):
        if obj is None:
            obj = self
        if getattr(obj, varname) != value:
            raise ViolatedAssumptionError(f"{varname} != {formatter(value)}, value is {formatter(getattr(obj, varname))}")

    def assert_is_zero(self, varname, obj=None, formatter=lambda x: x):
        if obj is None:
            obj = self
        self.assert_equal(varname, 0, obj=obj, formatter=formatter)

    def assert_equal_to_any(self, varname, *values, obj=None):
        if obj is None:
            obj = self
        if getattr(obj, varname) not in set(values):
            raise ViolatedAssumptionError(f"{varname} is not any of {','.join([str(e) for e in values])}, value is {getattr(obj, varname)}")
