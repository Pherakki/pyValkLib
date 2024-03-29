import copy
from .ReadWriter import POF0Builder, ENRSBuilder
from .Serializable import Serializable, Context
    
        
class Header16B(Serializable):
    __slots__ = ("filetype", "contents_length", "header_length", "flags")
    
    def __init__(self, context, filetype):
        super().__init__(context)
        self.filetype = filetype
        self.contents_length = None
        self.header_length = 0x10
        self.flags = None     
        
    def read_write(self, rw):
        self.filetype        = rw.rw_str(self.filetype, 4)
        self.contents_length = rw.rw_uint32(self.contents_length)
        self.header_length   = rw.rw_uint32(self.header_length)
        self.flags           = rw.rw_uint32(self.flags)
        
    def __repr__(self):
        return f"::0x10 Header:: Filetype: {self.filetype}, Contents Size: {self.contents_length}, Header Size: {self.header_length}, Flags: 0x{self.flags:0>8x}"
        
    def info_string(self):
        flagline = f"{self.flags}" if self.flags is None else f"0x{self.flags:0>8x}"
        return f"[{flagline}]"
    
class Header32B(Serializable):
    __slots__ = ("filetype", "contents_length", "header_length", "flags",
                 "depth", "data_length", "padding_0x18", "padding_0x1C")
    
    def __init__(self, context, filetype):
        super().__init__(context)
        self.filetype = filetype
        self.contents_length = None
        self.header_length = 0x20
        self.flags = None
        
        self.depth = None
        self.data_length = None
        self.padding_0x18 = 0
        self.padding_0x1C = 0
        
    def read_write(self, rw):
        self.filetype        = rw.rw_str(self.filetype, 4)
        self.contents_length = rw.rw_uint32(self.contents_length)
        self.header_length   = rw.rw_uint32(self.header_length)
        self.flags           = rw.rw_uint32(self.flags)
        
        self.depth           = rw.rw_uint32(self.depth)
        self.data_length     = rw.rw_uint32(self.data_length)
        self.padding_0x18    = rw.rw_uint32(self.padding_0x18)
        self.padding_0x1C    = rw.rw_uint32(self.padding_0x1C)
        
        #rw.assert_is_zero(self.padding_0x18)
        rw.assert_is_zero(self.padding_0x1C)

    def info_string(self):
        flagline = f"{self.flags}" if self.flags is None else f"0x{self.flags:0>8x}"
        return f"[{self.depth}] [{flagline}]"
    
    def __repr__(self):
        return f"::0x20 Header:: Filetype: {self.filetype}, Contents Size: {self.contents_length}, Header Size: {self.header_length}, Flags: 0x{self.flags:0>8x}, Depth: {self.depth}, Data Size: {self.data_length}"
        
class Header48B(Serializable):
    __slots__ = ("filetype", "contents_length", "header_length", "flags",
                 "depth", "data_length", "padding_0x18", "padding_0x1C",
                 "unknown_0x20", "unknown_0x24", "unknown_0x28", "unknown_0x2C")
    
    def __init__(self, context, filetype):
        super().__init__(context)
        self.filetype = filetype
        self.contents_length = None
        self.header_length = 0x30
        self.flags = None
        
        self.depth = None
        self.data_length = None
        self.padding_0x18 = 0
        self.padding_0x1C = 0
        
        self.unknown_0x20    = None
        self.unknown_0x24    = None
        self.unknown_0x28    = None
        self.unknown_0x2C    = None
        
    def read_write(self, rw):
        self.filetype        = rw.rw_str(self.filetype, 4)
        self.contents_length = rw.rw_uint32(self.contents_length)
        self.header_length   = rw.rw_uint32(self.header_length)
        self.flags           = rw.rw_uint32(self.flags)
        
        self.depth           = rw.rw_uint32(self.depth)
        self.data_length     = rw.rw_uint32(self.data_length)
        self.padding_0x18    = rw.rw_uint32(self.padding_0x18)
        self.padding_0x1C    = rw.rw_uint32(self.padding_0x1C)
        
        rw.assert_is_zero(self.padding_0x18)
        rw.assert_is_zero(self.padding_0x1C)
        
        self.unknown_0x20    = rw.rw_uint32(self.unknown_0x20)
        self.unknown_0x24    = rw.rw_uint32(self.unknown_0x24)
        self.unknown_0x28    = rw.rw_uint32(self.unknown_0x28)
        self.unknown_0x2C    = rw.rw_uint32(self.unknown_0x2C)

    def info_string(self):
        flagline = f"{self.flags}" if self.flags is None else f"0x{self.flags:0>8x}"
        return f"[{self.depth}] [{flagline}]"
    
    def __repr__(self):
        return f"::0x30 Header:: Filetype: {self.filetype}, Contents Size: {self.contents_length}, Header Size: {self.header_length}, Flags: 0x{self.flags:0>8x} "\
               f"Depth: {self.depth}, Data Size: {self.data_length}" \
               f"Unk0x20: {self.unknown_0x20}, Unk0x24: {self.unknown_0x24}, Unk0x28: {self.unknown_0x28}, Unk0x2C: {self.unknown_0x2C}"
        
