from pyValkLib.serialisation.Serializable import Serializable
from .AssetEntry import AssetEntry
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray


class AssetTable(Serializable):
    def __init__(self, endianness):
        super().__init__(endianness)
        self.padding_0x00 = None
        self.asset_reference_count = None
        self.asset_references_offset = None
        self.asset_use_count = None
        self.asset_use_offset = None
        self.padding_0x14 = None
        self.padding_0x18 = None
        self.padding_0x1C = None
        
        self.entries = PointerIndexableArray()
        self.asset_slot_offsets = None
        
    def read_write(self):
        self.rw_header()
        if self.rw_method == 'read':
            self.init_structs()
                
    def rw_header(self, rw):
        self.padding_0x00            = rw.rw_uint32(self.padding_0x00)
        self.asset_reference_count   = rw.rw_uint32(self.asset_reference_count)
        self.asset_references_offset = rw.rw_uint32(self.asset_references_offset)
        self.asset_use_count         = rw.rw_uint32(self.asset_use_count)
        self.asset_use_offset        = rw.rw_uint32(self.asset_use_offset)
        self.padding_0x14            = rw.rw_uint32(self.padding_0x14)
        self.padding_0x18            = rw.rw_uint32(self.padding_0x18)
        self.padding_0x1C            = rw.rw_uint32(self.padding_0x1C)
        
        rw.assert_is_zero(self.padding_0x00)
        rw.assert_is_zero(self.padding_0x14)
        rw.assert_is_zero(self.padding_0x18)
        rw.assert_is_zero(self.padding_0x1C)
        
    def init_structs(self):
        self.entries.data = [AssetEntry(self.endianness) for _ in range(self.asset_reference_count)]
        
    def rw_asset_slot_offsets(self, rw):
        self.asset_slot_offsets = rw.rw_uint32s(self.asset_slot_offsets, self.asset_use_count)
