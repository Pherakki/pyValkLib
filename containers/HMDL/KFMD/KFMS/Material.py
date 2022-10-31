from pyValkLib.serialisation.Serializable import Context, Serializable

class MaterialBinary(Serializable):
    def __init__(self, context=None):
        if context is None:
            self.context = Context()
        super().__init__(context)
        
        self.unknown_0x00     = None
        self.shader_ID        = None
        self.padding_0x08     = 0
        self.num_textures     = None
        self.src_blend        = None
        self.dst_blend        = None
        self.backface_culling = None
        
        self.texture_1_offset = None
        self.texture_2_offset = None
        self.texture_3_offset = None
        self.padding_0x1C     = 0
        
        self.padding_0x20     = 0
        self.padding_0x24     = 0
        self.padding_0x28     = 0
        self.padding_0x2C     = 0
        
        self.color_1          = None
        self.color_2          = None
        self.color_3          = None
        self.color_4          = None
        
        self.padding_0x70     = 0
        self.padding_0x74     = 0
        self.padding_0x78     = 0
        self.padding_0x7C     = 0
        
        self.padding_0x80     = 0
        self.unknown_0x88     = None
        self.padding_0x8C     = 0
        
        self.unknown_0x90     = 0x20
        self.unknown_0x91     = 0x20
        self.unknown_0x92     = 0x20
        self.unknown_0x93     = 0x20
        self.unknown_0x94     = None
        self.padding_0x98     = 0
        self.unknown_0x9C     = None
        
    def __repr__(self):
        return f"[Material] {self.unknown_0x00} {hex(self.shader_ID)} {self.padding_0x08}\n" \
               f"{self.num_textures} {self.src_blend} {self.dst_blend} {self.backface_culling}\n" \
               f"{self.texture_1_offset} {self.texture_2_offset} {self.texture_3_offset} {self.padding_0x1C}\n" \
               f"{self.padding_0x20} {self.padding_0x24} {self.padding_0x28} {self.padding_0x2C}\n" \
               f"{self.color_1}\n" \
               f"{self.color_2}\n" \
               f"{self.color_3}\n" \
               f"{self.color_4}\n" \
               f"{self.padding_0x70} {self.padding_0x74} {self.padding_0x78} {self.padding_0x7C}\n" \
               f"{self.padding_0x80} {self.unknown_0x88} {self.padding_0x8C}\n" \
               f"{self.unknown_0x90} {self.unknown_0x91} {self.unknown_0x92} {self.unknown_0x93}\n" \
               f"{self.unknown_0x94} {self.padding_0x98} {self.unknown_0x9C}"
        
    def read_write(self, rw):
        self.unknown_0x00     = rw.rw_uint32(self.unknown_0x00)
        self.shader_ID        = rw.rw_uint32(self.shader_ID)
        self.padding_0x08     = rw.rw_pointer(self.padding_0x08)
        self.num_textures     = rw.rw_uint8(self.num_textures)
        self.src_blend        = rw.rw_uint8(self.src_blend)
        self.dst_blend        = rw.rw_uint8(self.dst_blend)
        self.backface_culling = rw.rw_uint8(self.backface_culling)
        
        self.texture_1_offset = rw.rw_pointer(self.texture_1_offset)
        self.texture_2_offset = rw.rw_pointer(self.texture_2_offset)
        self.texture_3_offset = rw.rw_pointer(self.texture_3_offset)
        self.padding_0x1C     = rw.rw_uint32(self.padding_0x1C)

        self.padding_0x20     = rw.rw_uint32(self.padding_0x20)
        self.padding_0x24     = rw.rw_uint32(self.padding_0x24)
        self.padding_0x28     = rw.rw_uint32(self.padding_0x28)
        self.padding_0x2C     = rw.rw_uint32(self.padding_0x2C)
        
        self.color_1          = rw.rw_color128(self.color_1)
        self.color_2          = rw.rw_color128(self.color_2)
        self.color_3          = rw.rw_color128(self.color_3)
        self.color_4          = rw.rw_color128(self.color_4)
        
        self.padding_0x70     = rw.rw_uint32(self.padding_0x70)
        self.padding_0x74     = rw.rw_uint32(self.padding_0x74)
        self.padding_0x78     = rw.rw_uint32(self.padding_0x78)
        self.padding_0x7C     = rw.rw_uint32(self.padding_0x7C)
        
        self.padding_0x80     = rw.rw_uint64(self.padding_0x80)
        self.unknown_0x88     = rw.rw_uint32(self.unknown_0x88)
        self.padding_0x8C     = rw.rw_uint32(self.padding_0x8C)
        
        self.unknown_0x90     = rw.rw_uint8(self.unknown_0x90)
        self.unknown_0x91     = rw.rw_uint8(self.unknown_0x91)
        self.unknown_0x92     = rw.rw_uint8(self.unknown_0x92)
        self.unknown_0x93     = rw.rw_uint8(self.unknown_0x93)
        self.unknown_0x94     = rw.rw_float32(self.unknown_0x94)
        self.padding_0x98     = rw.rw_pad32(self.padding_0x98)
        self.unknown_0x9C     = rw.rw_uint32(self.unknown_0x9C) # This one sometimes has no ENRS
        
        rw.assert_equal(0 <= self.num_textures <= 3, True)
        rw.assert_is_zero(self.padding_0x08)
        rw.assert_is_zero(self.padding_0x1C)
        rw.assert_is_zero(self.padding_0x20)
        rw.assert_is_zero(self.padding_0x24)
        rw.assert_is_zero(self.padding_0x28)
        rw.assert_is_zero(self.padding_0x2C)
        rw.assert_is_zero(self.padding_0x70)
        rw.assert_is_zero(self.padding_0x74)
        rw.assert_is_zero(self.padding_0x78)
        rw.assert_is_zero(self.padding_0x7C)
        rw.assert_is_zero(self.padding_0x80)
        rw.assert_is_zero(self.padding_0x8C)
        rw.assert_is_zero(self.padding_0x98)
        
        rw.assert_equal(self.unknown_0x90, 0x20)
        rw.assert_equal(self.unknown_0x91, 0x20)
        rw.assert_equal(self.unknown_0x92, 0x20)
        rw.assert_equal(self.unknown_0x93, 0x20)
