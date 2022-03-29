from BaseRW import BaseRW, ViolatedAssumptionError


class BadMagicValueError(Exception):
    def __init__(self, ftype):
        super().__init__(f'Expected an ascii-decodable string, received \'{ftype}\'.')
        
class UnimplementedFiletypeError(Exception):
    def __init__(self, ftype):
        super().__init__(f'File type \'{ftype}\' not defined.')
        
class ValkyriaBaseRW(BaseRW):
    __slots__ = ("start_position", "header", "filetype")
    
    def __init__(self, endianness=None):
        super().__init__(endianness)
        self.filetype = None
        self.start_position = None
        self.header = None
        
        
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
            print("header len:", self.header_length)
            print("body len:  ", self.contents_length)
            # raise e
        
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
    
