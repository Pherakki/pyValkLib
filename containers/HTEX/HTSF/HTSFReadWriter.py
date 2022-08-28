from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH


class HTSFReadWriter(ValkSerializable32BH):
    FILETYPE = "HTSF"
    
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.flags = 0x10000000
        self.lead_padding = b'\x00'*0x20
        self.dds_data = None

    def read_write_contents(self, rw):
        # 0x10000000, 0x10000004
        # Maybe the 0x04 flag indicates that the file is mergeable?
        #rw.assert_equal(self.header.flags, 0x10000004, lambda x: hex(x))
        
        self.lead_padding = rw.rw_bytestring(self.lead_padding, 0x20)
        rw.assert_equal(self.lead_padding, b'\x00'*0x20)
        self.dds_data = rw.rw_bytestring(self.dds_data, self.header.data_length - 0x20)

    def __repr__(self):
        return f"HTSF Object [{self.header.depth}] [0x{self.header.flags:0>8x}]."
