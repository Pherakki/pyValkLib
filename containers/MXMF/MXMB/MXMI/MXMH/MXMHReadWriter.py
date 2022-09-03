from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH

from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter


class MXMHReadWriter(ValkSerializable32BH):
    FILETYPE = "MXMH"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.flags = 0x18004000
        self.ENRS = ENRSReadWriter("<")
        
        self.asset_folder_name_offset = None
        self.asset_file_name_offset   = None
        self.unknown                  = None # Pointer or data size relating to next entry?
        self.file_type                = None
        self.asset_folder_name        = None
        self.asset_file_name          = None
        

    def get_subcontainers(self):
        return [self.ENRS]
    
    def read_write_contents(self, rw):
        rw.mark_new_contents_array()
        rw.assert_equal(self.header.flags, 0x18004000, lambda x: hex(x))
        
        self.asset_folder_name_offset = rw.rw_uint32(self.asset_folder_name_offset)
        self.asset_file_name_offset   = rw.rw_uint32(self.asset_file_name_offset)
        self.unknown                  = rw.rw_uint32(self.unknown)
        self.file_type                = rw.rw_uint32(self.file_type)
        rw.align(rw.local_tell(), 0x20)
        
        rw.assert_local_file_pointer_now_at("Asset Folder Name", self.asset_folder_name_offset + self.header.header_length)
        self.asset_folder_name = rw.rw_cstr(self.asset_folder_name)
        rw.assert_local_file_pointer_now_at("Asset File Name", self.asset_file_name_offset + self.header.header_length)
        self.asset_file_name = rw.rw_cstr(self.asset_file_name)
        rw.align(rw.local_tell(), 0x10)
        rw.mark_new_contents_array()

    def __repr__(self):
        return f"MXMH Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains ENRS."
