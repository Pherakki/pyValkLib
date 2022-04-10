from pyValkLib.serialisation.BaseRW import BaseRW
from .AssetEntry import AssetEntry
from pyValkLib.serialisation.ValkyriaBaseRW import PointerIndexableArray


class AssetTable(BaseRW):
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
                
    def rw_header(self):
        self.rw_var("padding_0x00", "I")
        self.rw_var("asset_reference_count", "I")
        self.rw_var("asset_references_offset", "I")
        self.rw_var("asset_use_count", "I")
        self.rw_var("asset_use_offset", "I")
        self.rw_var("padding_0x14", "I")
        self.rw_var("padding_0x18", "I")
        self.rw_var("padding_0x1C", "I")
        
        self.assert_is_zero("padding_0x00")
        self.assert_is_zero("padding_0x14")
        self.assert_is_zero("padding_0x18")
        self.assert_is_zero("padding_0x1C")
        
    def init_structs(self):
        self.entries.data = [AssetEntry(self.endianness) for _ in range(self.asset_reference_count)]
        
    def rw_asset_slot_offsets(self):
        self.rw_varlist("asset_slot_offsets", 'I', self.asset_use_count)

        