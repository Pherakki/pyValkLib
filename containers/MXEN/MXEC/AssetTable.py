from pyValkLib.serialisation.BaseRW import BaseRW
from .AssetEntry import AssetEntry

class AssetTable(BaseRW):
    def __init__(self, endianness):
        super().__init__(endianness)
        self.pad_0x00 = None
        self.count_1 = None
        self.offset_1 = None
        self.count_2 = None
        self.offset_2 = None
        self.pad_0x14 = None
        self.pad_0x18 = None
        self.pad_0x1C = None
        
        self.elements_1 = None
        self.elements_2 = None
        
        
    def rw_header(self):
        self.rw_var("pad_0x00", "I")
        self.rw_var("count_1", "I")
        self.rw_var("offset_1", "I")
        self.rw_var("count_2", "I")
        self.rw_var("offset_2", "I")
        self.rw_var("pad_0x14", "I")
        self.rw_var("pad_0x18", "I")
        self.rw_var("pad_0x1C", "I")
        
        self.assert_is_zero("pad_0x00")
        self.assert_is_zero("pad_0x14")
        self.assert_is_zero("pad_0x18")
        self.assert_is_zero("pad_0x1C")
        
    def init_structs(self):
        self.elements_1 = [AssetEntry() for _ in range(self.count_1)]
        
    def rw_unknown_offsets(self):
        self.rw_vararray("elements_2", 'I', self.count_2)

        