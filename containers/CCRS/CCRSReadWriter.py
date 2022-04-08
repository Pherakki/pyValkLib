from pyValkLib.serialisation.ValkyriaBaseRW import ValkyriaBaseRW32BH


class CCRSReadWriter(ValkyriaBaseRW32BH):
    FILETYPE = "CCRS"
    
    __slots__ = ("padding_0x20", "num_groups", "data")
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        
        # Data holders
        self.ptr_groups = None
        self.data = None
        
    def read_write_contents(self):
        self.assert_equal("flags", 0x10000000, self.header, lambda x: hex(x))
        self.rw_var("padding_0x20", 'I')
        self.rw_var("num_groups", 'I')
        self.cleanup_ragged_chunk(self.local_tell(), 0x10)
        
        self.assert_is_zero("padding_0x20")
        self.rw_varlist("data", "B", self.header.data_length - 0x10, endianness='<')
