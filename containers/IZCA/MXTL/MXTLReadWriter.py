from pyValkLib.serialisation.ValkSerializable import Serializable, ValkSerializable16BH


class MXTLReadWriter(ValkSerializable16BH):
    FILETYPE = "MXTL"
    
    
    def __init__(self, endianness=None):
        super().__init__({}, "<")
        
        self.hmdl_count = None
        self.hmdl_data = []
        self.htsf_names = []
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x00000000, lambda x: hex(x))
        
        self.hmdl_count = rw.rw_uint32(self.hmdl_count)
        self.hmdl_data = rw.rw_obj_array(self.hmdl_data, lambda: HMDLTextureData(self.context), self.hmdl_count)
        
        texture_idxs = set()
        for h in self.hmdl_data:
            for t in h.htsf_data:
                texture_idxs.add(t.htsf_idx)
        self.htsf_names = rw.rw_cstrs(self.htsf_names, len(texture_idxs))
        rw.align(rw.local_tell(), 0x4)

        
class HMDLTextureData(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.flags = None
        self.htsf_count = None
        self.htsf_data = []
    
    def __repr__(self):
        return f"[MXTL::HMDLTextureData] {self.flags} {self.htsf_count} {self.htsf_data}"
    
    def read_write(self, rw):
        self.flags = rw.rw_uint32(self.flags)
        self.htsf_count = rw.rw_uint32(self.htsf_count)
        rw.assert_equal(self.flags, 8)
        
        self.htsf_data = rw.rw_obj_array(self.htsf_data, lambda: HTSFData(self.context), self.htsf_count)
        
class HTSFData(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.htsf_idx = None
        
    def __repr__(self):
        return f"[MXTL::HMDLTextureData::HTSFData] {self.unknown_0x00} {self.unknown_0x04} {self.htsf_idx}"
        
    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.htsf_idx = rw.rw_uint32(self.htsf_idx)
        rw.assert_equal(self.unknown_0x04, 0)
        