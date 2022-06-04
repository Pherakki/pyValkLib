from .Serializable import Serializable
    
        
class Header16B(Serializable):
    __slots__ = ("filetype", "contents_length", "header_length", "flags")
    
    def __init__(self, endianness=None):
        super().__init__(endianness)
        self.filetype = None
        self.contents_length = None
        self.header_length = None
        self.flags = None     
        
    def read_write(self, rw):
        self.filetype        = rw.rw_str(self.filetype, 4)
        self.contents_length = rw.rw_uint32(self.contents_length)
        self.header_length   = rw.rw_uint32(self.header_length)
        self.flags           = rw.rw_uint32(self.flags)
        
    def __repr__(self):
        return f"::0x10 Header:: Filetype: {self.filetype}, Contents Size: {self.contents_length}, Header Size: {self.header_length}, Flags: 0x{self.flags:0>8x}"
        
class Header32B(Serializable):
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
        
    def read_write(self, rw):
        self.filetype        = rw.rw_str(self.filetype, 4)
        self.contents_length = rw.rw_uint32(self.contents_length)
        self.header_length   = rw.rw_uint32(self.header_length)
        self.flags           = rw.rw_uint32(self.flags)
        
        self.depth           = rw.rw_uint32(self.depth)
        self.data_length     = rw.rw_uint32(self.data_length)
        self.unknown_0x18    = rw.rw_uint32(self.unknown_0x18)
        self.unknown_0x1C    = rw.rw_uint32(self.unknown_0x1C)
        
        rw.assert_is_zero(self.unknown_0x18)
        rw.assert_is_zero(self.unknown_0x1C)

                
    def __repr__(self):
        return f"::0x20 Header:: Filetype: {self.filetype}, Contents Size: {self.contents_length}, Header Size: {self.header_length}, Flags: 0x{self.flags:0>8x}, Depth: {self.depth}, Data Size: {self.data_length}"
        
    
class ValkSerializable(Serializable):
    FILETYPE=None
    
    def __init__(self, containers, endianness=None):
        super().__init__(endianness)
        self.header = None
        self.containers = containers
        self.subcontainers = []
        
    # RW methods
    
    def read_write(self, rw):
        self.context.anchor_pos = rw.global_tell()
        
        self.header = rw.rw_obj(self.header)
        if self.FILETYPE != self.header.filetype:
            raise TypeError(f"Container is {self.header.filetype}, expected {self.FILETYPE}.")
        self.check_header_size(rw)
        self.read_write_contents(rw)
        self.check_data_size(rw)
        self.read_write_subcontainers(rw)
        self.check_contents_size(rw)

    def check_header_size(self, rw):
        rw.assert_local_file_pointer_now_at(self.header.header_length)
        
    def read_write_contents(self):
        raise NotImplementedError()
        
    def check_data_size(self):
        raise NotImplementedError()
        
    def read_write_subcontainers(self, rw):
        for subcontainer in self.subcontainers:
            rw.rw_obj(subcontainer)
            
    def check_contents_size(self, rw):
        try:
            rw.assert_local_file_pointer_now_at(self.header.contents_length + self.header.header_length)
        except Exception as e:
            print("FUCKED UP ON", self.FILETYPE, ":", e)
            print("Start pos:  ", self.context.anchor_pos)
            print("header len: ", self.header.header_length)
            print("body len:   ", self.header.contents_length)
            raise e
    
class ValkSerializable16BH(ValkSerializable):
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        self.header = Header16B()
        self.header.context.anchor_pos = self.context.anchor_pos
        self.header.endianness = "<"
        
    def check_data_size(self):
        pass
    
class ValkSerializable32BH(ValkSerializable):
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        self.header = Header32B()
        self.header.context.anchor_pos = self.context.anchor_pos
        self.header.context.endianness = "<"
        
    def check_data_size(self, rw):
        rw.assert_local_file_pointer_now_at(self.header.header_length + self.header.data_length)