class ValkSerializable(Serializable):
    FILETYPE=None
    
    def __init__(self, containers, endianness=None):
        context = Context()
        if endianness is not None:
            context.endianness = endianness 
        super().__init__(context)
        self.header = None
        self.start_pos = None
        self.containers = containers
        
    
    def __repr__(self):
        subcon = self.get_subcontainers()
        containsline = f": Contains {', '.join(o.FILETYPE for o in subcon)}" if len(subcon) else ""
        return f"{self.FILETYPE} Object {self.header.info_string()}{containsline}"
        
    # RW methods
    
    def read_write(self, rw):
        # Tell the RW that any local ops should be done relative to this container's origin!
        old_origin = rw.anchor_pos
        self.start_pos = rw.global_tell()
        rw.anchor_pos = self.start_pos
        
        try:
            self.header = rw.rw_obj(self.header)
        except Exception as e:
            raise Exception(f"Failed to read header on {self.FILETYPE}: {e}") from e
            
        if self.FILETYPE != self.header.filetype:
            raise TypeError(f"Container is {self.header.filetype}, expected {self.FILETYPE}.")
        self.check_header_size(rw)
        self.read_write_contents(rw)
        self.check_data_size(rw)
        container_origin = rw.anchor_pos
        self.read_write_subcontainers(rw)
        rw.anchor_pos = container_origin
        self.check_contents_size(rw)
        rw.anchor_pos = old_origin

    def check_header_size(self, rw):
        rw.assert_local_file_pointer_now_at(f"{self.FILETYPE}: End-Of-Header", self.header.header_length)
        
    def read_write_contents(self, rw):
        raise NotImplementedError()
        
    def check_data_size(self, rw):
        raise NotImplementedError()
        
    def get_subcontainers(self):
        return []
        
    def read_write_subcontainers(self, rw):
        for i, subcontainer in enumerate(self.get_subcontainers()):
            try:
                rw.rw_obj(subcontainer)
            except Exception as e:
                raise Exception(f"Attempted to read subcontainer {i} on {self.FILETYPE}: {e}") from e
            
    def check_contents_size(self, rw):
        try:
            rw.assert_local_file_pointer_now_at("End of Container Sub-Containers", self.header.contents_length + self.header.header_length)
        except Exception as e:
            print("FUCKED UP ON", self.FILETYPE, ":", e)
            print("Start pos:  ", self.start_pos)
            print("header len: ", self.header.header_length)
            print("body len:   ", self.header.contents_length)
            raise e

    def buildPOF0(self):
        pof0_info = POF0Builder()
        pof0_info.context = copy.deepcopy(self.context)
        pof0_info.anchor_pos = -self.header.header_length
        self.read_write_contents(pof0_info)
        return pof0_info

    def buildENRS(self):
        enrs_info = ENRSBuilder('>')
        enrs_info.context = copy.deepcopy(self.context)
        enrs_info.anchor_pos = -self.header.header_length
        self.read_write_contents(enrs_info)
        return enrs_info


class ValkSerializable16BH(ValkSerializable):
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        self.header = Header16B(self.context, self.FILETYPE)
        self.header.context.endianness = "<"
        
    def check_data_size(self, rw):
        pass


class ValkSerializable32BH(ValkSerializable):
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        self.header = Header32B(self.context, self.FILETYPE)
        self.header.context.endianness = "<"
        
    def check_data_size(self, rw):
        rw.assert_local_file_pointer_now_at(f"End of {self.FILETYPE} Container Data", self.header.header_length + self.header.data_length)


class ValkSerializable48BH(ValkSerializable):
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        self.header = Header48B(self.context, self.FILETYPE)
        self.header.context.endianness = "<"
        
    def check_data_size(self, rw):
        rw.assert_local_file_pointer_now_at(f"End of {self.FILETYPE} Container Data", self.header.header_length + self.header.data_length)
