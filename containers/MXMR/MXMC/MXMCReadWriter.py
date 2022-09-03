from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray

from .AssetReference import AssetReference
from pyValkLib.containers.Metadata.POF0.POF0ReadWriter import POF0ReadWriter
from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter


class MXMCReadWriter(ValkSerializable32BH):
    FILETYPE = "MXMC"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.header.flags = 0x18000000
        self.POF0 = POF0ReadWriter("<")
        self.ENRS = ENRSReadWriter("<")
        self.EOFC = EOFCReadWriter("<")
        
        self.unknown_0x00           = 0
        self.mmf_folder_name_offset = None
        self.mmf_folder_name        = None
        self.mmf_file_name_offset   = None
        self.mmf_file_name          = None
        self.asset_ref_count        = None
        self.asset_refs_offset      = None
        
        self.asset_refs = PointerIndexableArray(self.context)

    def get_subcontainers(self):
        return [self.POF0, self.ENRS, self.EOFC]
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))
        self.rw_fileinfo(rw)
        self.rw_asset_references(rw)
        self.rw_strings(rw)
        rw.mark_new_contents_array()
        
    def rw_fileinfo(self, rw):
        rw.mark_new_contents_array()
        self.unknown_0x00           = rw.rw_uint32(self.unknown_0x00)
        self.mmf_folder_name_offset = rw.rw_pointer(self.mmf_folder_name_offset)
        self.mmf_file_name_offset   = rw.rw_pointer(self.mmf_file_name_offset)
        self.asset_ref_count        = rw.rw_uint32(self.asset_ref_count)
        self.asset_refs_offset      = rw.rw_pointer(self.asset_refs_offset)
        rw.align(rw.local_tell(), 0x60)
        
    def rw_asset_references(self, rw):
        if self.asset_refs_offset:
            rw.assert_local_file_pointer_now_at("Asset References", self.asset_refs_offset)
            if rw.mode() == "read":
                self.asset_refs.data = [AssetReference(self.context) for _ in range(self.asset_ref_count)]
            rw.rw_obj(self.asset_refs)
            
    def rw_strings(self, rw):
        rw.assert_local_file_pointer_now_at("Folder Name", self.mmf_folder_name_offset)
        self.mmf_folder_name = rw.rw_cstr(self.mmf_folder_name)
        rw.assert_local_file_pointer_now_at("File Name", self.mmf_file_name_offset)
        self.mmf_file_name = rw.rw_cstr(self.mmf_file_name)
        rw.align(rw.local_tell(), 0x10)

    def __repr__(self):
        return f"MXMC Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains MXMC, EOFC."
