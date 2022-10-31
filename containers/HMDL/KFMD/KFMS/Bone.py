from pyValkLib.serialisation.Serializable import Context, Serializable

class BoneBinary(Serializable):
    __slots__ = ("ibpm_offset", "unknown_0x04", "ID")
    
    def __init__(self, context=None):
        if context is None:
            self.context = Context()
        super().__init__(context)
        
        self.ibpm_offset = None
        self.ID = None
        self.unknown_0x04 = None # Can be 0, 1...
    
    def __repr__(self):
        return f"[BoneBinary] {self.ID} {self.unknown_0x04} {self.ibpm_offset}"
    
    def read_write(self, rw):
        self.ibpm_offset  = rw.rw_pointer(self.ibpm_offset)
        self.unknown_0x04 = rw.rw_uint16(self.unknown_0x04)
        self.ID           = rw.rw_uint16(self.ID)

        try:
            rw.assert_equal(self.unknown_0x04 in [0, 1], True)
        except Exception as e:
            print(self.unknown_0x04)
            raise e
