from pyValkLib.serialisation.BaseRW import BaseRW, ViolatedAssumptionError


class BadMagicValueError(Exception):
    def __init__(self, ftype):
        super().__init__(f'Expected an ascii-decodable string, received \'{ftype}\'.')
        
class UnimplementedFiletypeError(Exception):
    def __init__(self, ftype):
        super().__init__(f'File type \'{ftype}\' not defined.')
        

class PointerIndexableArray:
    def __init__(self):
        self.data = []
        self.ptr_to_idx = {}
        self.idx_to_ptr = []
        
        
class Header16B(BaseRW):
    __slots__ = ("filetype", "contents_length", "header_length", "flags")
    
    def __init__(self, endianness=None):
        super().__init__(endianness)
        self.filetype = None
        self.contents_length = None
        self.header_length = None
        self.flags = None     
        
    def read_write(self):
        self.rw_ascii("filetype", 4)
        self.rw_var("contents_length", "I")
        self.rw_var("header_length", "I")
        self.rw_var("flags", "I")
        
class Header32B(BaseRW):
    __slots__ = ("filetype", "contents_length", "header_length", "flags",
                 "depth", "data_length", "unknown_0x18", "unknown_0x1C")
    
    def __init__(self, endianness=None):
        super().__init__(endianness)
        self.filetype = None
        self.contents_length = None
        self.header_length = None
        self.flags = None
        
        self.depth = None
        self.data_length = None
        self.unknown_0x18 = None
        self.unknown_0x1C = None
        
    def read_write(self):
        self.rw_ascii("filetype", 4)
        self.rw_var("contents_length", "I")
        self.rw_var("header_length", "I")
        self.rw_var("flags", "I")
        
        self.rw_var("depth", "I")
        self.rw_var("data_length", "I")
        self.rw_var("unknown_0x18", "I")
        self.rw_var("unknown_0x1C", "I")
        
        self.assert_is_zero("unknown_0x18")
        self.assert_is_zero("unknown_0x1C")
        
class ValkyriaBaseRW(BaseRW):
    __slots__ = ("start_position", "header", "containers", "subcontainers")
    FILETYPE = None
    
    def __init__(self, containers, endianness=None):
        super().__init__(endianness)
        self.start_position = None
        self.header = None
        self.containers = containers
        self.subcontainers = []
        
        
    def local_tell(self):
        return self.bytestream.tell() - self.start_position
    
    def local_seek(self, pos, whence=0):
        return self.bytestream.seek(self.start_position + pos, whence)
    
    def global_tell(self):
        return self.bytestream.tell()
    
    def check_header_size(self):
        self.assert_local_file_pointer_now_at(self.header.header_length)
        
    def check_contents_size(self):
        try:
            self.assert_local_file_pointer_now_at(self.header.contents_length + self.header.header_length)
        except Exception as e:
            print("FUCKED UP ON", self.filetype, ":", e)
            print("Start pos: ", self.start_position)
            print("header len:", self.header.header_length)
            print("body len:  ", self.header.contents_length)
            raise e
        
    def convert_to_local_position(self, position):
        return position - self.start_position
    
    def convert_to_global_position(self, position):
        return position + self.start_position
        
    def assert_local_file_pointer_now_at(self, location, file_pointer_location=None, use_hex=False):
        if file_pointer_location is None:
            file_pointer_location = self.local_tell()
        if file_pointer_location != location:
            if use_hex:
                size = lambda x : len(f'{x:0x}')
                formatter = lambda x: f"0x{x:0{size(x) + (((size(x) + 1)//2) - (size(x) // 2))}x}"
            else:
                formatter = lambda x: x
            raise ViolatedAssumptionError(f"Local file pointer at {formatter(file_pointer_location)}, not at {formatter(location)}.")

    def read_write_contents(self):
        raise NotImplementedError()
        
    def read_write_subcontainers(self):
        for subcontainer in self.subcontainers:
            self.rw_readwriter(subcontainer)
    
class ValkyriaBaseRW16BH(ValkyriaBaseRW):
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        self.header = Header16B()
        
    def read_write(self):
        self.start_position = self.global_tell()
        
        self.rw_readwriter(self.header)
        if self.FILETYPE != self.header.filetype:
            raise TypeError(f"Container is {self.header.filetype}, expected {self.FILETYPE}.")
        self.check_header_size()
        self.read_write_contents()
        self.read_write_subcontainers()
        self.check_contents_size()
        
class ValkyriaBaseRW32BH(ValkyriaBaseRW):
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        self.header = Header32B()
        
    def check_data_size(self):
        self.assert_local_file_pointer_now_at(self.header.header_length + self.header.data_length)
        
    def read_write(self):
        self.start_position = self.global_tell()
        
        self.rw_readwriter(self.header)
        if self.FILETYPE != self.header.filetype:
            raise TypeError(f"Container is {self.header.filetype}, expected {self.FILETYPE}.")
        self.check_header_size()
        self.read_write_contents()
        self.check_data_size()
        self.read_write_subcontainers()
        self.check_contents_size()