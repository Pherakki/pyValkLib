from pyValkLib.serialisation.Serializable import Context, Serializable

class Texture(Serializable):
    def __init__(self, context=None):
        if context is None:
            self.context = Context()
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.texture_ID   = None
        self.unknown_0x06 = None
        self.blend_factor = None
        self.padding_0x0C = 0
        
        self.padding_0x10 = 0
        self.padding_0x14 = 0
        self.unknown_0x18 = None
        self.unknown_0x1C = None
        
        self.padding_0x20 = 0
        self.padding_0x24 = 0 # Flags?
        self.padding_0x28 = 0
        self.padding_0x2C = 0
        
        self.unknown_0x30 = 0x20
        self.unknown_0x31 = 0x20
        self.unknown_0x32 = 0x20
        self.unknown_0x33 = 0x20
        self.padding_0x34 = 0
        self.padding_0x38 = 0
        self.padding_0x3C = 0
        
    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.texture_ID   = rw.rw_uint16(self.texture_ID)
        self.unknown_0x06 = rw.rw_uint16(self.unknown_0x06)
        self.blend_factor = rw.rw_float32(self.blend_factor)
        self.padding_0x0C = rw.rw_pad32(self.padding_0x0C)

        self.padding_0x10 = rw.rw_uint32(self.padding_0x10)
        self.padding_0x14 = rw.rw_uint32(self.padding_0x14)
        self.unknown_0x18 = rw.rw_float32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_float32(self.unknown_0x1C)

        self.padding_0x20 = rw.rw_pad32(self.padding_0x20)
        self.padding_0x24 = rw.rw_uint32(self.padding_0x24)
        self.padding_0x28 = rw.rw_uint32(self.padding_0x28)
        self.padding_0x2C = rw.rw_uint32(self.padding_0x2C)

        self.unknown_0x30 = rw.rw_uint8(self.unknown_0x30)
        self.unknown_0x31 = rw.rw_uint8(self.unknown_0x31)
        self.unknown_0x32 = rw.rw_uint8(self.unknown_0x32)
        self.unknown_0x33 = rw.rw_uint8(self.unknown_0x33)
        self.padding_0x34 = rw.rw_pad32(self.padding_0x34)
        self.padding_0x38 = rw.rw_pad32(self.padding_0x38)
        self.padding_0x3C = rw.rw_pad32(self.padding_0x3C)
        
        rw.assert_is_zero(self.padding_0x20)
        rw.assert_is_zero(self.padding_0x28)
        rw.assert_is_zero(self.padding_0x2C)
        
        rw.assert_equal(self.unknown_0x30, 0x20)
        rw.assert_equal(self.unknown_0x31, 0x20)
        rw.assert_equal(self.unknown_0x32, 0x20)
        rw.assert_equal(self.unknown_0x33, 0x20)
        
        rw.assert_is_zero(self.padding_0x34)
        rw.assert_is_zero(self.padding_0x38)
        rw.assert_is_zero(self.padding_0x3C)
        
        