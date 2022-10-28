from pyValkLib.serialisation.ValkSerializable import ValkSerializable16BH


class MLX0ReadWriter(ValkSerializable16BH):
    FILETYPE = "MLX0"
    
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        
        self.unknown_0x10  = None
        self.unknown_0x14  = None
        self.unknown_0x18  = None
        self.unknown_0x1C  = None
        self.unknown_0x20  = None
        self.unknown_0x24  = None
        self.unknown_0x28  = None
        self.section_count = None
        
        self.sections = None
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x00000000, lambda x: hex(x))
        
        # Data
        self.rw_section_data(rw)
        self.rw_sections(rw)
        
    def rw_section_data(self, rw):
        self.unknown_0x10  = rw.rw_int32(self.unknown_0x10) # Only non-zero when HSPR exists
        self.unknown_0x14  = rw.rw_int32(self.unknown_0x14) # Solo HTSF?
        self.unknown_0x18  = rw.rw_int32(self.unknown_0x18) # Solo HMDL
        self.unknown_0x1C  = rw.rw_int32(self.unknown_0x1C) # HMOT
        self.unknown_0x20  = rw.rw_int32(self.unknown_0x20) # MXTF?
        self.unknown_0x24  = rw.rw_int32(self.unknown_0x24) # MXTL?
        self.unknown_0x28  = rw.rw_int32(self.unknown_0x28) # CLDC / Unified HDML/HTEX
        self.section_count = rw.rw_uint32(self.section_count)
        
    def rw_sections(self, rw):
        # Section count???
        # Try rebuilding with extra sections, see if it matters?
        # Check section count correlation w/ flags...
        
        # Confirmed orders:
            
        # ---
        # MXTL
        # HMDL
        # HMOT
        # MXTF
        # HTSF
        
        # MXTL
        # HSPR
        # MXTF
        
        # ---
        # HMOT
        # HMRP
        # HMMT
        # HCMT
        # HSCM
        # CLDC
        
        # -1 or 0
        # [HSHP ] [HMRP ] [HMMT ] [-----]
        # [HCMT?] [-----] [HSCM?] [-----]
        # [-----] [-----] [HSPR ] [-----]
        self.sections = rw.rw_int32s(self.sections, (self.section_count, 4))
