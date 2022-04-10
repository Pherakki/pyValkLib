from pyValkLib.serialisation.BaseRW import BaseRW


class AssetEntry(BaseRW):
    
    def __init__(self, endianness):
        super().__init__(endianness)
        
        self.flags = None
        self.ID = None
        self.folder_name_ptr = None
        self.file_name_ptr = None
        
        self.filetype = None
        self.unknown_0x14 = None
        self.padding_0x18 = None
        self.padding_0x1C = None
        
        self.unknown_0x20 = None
        self.unknown_0x24 = None
        self.padding_0x28 = None
        self.padding_0x2C = None
        
        self.padding_0x30 = None
        self.padding_0x34 = None
        self.padding_0x38 = None
        self.padding_0x3C = None   
        
    def read_write(self): 
        # Contents_flags? 
        # 0x000 = all -1
        # 0x100 = something in unknown_0x14, unknown_0x20
        # 0x200 = something in unknown_0x24
        # Unknown0x14 appears to be another ID
        # Unknown_0x20 is always 0
        # Unknown_0x24 also appears to be another ID
        
        # Filetypes?
        # - HMD: 1
        # - HTX: 2, 21
        # - HMT: 3
        # - MCL: 6
        # - MLX: 8
        # - ABR: 9
        # - ABD: 10
        # - CVD: 12
        # - HST: 12
        # - BHV: 12
        # - PVS: 20
        # - HTR: 22
        # - MMF: 24
        # - MMR: 25
        self.rw_var("flags", "I") 
        self.rw_var("ID", "I")
        self.rw_var("folder_name_ptr", "I")
        self.rw_var("file_name_ptr", "I")
        self.rw_var("filetype", "I")
        self.rw_var("unknown_0x14", "i")
        self.rw_var("padding_0x18", "I")
        self.rw_var("padding_0x1C", "I")
        
        self.rw_var("unknown_0x20", "i")
        self.rw_var("unknown_0x24", "i")
        self.rw_var("padding_0x28", "I")
        self.rw_var("padding_0x2C", "I")
        
        self.rw_var("padding_0x30", "I")
        self.rw_var("padding_0x34", "I")
        self.rw_var("padding_0x38", "I")
        self.rw_var("padding_0x3C", "I")
        
        # if not (self.padding_0x00 == 0 or self.padding_0x00 == 512): # can be 512 if flags...
        #     assert 0, "Padding in Table is fucked"
        # self.assert_equal("unknown_0x14", -1)  # Can be 24
        self.assert_is_zero("padding_0x18")
        self.assert_is_zero("padding_0x1C")
        
        # self.assert_equal("unknown_0x20", -1) # Can be 0
        # self.assert_equal("unknown_0x24", -1) # Can be 12 if flags...
        # if not (self.unknown_0x24 == -1 or self.unknown_0x24 == 12):
        #     assert 0, "Eggh"
        self.assert_is_zero("padding_0x28")
        self.assert_is_zero("padding_0x2C")
        
        self.assert_is_zero("padding_0x30")
        self.assert_is_zero("padding_0x34")
        self.assert_is_zero("padding_0x38")
        self.assert_is_zero("padding_0x3C")
        
        
        