from pyValkLib.serialisation.Serializable import Serializable

        
##############
# DATA TYPES #
##############
        
class MxParameterFog(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_float32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_float32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_float32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_float32(self.unknown_0x1C)
        
    def get_data(self):
        return (self.unknown_0x00, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C,
                self.unknown_0x10, self.unknown_0x14, self.unknown_0x18, self.unknown_0x1C)
        
    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C ]
    
class HyColor(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_float32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        
    def get_data(self):
        return (self.unknown_0x00, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C)
        
    def asset_table_offsets(self):
        return []
    
        
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C ]
    
class MxParameterLight(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_ptr_1 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_float32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_float32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_float32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_float32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_float32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_float32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_float32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_float32(self.unknown_0x4C)
        
        self.unknown_ptr_1 = rw.rw_pointer(self.unknown_ptr_1)
        self.unknown_0x54 = rw.rw_pad32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_pad32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_pad32(self.unknown_0x5C)
        
        rw.assert_is_zero(self.unknown_0x54)
        rw.assert_is_zero(self.unknown_0x58)
        rw.assert_is_zero(self.unknown_0x5C)
        
    def get_data(self):
        return (self.unknown_0x00, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C,
                self.unknown_0x10, self.unknown_0x14, self.unknown_0x18, self.unknown_0x1C,
                self.unknown_0x20, self.unknown_0x24, self.unknown_0x28, self.unknown_0x2C,
                self.unknown_0x30, self.unknown_0x34, self.unknown_0x38, self.unknown_0x3C,
                self.unknown_0x40, self.unknown_0x44, self.unknown_0x48, self.unknown_0x4C,
                self.unknown_ptr_1, self.unknown_0x54, self.unknown_0x58, self.unknown_0x5C)
    
    def asset_table_offsets(self):
        return []
            
    def pof0_offsets(self):
        return [0x50]
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C , 0x30,  0x34,  0x38,  0x3C,
                 0x40,  0x44,  0x48,  0x4C,  0x50 ]
        
class MxParameterStaticLight(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.light_count = 0
        self.unknown_ptr = 0
        self.padding_0x08 = 0
        self.padding_0x0C = 0
        
        self.lights = []

    def read_write(self, rw):
        self.light_count = rw.rw_uint32(self.light_count)
        self.unknown_ptr = rw.rw_pointer(self.unknown_ptr)
        self.padding_0x08 = rw.rw_pad32(self.padding_0x08)
        self.padding_0x0C = rw.rw_pad32(self.padding_0x0C)
        
        rw.assert_is_zero(self.padding_0x08)
        rw.assert_is_zero(self.padding_0x0C)
        
        if rw.mode() == "read":
            self.lights = [MxParameterLight(self.context) for _ in range(self.light_count)]
            
        for light in self.lights:
            rw.rw_obj(light)
        
    def get_data(self):
        return (self.light_count, self.unknown_ptr, [light.get_data() for light in self.lights])

    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return [0x04]
    
    def enrs_offsets(self):
        return [ 0x00,  0x04 ]
    
class VlMxFogParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_pad32(self.unknown_0x14)
        
        
        
    def get_data(self):
        return (self.unknown_0x00, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C,
                self.unknown_0x10, 
                self.unknown_0x14)
        
    def asset_table_offsets(self):
        return []
        
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10 ]
    
class VlMxShaderParamSetId(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        
    def get_data(self):
        return (self.unknown_0x00, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C)
         
    def asset_table_offsets(self):
        return []  
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C ]
    
class VlMxStandardLightParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x74 = 0
        self.unknown_0x78 = 0
        self.unknown_0x7C = 0
        self.unknown_0x80 = 0
        self.unknown_0x84 = 0
        self.unknown_0x88 = 0
        self.unknown_0x8C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_float32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_float32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_float32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_float32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_float32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_float32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_float32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_float32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_float32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_float32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_float32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_float32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_float32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_float32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_float32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_uint32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_uint32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_uint32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_uint32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_float32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_float32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_float32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_float32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_float32(self.unknown_0x70)
        self.unknown_0x74 = rw.rw_float32(self.unknown_0x74)
        self.unknown_0x78 = rw.rw_float32(self.unknown_0x78)
        self.unknown_0x7C = rw.rw_float32(self.unknown_0x7C)
        
        self.unknown_0x80 = rw.rw_uint32(self.unknown_0x80)
        self.unknown_0x84 = rw.rw_uint32(self.unknown_0x84)
        self.unknown_0x88 = rw.rw_uint32(self.unknown_0x88)
        self.unknown_0x8C = rw.rw_uint32(self.unknown_0x8C)
        
    def get_data(self):
        return (self.unknown_0x00, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C,
                self.unknown_0x10, self.unknown_0x14, self.unknown_0x18, self.unknown_0x1C,
                self.unknown_0x20, self.unknown_0x24, self.unknown_0x28, self.unknown_0x2C,
                self.unknown_0x30, self.unknown_0x34, self.unknown_0x38, self.unknown_0x3C,
                self.unknown_0x40, self.unknown_0x44, self.unknown_0x48, self.unknown_0x4C,
                self.unknown_0x50, self.unknown_0x54, self.unknown_0x58, self.unknown_0x5C,
                self.unknown_0x60, self.unknown_0x64, self.unknown_0x68, self.unknown_0x6C,
                self.unknown_0x70, self.unknown_0x74, self.unknown_0x78, self.unknown_0x7C,
                self.unknown_0x80, self.unknown_0x84, self.unknown_0x88, self.unknown_0x8C)

    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,         0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                  0x80,  0x84,  0x88,  0x8C
               ]

class EnTalkEventMapParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        # THESE ALL SEEM TO BE FLAGS
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)  # Padding
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)  # Padding
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)  # Padding
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)  # Padding
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)  # Padding
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)  # Padding
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)  # Padding
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)  # Padding
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)  # Padding
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,
                 0x110, 0x118
               ]

class VlMxAddEsdInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04 ]
    
class VlMxCharacterAffinityInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08)
    
    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08 ]

class VlMxCharacterCommonInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_float32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_float32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_float32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_float32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_float32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_float32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_float32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_uint32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_float32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_float32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_float32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_float32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_float32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_float32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_float32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_float32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_float32(self.unknown_0x54)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54 )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54
               ]

class VlMxCharacterEachInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x74 = 0
        self.unknown_0x78 = 0
        self.unknown_0x7C = 0
        self.unknown_0x80 = 0
        self.unknown_0x84 = 0
        self.unknown_0x88 = 0
        self.unknown_0x8C = 0
        self.unknown_0x90 = 0
        self.unknown_0x94 = 0
        self.unknown_0x98 = 0
        self.unknown_0x9C = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA4 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xAC = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB4 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xBC = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC4 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xCC = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD4 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xDC = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE4 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xEC = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF4 = 0
        self.unknown_0xF8 = 0
        self.unknown_0xFC = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0104 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x010C = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x011C = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0124 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x012C = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x013C = 0
        self.unknown_0x0140 = 0
        self.unknown_0x0144 = 0
        self.unknown_0x0148 = 0
        self.unknown_0x014C = 0
        self.unknown_0x0150 = 0
        self.unknown_0x0154 = 0
        self.unknown_0x0158 = 0
        self.unknown_0x015C = 0
        self.unknown_0x0160 = 0
        self.unknown_0x0164 = 0
        self.unknown_0x0168 = 0
        self.unknown_0x016C = 0
        self.unknown_0x0170 = 0
        self.unknown_0x0174 = 0
        self.unknown_0x0178 = 0
        self.unknown_0x017C = 0
        self.unknown_0x0180 = 0
        self.unknown_0x0184 = 0
        self.unknown_0x0188 = 0
        self.unknown_0x018C = 0
        self.unknown_0x0190 = 0
        self.unknown_0x0194 = 0
        self.unknown_0x0198 = 0
        self.unknown_0x019C = 0
        self.unknown_0x01A0 = 0
        self.unknown_0x01A4 = 0
        self.unknown_0x01A8 = 0
        self.unknown_0x01AC = 0
        self.unknown_0x01A0 = 0
        self.unknown_0x01A4 = 0
        self.unknown_0x01A8 = 0
        self.unknown_0x01AC = 0
        self.unknown_0x01B0 = 0
        self.unknown_0x01B4 = 0
        self.unknown_0x01B8 = 0
        self.unknown_0x01BC = 0
        self.unknown_0x01C0 = 0
        self.unknown_0x01C4 = 0
        self.unknown_0x01C8 = 0
        self.unknown_0x01CC = 0
        self.unknown_0x01D0 = 0
        self.unknown_0x01D4 = 0
        self.unknown_0x01D8 = 0
        self.unknown_0x01DC = 0
        self.unknown_0x01E0 = 0
        self.unknown_0x01E4 = 0
        self.unknown_0x01E8 = 0
        self.unknown_0x01EC = 0
        self.unknown_0x01F0 = 0
        self.unknown_0x01F4 = 0
        self.unknown_0x01F8 = 0
        self.unknown_0x01FC = 0
        self.unknown_0x0200 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_float32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_float32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_float32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pointer(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pointer(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_pointer(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_pointer(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_pointer(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_float32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_float32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_float32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_float32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_float32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_float32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int32(self.unknown_0x70)
        self.unknown_0x74 = rw.rw_int32(self.unknown_0x74)
        self.unknown_0x78 = rw.rw_int32(self.unknown_0x78)
        self.unknown_0x7C = rw.rw_int32(self.unknown_0x7C)
        
        self.unknown_0x80 = rw.rw_int32(self.unknown_0x80)
        self.unknown_0x84 = rw.rw_int32(self.unknown_0x84)
        self.unknown_0x88 = rw.rw_int32(self.unknown_0x88)
        self.unknown_0x8C = rw.rw_int32(self.unknown_0x8C)
        
        self.unknown_0x90 = rw.rw_int32(self.unknown_0x90)
        self.unknown_0x94 = rw.rw_int32(self.unknown_0x94)
        self.unknown_0x98 = rw.rw_int32(self.unknown_0x98)
        self.unknown_0x9C = rw.rw_int32(self.unknown_0x9C)
        
        self.unknown_0xA0 = rw.rw_int32(self.unknown_0xA0)
        self.unknown_0xA4 = rw.rw_int32(self.unknown_0xA4)
        self.unknown_0xA8 = rw.rw_int32(self.unknown_0xA8)
        self.unknown_0xAC = rw.rw_int32(self.unknown_0xAC)
        
        self.unknown_0xB0 = rw.rw_int32(self.unknown_0xB0)
        self.unknown_0xB4 = rw.rw_int32(self.unknown_0xB4)
        self.unknown_0xB8 = rw.rw_int32(self.unknown_0xB8)
        self.unknown_0xBC = rw.rw_int32(self.unknown_0xBC)
        
        self.unknown_0xC0 = rw.rw_int32(self.unknown_0xC0)
        self.unknown_0xC4 = rw.rw_int32(self.unknown_0xC4)
        self.unknown_0xC8 = rw.rw_int32(self.unknown_0xC8)
        self.unknown_0xCC = rw.rw_int32(self.unknown_0xCC)
        
        self.unknown_0xD0 = rw.rw_int32(self.unknown_0xD0)
        self.unknown_0xD4 = rw.rw_int32(self.unknown_0xD4)
        self.unknown_0xD8 = rw.rw_int32(self.unknown_0xD8)
        self.unknown_0xDC = rw.rw_int32(self.unknown_0xDC)
        
        self.unknown_0xE0 = rw.rw_int32(self.unknown_0xE0)
        self.unknown_0xE4 = rw.rw_int32(self.unknown_0xE4)
        self.unknown_0xE8 = rw.rw_int32(self.unknown_0xE8)
        self.unknown_0xEC = rw.rw_int32(self.unknown_0xEC)
        
        self.unknown_0xF0 = rw.rw_int32(self.unknown_0xF0)
        self.unknown_0xF4 = rw.rw_int32(self.unknown_0xF4)
        self.unknown_0xF8 = rw.rw_int32(self.unknown_0xF8)
        self.unknown_0xFC = rw.rw_int32(self.unknown_0xFC)
        
        self.unknown_0x0100 = rw.rw_int32(self.unknown_0x0100)
        self.unknown_0x0104 = rw.rw_int32(self.unknown_0x0104)
        self.unknown_0x0108 = rw.rw_int32(self.unknown_0x0108)
        self.unknown_0x010C = rw.rw_int32(self.unknown_0x010C)
        
        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_int32(self.unknown_0x0118)
        self.unknown_0x011C = rw.rw_int32(self.unknown_0x011C)
        
        self.unknown_0x0120 = rw.rw_int32(self.unknown_0x0120)
        self.unknown_0x0124 = rw.rw_int32(self.unknown_0x0124)
        self.unknown_0x0128 = rw.rw_int32(self.unknown_0x0128)
        self.unknown_0x012C = rw.rw_int32(self.unknown_0x012C)
        
        self.unknown_0x0130 = rw.rw_int32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_int32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_int32(self.unknown_0x0138)
        self.unknown_0x013C = rw.rw_int32(self.unknown_0x013C)
        
        self.unknown_0x0140 = rw.rw_int32(self.unknown_0x0140)
        self.unknown_0x0144 = rw.rw_int32(self.unknown_0x0144)
        self.unknown_0x0148 = rw.rw_int32(self.unknown_0x0148)
        self.unknown_0x014C = rw.rw_int32(self.unknown_0x014C)
        
        self.unknown_0x0150 = rw.rw_int32(self.unknown_0x0150)
        self.unknown_0x0154 = rw.rw_int32(self.unknown_0x0154)
        self.unknown_0x0158 = rw.rw_int32(self.unknown_0x0158)
        self.unknown_0x015C = rw.rw_int32(self.unknown_0x015C)
        
        self.unknown_0x0160 = rw.rw_int32(self.unknown_0x0160)
        self.unknown_0x0164 = rw.rw_int32(self.unknown_0x0164)
        self.unknown_0x0168 = rw.rw_int32(self.unknown_0x0168)
        self.unknown_0x016C = rw.rw_int32(self.unknown_0x016C)
        
        self.unknown_0x0170 = rw.rw_int32(self.unknown_0x0170)
        self.unknown_0x0174 = rw.rw_int32(self.unknown_0x0174)
        self.unknown_0x0178 = rw.rw_int32(self.unknown_0x0178)
        self.unknown_0x017C = rw.rw_int32(self.unknown_0x017C)
        
        self.unknown_0x0180 = rw.rw_int32(self.unknown_0x0180)
        self.unknown_0x0184 = rw.rw_int32(self.unknown_0x0184)
        self.unknown_0x0188 = rw.rw_int32(self.unknown_0x0188)
        self.unknown_0x018C = rw.rw_int32(self.unknown_0x018C)
        
        self.unknown_0x0190 = rw.rw_int32(self.unknown_0x0190)
        self.unknown_0x0194 = rw.rw_int32(self.unknown_0x0194)
        self.unknown_0x0198 = rw.rw_int32(self.unknown_0x0198)
        self.unknown_0x019C = rw.rw_int32(self.unknown_0x019C)
        
        self.unknown_0x01A0 = rw.rw_int32(self.unknown_0x01A0)
        self.unknown_0x01A4 = rw.rw_int32(self.unknown_0x01A4)
        self.unknown_0x01A8 = rw.rw_int32(self.unknown_0x01A8)
        self.unknown_0x01AC = rw.rw_int32(self.unknown_0x01AC)
        
        self.unknown_0x01A0 = rw.rw_int32(self.unknown_0x01A0)
        self.unknown_0x01A4 = rw.rw_int32(self.unknown_0x01A4)
        self.unknown_0x01A8 = rw.rw_int32(self.unknown_0x01A8)
        self.unknown_0x01AC = rw.rw_int32(self.unknown_0x01AC)
        
        self.unknown_0x01B0 = rw.rw_int32(self.unknown_0x01B0)
        self.unknown_0x01B4 = rw.rw_int32(self.unknown_0x01B4)
        self.unknown_0x01B8 = rw.rw_int32(self.unknown_0x01B8)
        self.unknown_0x01BC = rw.rw_int32(self.unknown_0x01BC)
        
        self.unknown_0x01C0 = rw.rw_int32(self.unknown_0x01C0)
        self.unknown_0x01C4 = rw.rw_int32(self.unknown_0x01C4)
        self.unknown_0x01C8 = rw.rw_int32(self.unknown_0x01C8)
        self.unknown_0x01CC = rw.rw_int32(self.unknown_0x01CC)
        
        self.unknown_0x01D0 = rw.rw_int32(self.unknown_0x01D0)
        self.unknown_0x01D4 = rw.rw_int32(self.unknown_0x01D4)
        self.unknown_0x01D8 = rw.rw_int32(self.unknown_0x01D8)
        self.unknown_0x01DC = rw.rw_int32(self.unknown_0x01DC)
        
        self.unknown_0x01E0 = rw.rw_int32(self.unknown_0x01E0)
        self.unknown_0x01E4 = rw.rw_int32(self.unknown_0x01E4)
        self.unknown_0x01E8 = rw.rw_int32(self.unknown_0x01E8)
        self.unknown_0x01EC = rw.rw_int32(self.unknown_0x01EC)
        
        self.unknown_0x01F0 = rw.rw_int32(self.unknown_0x01F0)
        self.unknown_0x01F4 = rw.rw_int32(self.unknown_0x01F4)
        self.unknown_0x01F8 = rw.rw_int32(self.unknown_0x01F8)
        self.unknown_0x01FC = rw.rw_int32(self.unknown_0x01FC)
        
        self.unknown_0x0200 = rw.rw_int32(self.unknown_0x0200)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC, 
                 
                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128,  self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134,  self.unknown_0x0138,  self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0144,  self.unknown_0x0148,  self.unknown_0x014C,
                 self.unknown_0x0150,  self.unknown_0x0154,  self.unknown_0x0158,  self.unknown_0x015C,
                 self.unknown_0x0160,  self.unknown_0x0164,  self.unknown_0x0168,  self.unknown_0x016C,
                 self.unknown_0x0170,  self.unknown_0x0174,  self.unknown_0x0178,  self.unknown_0x017C,
                
                 self.unknown_0x0180,  self.unknown_0x0184,  self.unknown_0x0188,  self.unknown_0x018C,
                 self.unknown_0x0190,  self.unknown_0x0194,  self.unknown_0x0198,  self.unknown_0x019C,
                 self.unknown_0x01A0,  self.unknown_0x01A4,  self.unknown_0x01A8,  self.unknown_0x01AC,
                 self.unknown_0x01B0,  self.unknown_0x01B4,  self.unknown_0x01B8,  self.unknown_0x01BC,
                 self.unknown_0x01C0,  self.unknown_0x01C4,  self.unknown_0x01C8,  self.unknown_0x01CC,
                 self.unknown_0x01D0,  self.unknown_0x01D4,  self.unknown_0x01D8,  self.unknown_0x01DC,
                 self.unknown_0x01E0,  self.unknown_0x01E4,  self.unknown_0x01E8,  self.unknown_0x01EC,
                 self.unknown_0x01F0,  self.unknown_0x01F4,  self.unknown_0x01F8,  self.unknown_0x01FC,
                 
                 self.unknown_0x0200 )  
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x38, 0x3C, 0x40, 0x44, 0x48 ]
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                 0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                 0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  
                 0xB8,  0xBA,  0xBC,  0xBE,
                 0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                 0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4,  0xF8,  0xFC,
                0x100, 0x104, 0x108, 0x10C, 0x110, 0x114, 0x118, 0x11C,
                0x120, 0x124, 0x128, 0x12C, 0x130, 0x134, 0x138, 0x13C,
                0x140, 0x144, 0x148, 0x14C, 0x150, 0x154, 0x158, 0x15C,
                0x160, 0x164, 0x168, 0x16C, 0x170, 0x174, 0x178, 0x17C,
                0x180, 0x184, 0x188, 0x18C, 0x190, 0x194, 0x198, 0x19C,
                0x1A0, 0x1A4, 0x1A8, 0x1AC, 0x1B0, 0x1B4, 0x1B8, 0x1BC,
                0x1C0, 0x1C4, 0x1C8, 0x1CC, 0x1D0, 0x1D4, 0x1D8, 0x1DC,
                0x1E0, 0x1E4, 0x1E8, 0x1EC, 0x1F0, 0x1F4, 0x1F8, 0x1FC,
                0x200, 0x204, 0x208, 0x20C, 0x210
               ]
    def get_string_ptrs(self):
        return [ self.unknown_0x38, self.unknown_0x3C, self.unknown_0x40, self.unknown_0x44, self.unknown_0x48 ]

class VlMxCharacterInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_pointer(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_pointer(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_pointer(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_pointer(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_pointer(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_int32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_int32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [0x04, 0x08, 0x0C, 0x10, 0x14, 0x18]
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40,  0x44,  0x48,  0x4C
               ]

    def get_string_ptrs(self):
        return [self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C,
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18]
    
class VlMxClothesInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_pointer(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_float32(self.unknown_0x20)
      
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x00, 0x04 ]
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20
               ]

    def get_string_ptrs(self):
        return [self.unknown_0x00, self.unknown_0x04]
    
class VlMxExplosiveInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pad32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)

        #rw.assert_is_zero(self.unknown_0x04)
          
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04, self.unknown_0x08,  
                 self.unknown_0x0C, self.unknown_0x10 )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x08,  0x0C,  0x10 ]
        
class VlMxForceInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
      
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x04 ]
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20
               ]

    def get_string_ptrs(self):
        return [self.unknown_0x04]
    
class VlMxGalliaRareWeaponCandidateInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x16 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1A = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_pad32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int16(self.unknown_0x14)  
        self.unknown_0x16 = rw.rw_int16(self.unknown_0x16) 
        self.unknown_0x18 = rw.rw_int16(self.unknown_0x18) 
        self.unknown_0x1A = rw.rw_int16(self.unknown_0x1A)

        #rw.assert_is_zero(self.unknown_0x00)
          
    def get_data(self):
        return ( self.unknown_0x00, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C, 
                 self.unknown_0x10, self.unknown_0x14, self.unknown_0x16, self.unknown_0x18, 
                 self.unknown_0x1A, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x04,  0x08,  0x0C,  0x10,  0x14,  0x16, 0x18,  0x1A ]
  
class VlMxGeneralCharInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x74 = 0
        self.unknown_0x78 = 0
        self.unknown_0x7C = 0
        self.unknown_0x80 = 0
        self.unknown_0x84 = 0
        self.unknown_0x88 = 0
        self.unknown_0x8C = 0
        self.unknown_0x90 = 0
        self.unknown_0x94 = 0
        self.unknown_0x98 = 0
        self.unknown_0x9C = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA4 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xAC = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB4 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xBC = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC4 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xCC = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD4 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xDC = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE4 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xEC = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF4 = 0
        self.unknown_0xF8 = 0
        self.unknown_0xFC = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0104 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x010C = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x011C = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0124 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x012C = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x013C = 0
        self.unknown_0x0140 = 0
        self.unknown_0x0144 = 0
        self.unknown_0x0148 = 0
        self.unknown_0x014C = 0
        self.unknown_0x0150 = 0
        self.unknown_0x0154 = 0
        self.unknown_0x0158 = 0
        self.unknown_0x015C = 0
        self.unknown_0x0160 = 0
        self.unknown_0x0164 = 0
        self.unknown_0x0168 = 0
        self.unknown_0x016C = 0
        self.unknown_0x0170 = 0
        self.unknown_0x0174 = 0
        self.unknown_0x0178 = 0
        self.unknown_0x017C = 0
        self.unknown_0x0180 = 0
        self.unknown_0x0184 = 0
        self.unknown_0x0188 = 0
        self.unknown_0x018C = 0
        self.unknown_0x0190 = 0
        self.unknown_0x0194 = 0
        self.unknown_0x0198 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_pointer(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_pointer(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_pointer(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_pointer(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_pointer(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_pointer(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_pointer(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_pointer(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pointer(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pointer(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pointer(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pointer(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pointer(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pointer(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_pointer(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_pointer(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_pointer(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_pointer(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_pointer(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_pointer(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_pointer(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_pointer(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_pointer(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_pointer(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_pointer(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_pointer(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_pointer(self.unknown_0x70)
        self.unknown_0x74 = rw.rw_pointer(self.unknown_0x74)
        self.unknown_0x78 = rw.rw_pointer(self.unknown_0x78)
        self.unknown_0x7C = rw.rw_pointer(self.unknown_0x7C)
        
        self.unknown_0x80 = rw.rw_pointer(self.unknown_0x80)
        self.unknown_0x84 = rw.rw_pointer(self.unknown_0x84)
        self.unknown_0x88 = rw.rw_pointer(self.unknown_0x88)
        self.unknown_0x8C = rw.rw_pointer(self.unknown_0x8C)
        
        self.unknown_0x90 = rw.rw_pointer(self.unknown_0x90)
        self.unknown_0x94 = rw.rw_pointer(self.unknown_0x94)
        self.unknown_0x98 = rw.rw_pointer(self.unknown_0x98)
        self.unknown_0x9C = rw.rw_pointer(self.unknown_0x9C)
        
        self.unknown_0xA0 = rw.rw_pointer(self.unknown_0xA0)
        self.unknown_0xA4 = rw.rw_pointer(self.unknown_0xA4)
        self.unknown_0xA8 = rw.rw_pointer(self.unknown_0xA8)
        self.unknown_0xAC = rw.rw_pointer(self.unknown_0xAC)
        
        self.unknown_0xB0 = rw.rw_pointer(self.unknown_0xB0)
        self.unknown_0xB4 = rw.rw_pointer(self.unknown_0xB4)
        self.unknown_0xB8 = rw.rw_pointer(self.unknown_0xB8)
        self.unknown_0xBC = rw.rw_pointer(self.unknown_0xBC)
        
        self.unknown_0xC0 = rw.rw_pointer(self.unknown_0xC0)
        self.unknown_0xC4 = rw.rw_pointer(self.unknown_0xC4)
        self.unknown_0xC8 = rw.rw_pointer(self.unknown_0xC8)
        self.unknown_0xCC = rw.rw_pointer(self.unknown_0xCC)
        
        self.unknown_0xD0 = rw.rw_pointer(self.unknown_0xD0)
        self.unknown_0xD4 = rw.rw_pointer(self.unknown_0xD4)
        self.unknown_0xD8 = rw.rw_pointer(self.unknown_0xD8)
        self.unknown_0xDC = rw.rw_pointer(self.unknown_0xDC)
        
        self.unknown_0xE0 = rw.rw_pointer(self.unknown_0xE0)
        self.unknown_0xE4 = rw.rw_pointer(self.unknown_0xE4)
        self.unknown_0xE8 = rw.rw_pointer(self.unknown_0xE8)
        self.unknown_0xEC = rw.rw_pointer(self.unknown_0xEC)
        
        self.unknown_0xF0 = rw.rw_pointer(self.unknown_0xF0)
        self.unknown_0xF4 = rw.rw_pointer(self.unknown_0xF4)
        self.unknown_0xF8 = rw.rw_pointer(self.unknown_0xF8)
        self.unknown_0xFC = rw.rw_pointer(self.unknown_0xFC)
        
        self.unknown_0x0100 = rw.rw_pointer(self.unknown_0x0100)
        self.unknown_0x0104 = rw.rw_pointer(self.unknown_0x0104)
        self.unknown_0x0108 = rw.rw_pointer(self.unknown_0x0108)
        self.unknown_0x010C = rw.rw_pointer(self.unknown_0x010C)
        
        self.unknown_0x0110 = rw.rw_pointer(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_pointer(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_pointer(self.unknown_0x0118)
        self.unknown_0x011C = rw.rw_pointer(self.unknown_0x011C)
        
        self.unknown_0x0120 = rw.rw_pointer(self.unknown_0x0120)
        self.unknown_0x0124 = rw.rw_pointer(self.unknown_0x0124)
        self.unknown_0x0128 = rw.rw_pointer(self.unknown_0x0128)
        self.unknown_0x012C = rw.rw_pointer(self.unknown_0x012C)
        
        self.unknown_0x0130 = rw.rw_pointer(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_pointer(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_pointer(self.unknown_0x0138)
        self.unknown_0x013C = rw.rw_pointer(self.unknown_0x013C)
        
        self.unknown_0x0140 = rw.rw_pointer(self.unknown_0x0140)
        self.unknown_0x0144 = rw.rw_pointer(self.unknown_0x0144)
        self.unknown_0x0148 = rw.rw_pointer(self.unknown_0x0148)
        self.unknown_0x014C = rw.rw_pointer(self.unknown_0x014C)
        
        self.unknown_0x0150 = rw.rw_pointer(self.unknown_0x0150)
        self.unknown_0x0154 = rw.rw_pointer(self.unknown_0x0154)
        self.unknown_0x0158 = rw.rw_pointer(self.unknown_0x0158)
        self.unknown_0x015C = rw.rw_pointer(self.unknown_0x015C)
        
        self.unknown_0x0160 = rw.rw_pointer(self.unknown_0x0160)
        self.unknown_0x0164 = rw.rw_pointer(self.unknown_0x0164)
        self.unknown_0x0168 = rw.rw_pointer(self.unknown_0x0168)
        self.unknown_0x016C = rw.rw_pointer(self.unknown_0x016C)
        
        self.unknown_0x0170 = rw.rw_pointer(self.unknown_0x0170)
        self.unknown_0x0174 = rw.rw_pointer(self.unknown_0x0174)
        self.unknown_0x0178 = rw.rw_pointer(self.unknown_0x0178)
        self.unknown_0x017C = rw.rw_pointer(self.unknown_0x017C)
        
        self.unknown_0x0180 = rw.rw_pointer(self.unknown_0x0180)
        self.unknown_0x0184 = rw.rw_pointer(self.unknown_0x0184)
        self.unknown_0x0188 = rw.rw_pointer(self.unknown_0x0188)
        self.unknown_0x018C = rw.rw_pointer(self.unknown_0x018C)
        
        self.unknown_0x0190 = rw.rw_pointer(self.unknown_0x0190)
        self.unknown_0x0194 = rw.rw_pointer(self.unknown_0x0194)
        self.unknown_0x0198 = rw.rw_pad32(self.unknown_0x0198)
        
        rw.assert_is_zero(self.unknown_0x0198)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC, 
                 
                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128,  self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134,  self.unknown_0x0138,  self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0144,  self.unknown_0x0148,  self.unknown_0x014C,
                 self.unknown_0x0150,  self.unknown_0x0154,  self.unknown_0x0158,  self.unknown_0x015C,
                 self.unknown_0x0160,  self.unknown_0x0164,  self.unknown_0x0168,  self.unknown_0x016C,
                 self.unknown_0x0170,  self.unknown_0x0174,  self.unknown_0x0178,  self.unknown_0x017C,
                
                 self.unknown_0x0180,  self.unknown_0x0184,  self.unknown_0x0188,  self.unknown_0x018C,
                 self.unknown_0x0190,  self.unknown_0x0194,  self.unknown_0x0198 )   
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [                0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                  0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                  0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  0xB8,  0xBC,
                  0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                  0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4,  0xF8,  0xFC,
                 0x100, 0x104, 0x108, 0x10C, 0x110, 0x114, 0x118, 0x11C,
                 0x120, 0x124, 0x128, 0x12C, 0x130, 0x134, 0x138, 0x13C,
                 0x140, 0x144, 0x148, 0x14C, 0x150, 0x154, 0x158, 0x15C,
                 0x160, 0x164, 0x168, 0x16C, 0x170, 0x174, 0x178, 0x17C,
                 0x180, 0x184, 0x188, 0x18C, 0x190, 0x194
               ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                  0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                  0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  0xB8,  0xBC,
                  0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                  0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4,  0xF8,  0xFC,
                 0x100, 0x104, 0x108, 0x10C, 0x110, 0x114, 0x118, 0x11C,
                 0x120, 0x124, 0x128, 0x12C, 0x130, 0x134, 0x138, 0x13C,
                 0x140, 0x144, 0x148, 0x14C, 0x150, 0x154, 0x158, 0x15C,
                 0x160, 0x164, 0x168, 0x16C, 0x170, 0x174, 0x178, 0x17C,
                 0x180, 0x184, 0x188, 0x18C, 0x190, 0x194
               ]

    def get_shiftjis_string_ptrs(self):
        return [self.unknown_0x08,  self.unknown_0x0C,
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C,
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C,
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C,
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C,
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C,
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C,
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C,

                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C,
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C,
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC,
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC,
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC,
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC,
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC,

                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128,  self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134,  self.unknown_0x0138,  self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0144,  self.unknown_0x0148,  self.unknown_0x014C,
                 self.unknown_0x0150,  self.unknown_0x0154,  self.unknown_0x0158,  self.unknown_0x015C,
                 self.unknown_0x0160,  self.unknown_0x0164,  self.unknown_0x0168,  self.unknown_0x016C,
                 self.unknown_0x0170,  self.unknown_0x0174,  self.unknown_0x0178,  self.unknown_0x017C,

                 self.unknown_0x0180,  self.unknown_0x0184,  self.unknown_0x0188,  self.unknown_0x018C,
                 self.unknown_0x0190,  self.unknown_0x0194]
    
class VlMxGeneralCharParamSetInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_int32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_int32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58
               ]
    
class VlMxJobInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x74 = 0
        self.unknown_0x78 = 0
        self.unknown_0x7C = 0
        self.unknown_0x80 = 0
        self.unknown_0x84 = 0
        self.unknown_0x88 = 0
        self.unknown_0x8C = 0
        self.unknown_0x90 = 0
        self.unknown_0x94 = 0
        self.unknown_0x98 = 0
        self.unknown_0x9C = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA4 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xAC = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB4 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xBC = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC4 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xCC = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD4 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xDC = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE4 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xEC = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF4 = 0
        self.unknown_0xF8 = 0
        self.unknown_0xFC = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0104 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x010C = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x011C = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0124 = 0
        self.unknown_0x0128 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_pointer(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_pointer(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_pointer(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_int32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_int32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int32(self.unknown_0x70)
        self.unknown_0x74 = rw.rw_int32(self.unknown_0x74)
        self.unknown_0x78 = rw.rw_int32(self.unknown_0x78)
        self.unknown_0x7C = rw.rw_int32(self.unknown_0x7C)
        
        self.unknown_0x80 = rw.rw_int32(self.unknown_0x80)
        self.unknown_0x84 = rw.rw_int32(self.unknown_0x84)
        self.unknown_0x88 = rw.rw_int32(self.unknown_0x88)
        self.unknown_0x8C = rw.rw_int32(self.unknown_0x8C)
        
        self.unknown_0x90 = rw.rw_int32(self.unknown_0x90)
        self.unknown_0x94 = rw.rw_int32(self.unknown_0x94)
        self.unknown_0x98 = rw.rw_int32(self.unknown_0x98)
        self.unknown_0x9C = rw.rw_int32(self.unknown_0x9C)
        
        self.unknown_0xA0 = rw.rw_int32(self.unknown_0xA0)
        self.unknown_0xA4 = rw.rw_int32(self.unknown_0xA4)
        self.unknown_0xA8 = rw.rw_int32(self.unknown_0xA8)
        self.unknown_0xAC = rw.rw_int32(self.unknown_0xAC)
        
        self.unknown_0xB0 = rw.rw_int32(self.unknown_0xB0)
        self.unknown_0xB4 = rw.rw_int32(self.unknown_0xB4)
        self.unknown_0xB8 = rw.rw_int32(self.unknown_0xB8)
        self.unknown_0xBC = rw.rw_int32(self.unknown_0xBC)
        
        self.unknown_0xC0 = rw.rw_int32(self.unknown_0xC0)
        self.unknown_0xC4 = rw.rw_int32(self.unknown_0xC4)
        self.unknown_0xC8 = rw.rw_int32(self.unknown_0xC8)
        self.unknown_0xCC = rw.rw_int32(self.unknown_0xCC)
        
        self.unknown_0xD0 = rw.rw_int32(self.unknown_0xD0)
        self.unknown_0xD4 = rw.rw_int32(self.unknown_0xD4)
        self.unknown_0xD8 = rw.rw_int32(self.unknown_0xD8)
        self.unknown_0xDC = rw.rw_int32(self.unknown_0xDC)
        
        self.unknown_0xE0 = rw.rw_int32(self.unknown_0xE0)
        self.unknown_0xE4 = rw.rw_int32(self.unknown_0xE4)
        self.unknown_0xE8 = rw.rw_int32(self.unknown_0xE8)
        self.unknown_0xEC = rw.rw_int32(self.unknown_0xEC)
        
        self.unknown_0xF0 = rw.rw_int32(self.unknown_0xF0)
        self.unknown_0xF4 = rw.rw_int32(self.unknown_0xF4)
        self.unknown_0xF8 = rw.rw_int32(self.unknown_0xF8)
        self.unknown_0xFC = rw.rw_int32(self.unknown_0xFC)
        
        self.unknown_0x0100 = rw.rw_int32(self.unknown_0x0100)
        self.unknown_0x0104 = rw.rw_int32(self.unknown_0x0104)
        self.unknown_0x0108 = rw.rw_int32(self.unknown_0x0108)
        self.unknown_0x010C = rw.rw_int32(self.unknown_0x010C)
        
        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_int32(self.unknown_0x0118)
        self.unknown_0x011C = rw.rw_int32(self.unknown_0x011C)
        
        self.unknown_0x0120 = rw.rw_int32(self.unknown_0x0120)
        self.unknown_0x0124 = rw.rw_int32(self.unknown_0x0124)
        self.unknown_0x0128 = rw.rw_int32(self.unknown_0x0128)
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC, 
                 
                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128, )
    
    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return [ 0x08, 0x0C, 0x10 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                  0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                  0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  0xB8,  0xBC,
                  0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                  0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4,  0xF8,  0xFC,
                 0x100, 0x104, 0x108, 0x10C, 0x110, 0x114, 0x118, 0x11C,
                 0x120, 0x124, 0x128
               ]

    def get_string_ptrs(self):
        return [self.unknown_0x08, self.unknown_0x0C, self.unknown_0x10]
    
class VlMxMapObjectCommonInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
    
    def get_data(self):
        return ( self.unknown_0x00, )
    
    def asset_table_offsets(self):
        return []
        
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00 ]
    
class VlMxMapObjectInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x04 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24
               ]

    def get_string_ptrs(self):
        return [self.unknown_0x04]
    
class VlMxNewsPaperInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_uint32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_uint32(self.unknown_0x14)
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14  ]
    
class VlMxOrderDirectionInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int64(self.unknown_0x08)
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08, )
    
    def asset_table_offsets(self):
        return [0x08]    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08  ]
    
class VlMxOrderInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1A = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_pointer(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1A = rw.rw_int32(self.unknown_0x1A)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_pad32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_int32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_int32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_uint32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_uint32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_pad32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_pad32(self.unknown_0x54)

        #rw.assert_is_zero(self.unknown_0x24)
        #rw.assert_is_zero(self.unknown_0x48)
        #rw.assert_is_zero(self.unknown_0x54)
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x04, 0x08 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1A, 0x1C,
                  0x20,         0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,         0x4C,  0x50
               ]

    def get_string_ptrs(self):
        return [self.unknown_0x04, self.unknown_0x08]
    
class VlMxParameterConvertTable(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x74 = 0
        self.unknown_0x78 = 0
        self.unknown_0x7C = 0
        self.unknown_0x80 = 0
        self.unknown_0x84 = 0
        self.unknown_0x88 = 0
        self.unknown_0x8C = 0
        self.unknown_0x90 = 0
        self.unknown_0x94 = 0
        self.unknown_0x98 = 0
        self.unknown_0x9C = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA4 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xAC = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB4 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_float32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_float32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_float32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_float32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_float32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_float32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_float32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_float32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_float32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_float32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_float32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_float32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_float32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_float32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_float32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_float32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_float32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_float32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_float32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_float32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_float32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_float32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_float32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_float32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_float32(self.unknown_0x70)
        self.unknown_0x74 = rw.rw_float32(self.unknown_0x74)
        self.unknown_0x78 = rw.rw_float32(self.unknown_0x78)
        self.unknown_0x7C = rw.rw_float32(self.unknown_0x7C)
        
        self.unknown_0x80 = rw.rw_float32(self.unknown_0x80)
        self.unknown_0x84 = rw.rw_float32(self.unknown_0x84)
        self.unknown_0x88 = rw.rw_float32(self.unknown_0x88)
        self.unknown_0x8C = rw.rw_float32(self.unknown_0x8C)
        
        self.unknown_0x90 = rw.rw_float32(self.unknown_0x90)
        self.unknown_0x94 = rw.rw_float32(self.unknown_0x94)
        self.unknown_0x98 = rw.rw_float32(self.unknown_0x98)
        self.unknown_0x9C = rw.rw_float32(self.unknown_0x9C)
        
        self.unknown_0xA0 = rw.rw_float32(self.unknown_0xA0)
        self.unknown_0xA4 = rw.rw_float32(self.unknown_0xA4)
        self.unknown_0xA8 = rw.rw_float32(self.unknown_0xA8)
        self.unknown_0xAC = rw.rw_float32(self.unknown_0xAC)
        
        self.unknown_0xB0 = rw.rw_float32(self.unknown_0xB0)
        self.unknown_0xB4 = rw.rw_pad32(self.unknown_0xB4)
        
        rw.assert_is_zero(self.unknown_0xB4)
    
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                  0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                  0xA0,  0xA4,  0xA8,  0xAC,  0xB0
               ]
    
class VlMxPotentialInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_pointer(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_pad32(self.unknown_0x0C)
        
        
        self.unknown_0x10 = rw.rw_pad32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_pad32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)

        #rw.assert_is_zero(self.unknown_0x0C)
        #rw.assert_is_zero(self.unknown_0x10)
        #rw.assert_is_zero(self.unknown_0x14)
            
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x04, 0x08 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,                       0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,
               ]

    def get_string_ptrs(self):
        return [self.unknown_0x04, self.unknown_0x08]
    
class VlMxSlgInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x20 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_uint32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_uint32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int64(self.unknown_0x18)
        
        self.unknown_0x20 = rw.rw_int64(self.unknown_0x20)
                
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18, 
                 self.unknown_0x20,)
    
    def asset_table_offsets(self):
        return [0x18, 0x20]    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,
                  0x20
               ]
        
class VlMxSlgLandformInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_uint32(self.unknown_0x10)
                
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x04 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10  ]

    def get_string_ptrs(self):
        return [self.unknown_0x04]

class VlMxSlgStrongholdCommonInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_uint32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_uint32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_uint32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_uint32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_uint32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_uint32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_uint32(self.unknown_0x28)
                
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28
               ]
  
class VlMxUnitCommonInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_float32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_float32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_float32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_float32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_float32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_float32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_float32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_float32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_float32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_float32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_float32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_float32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_float32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_float32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_float32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_float32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_float32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_float32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_float32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_float32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_float32(self.unknown_0x60)
            
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60
               ]
    
class VlMxUnitGrowthTypeInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
                
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C  ]
    
class VlMxVehicleCommonInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_uint32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_uint32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_uint32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_uint32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_uint32(self.unknown_0x20)
            
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20
               ]
    
class VlMxVehicleDevChangeParamInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
            
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04 )
    
    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return [ 0x04 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04  ]

    def get_string_ptrs(self):
        return [self.unknown_0x04]
    

class VlMxVehicleDevInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x2E = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x56 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x74 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_pointer(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_pointer(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int16(self.unknown_0x2C)
        self.unknown_0x2E = rw.rw_int16(self.unknown_0x2E)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_int32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_int32(self.unknown_0x3C)

        #rw.assert_is_zero(self.unknown_0x34)

        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_pad32(self.unknown_0x4C)

        #rw.assert_is_zero(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_pad32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_pad16(self.unknown_0x54)
        self.unknown_0x56 = rw.rw_int16(self.unknown_0x56)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)

        #rw.assert_is_zero(self.unknown_0x50)
        #rw.assert_is_zero(self.unknown_0x54)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int32(self.unknown_0x70)
        self.unknown_0x74 = rw.rw_pad32(self.unknown_0x74)

        #rw.assert_is_zero(self.unknown_0x74)
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  
                 self.unknown_0x28,                      self.unknown_0x2C,  self.unknown_0x2E,
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x00, 0x04, 0x08 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x2E,
                  0x30,         0x38,  0x3C, 
                  0x40,  0x44,  0x48,                0x56,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70
               ]

    def get_string_ptrs(self):
        return [self.unknown_0x00, self.unknown_0x04, self.unknown_0x08]
    
class VlMxVehicleEachInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x74 = 0
        self.unknown_0x78 = 0
        self.unknown_0x7C = 0
        self.unknown_0x80 = 0
        self.unknown_0x84 = 0
        self.unknown_0x88 = 0
        self.unknown_0x8C = 0
        self.unknown_0x90 = 0
        self.unknown_0x94 = 0
        self.unknown_0x98 = 0
        self.unknown_0x9C = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA4 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xAC = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB4 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xBC = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC4 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xCC = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD4 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xDC = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE4 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xEC = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF4 = 0
        self.unknown_0xF8 = 0
        self.unknown_0xFC = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0104 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x010C = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x011C = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0124 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x012C = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x013C = 0
        self.unknown_0x0140 = 0
        self.unknown_0x0144 = 0
        self.unknown_0x0148 = 0
        self.unknown_0x014C = 0
        self.unknown_0x0150 = 0
        self.unknown_0x0154 = 0
        self.unknown_0x0158 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_uint32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_uint32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_pointer(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_pointer(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pointer(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pointer(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pointer(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pointer(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_uint32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_uint32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_float32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_pad32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_pad32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_pad32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_float32(self.unknown_0x5C)
        
        rw.assert_is_zero(self.unknown_0x50)
        rw.assert_is_zero(self.unknown_0x54)
        rw.assert_is_zero(self.unknown_0x58)
        
        self.unknown_0x60 = rw.rw_float32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int32(self.unknown_0x70)
        self.unknown_0x74 = rw.rw_int32(self.unknown_0x74)
        self.unknown_0x78 = rw.rw_int32(self.unknown_0x78)
        self.unknown_0x7C = rw.rw_int32(self.unknown_0x7C)
        
        self.unknown_0x80 = rw.rw_int32(self.unknown_0x80)
        self.unknown_0x84 = rw.rw_int32(self.unknown_0x84)
        self.unknown_0x88 = rw.rw_int32(self.unknown_0x88)
        self.unknown_0x8C = rw.rw_int32(self.unknown_0x8C)
        
        self.unknown_0x90 = rw.rw_int32(self.unknown_0x90)
        self.unknown_0x94 = rw.rw_int32(self.unknown_0x94)
        self.unknown_0x98 = rw.rw_int32(self.unknown_0x98)
        self.unknown_0x9C = rw.rw_int32(self.unknown_0x9C)
        
        self.unknown_0xA0 = rw.rw_int32(self.unknown_0xA0)
        self.unknown_0xA4 = rw.rw_int32(self.unknown_0xA4)
        self.unknown_0xA8 = rw.rw_int32(self.unknown_0xA8)
        self.unknown_0xAC = rw.rw_int32(self.unknown_0xAC)
        
        self.unknown_0xB0 = rw.rw_int32(self.unknown_0xB0)
        self.unknown_0xB4 = rw.rw_int32(self.unknown_0xB4)
        self.unknown_0xB8 = rw.rw_int32(self.unknown_0xB8)
        self.unknown_0xBC = rw.rw_int32(self.unknown_0xBC)
        
        self.unknown_0xC0 = rw.rw_int32(self.unknown_0xC0)
        self.unknown_0xC4 = rw.rw_int32(self.unknown_0xC4)
        self.unknown_0xC8 = rw.rw_int32(self.unknown_0xC8)
        self.unknown_0xCC = rw.rw_int32(self.unknown_0xCC)
        
        self.unknown_0xD0 = rw.rw_int32(self.unknown_0xD0)
        self.unknown_0xD4 = rw.rw_int32(self.unknown_0xD4)
        self.unknown_0xD8 = rw.rw_int32(self.unknown_0xD8)
        self.unknown_0xDC = rw.rw_int32(self.unknown_0xDC)
        
        self.unknown_0xE0 = rw.rw_int32(self.unknown_0xE0)
        self.unknown_0xE4 = rw.rw_int32(self.unknown_0xE4)
        self.unknown_0xE8 = rw.rw_int32(self.unknown_0xE8)
        self.unknown_0xEC = rw.rw_int32(self.unknown_0xEC)
        
        self.unknown_0xF0 = rw.rw_int32(self.unknown_0xF0)
        self.unknown_0xF4 = rw.rw_int32(self.unknown_0xF4)
        self.unknown_0xF8 = rw.rw_int32(self.unknown_0xF8)
        self.unknown_0xFC = rw.rw_int32(self.unknown_0xFC)
        
        self.unknown_0x0100 = rw.rw_int32(self.unknown_0x0100)
        self.unknown_0x0104 = rw.rw_int32(self.unknown_0x0104)
        self.unknown_0x0108 = rw.rw_int32(self.unknown_0x0108)
        self.unknown_0x010C = rw.rw_int32(self.unknown_0x010C)
        
        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_int32(self.unknown_0x0118)
        self.unknown_0x011C = rw.rw_int32(self.unknown_0x011C)
        
        self.unknown_0x0120 = rw.rw_int32(self.unknown_0x0120)
        self.unknown_0x0124 = rw.rw_int32(self.unknown_0x0124)
        self.unknown_0x0128 = rw.rw_int32(self.unknown_0x0128)
        self.unknown_0x012C = rw.rw_int32(self.unknown_0x012C)
        
        self.unknown_0x0130 = rw.rw_int32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_int32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_int32(self.unknown_0x0138)
        self.unknown_0x013C = rw.rw_int32(self.unknown_0x013C)
        
        self.unknown_0x0140 = rw.rw_int32(self.unknown_0x0140)
        self.unknown_0x0144 = rw.rw_int32(self.unknown_0x0144)
        self.unknown_0x0148 = rw.rw_int32(self.unknown_0x0148)
        self.unknown_0x014C = rw.rw_int32(self.unknown_0x014C)
        
        self.unknown_0x0150 = rw.rw_int32(self.unknown_0x0150)
        self.unknown_0x0154 = rw.rw_int32(self.unknown_0x0154)
        self.unknown_0x0158 = rw.rw_int32(self.unknown_0x0158)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC, 
                 
                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128,  self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134,  self.unknown_0x0138,  self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0144,  self.unknown_0x0148,  self.unknown_0x014C,
                 self.unknown_0x0150,  self.unknown_0x0154,  self.unknown_0x0158, )
    
    def asset_table_offsets(self):
        return []
        
    def pof0_offsets(self):
        return [ 0x18, 0x24, 0x28, 0x2C, 0x30, 0x34 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,                       0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                  0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                  0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  0xB8,  0xBC,
                  0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                  0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4,  0xF8,  0xFC,
                 0x100, 0x104, 0x108, 0x10C, 0x110, 0x114, 0x118, 0x11C,
                 0x120, 0x124, 0x128, 0x12C, 0x130, 0x134, 0x138, 0x13C,
                 0x140, 0x144, 0x148, 0x14C, 0x150, 0x154, 0x158
               ]

    def get_string_ptrs(self):
        return [self.unknown_0x18, self.unknown_0x24, self.unknown_0x28, self.unknown_0x2C, self.unknown_0x30, self.unknown_0x34]

class VlMxVehicleInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x84 = 0
        self.unknown_0x88 = 0
        self.unknown_0x8C = 0
        self.unknown_0x90 = 0
        self.unknown_0x94 = 0
        self.unknown_0x98 = 0
        self.unknown_0x9C = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA4 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xAC = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB4 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xBC = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC4 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xCC = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_pointer(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_pointer(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_pointer(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_pointer(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_pointer(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_uint32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pointer(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pointer(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_float32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_uint32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_uint32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_uint32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_float32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_float32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_float32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_float32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_float32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_float32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int32(self.unknown_0x80)
        self.unknown_0x84 = rw.rw_int32(self.unknown_0x84)
        self.unknown_0x88 = rw.rw_int32(self.unknown_0x88)
        self.unknown_0x8C = rw.rw_int32(self.unknown_0x8C)
        
        self.unknown_0x90 = rw.rw_int32(self.unknown_0x90)
        self.unknown_0x94 = rw.rw_int32(self.unknown_0x94)
        self.unknown_0x98 = rw.rw_int32(self.unknown_0x98)
        self.unknown_0x9C = rw.rw_int32(self.unknown_0x9C)
        
        self.unknown_0xA0 = rw.rw_int32(self.unknown_0xA0)
        self.unknown_0xA4 = rw.rw_int32(self.unknown_0xA4)
        self.unknown_0xA8 = rw.rw_int32(self.unknown_0xA8)
        self.unknown_0xAC = rw.rw_pad32(self.unknown_0xAC)

        #rw.assert_is_zero(self.unknown_0xAC)
        
        self.unknown_0xB0 = rw.rw_pad32(self.unknown_0xB0)
        self.unknown_0xB4 = rw.rw_pad32(self.unknown_0xB4)
        self.unknown_0xB8 = rw.rw_int32(self.unknown_0xB8)
        self.unknown_0xBC = rw.rw_int32(self.unknown_0xBC)

        #rw.assert_is_zero(self.unknown_0xB0)
        #rw.assert_is_zero(self.unknown_0xB4)
  
        self.unknown_0xC0 = rw.rw_int32(self.unknown_0xC0)
        self.unknown_0xC4 = rw.rw_int32(self.unknown_0xC4)
        self.unknown_0xC8 = rw.rw_int32(self.unknown_0xC8)
        self.unknown_0xCC = rw.rw_pad32(self.unknown_0xCC)

        #rw.assert_is_zero(self.unknown_0xCC)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC)
    
    def asset_table_offsets(self):
        return [0x70, 0x78]
        
    def pof0_offsets(self):
        return [ 0x04, 0x08, 0x0C, 0x10, 0x14, 0x18, 0x28 ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,         0x78,
                  0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                  0xA0,  0xA4,  0xA8,                       0xB8,  0xBC,
                  0xC0,  0xC4,  0xC8
               ]

    def get_string_ptrs(self):
        return [self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C,
                self.unknown_0x10, self.unknown_0x14, self.unknown_0x18,
                self.unknown_0x28]
    
class VlMxWeaponBringOnUnwholesomeInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_uint32(self.unknown_0x10)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10, )
    
    def asset_table_offsets(self):
        return []        
    
    def pof0_offsets(self):
        return [ ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10  ]

class VlMxWeaponCommonInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04, )
    
    def asset_table_offsets(self):
        return []      
    
    def pof0_offsets(self):
        return [ ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04  ]

class VlMxWeaponInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x10 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x74 = 0
        self.unknown_0x78 = 0
        self.unknown_0x7C = 0
        self.unknown_0x80 = 0
        self.unknown_0x84 = 0
        self.unknown_0x88 = 0
        self.unknown_0x8C = 0
        self.unknown_0x90 = 0
        self.unknown_0x94 = 0
        self.unknown_0x98 = 0
        self.unknown_0x9C = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA4 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xAC = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB4 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xBC = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC4 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xCC = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD4 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xDC = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE4 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xEC = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF4 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_pointer(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int64(self.unknown_0x08)

        self.unknown_0x10 = rw.rw_int64(self.unknown_0x10)
        self.unknown_0x18 = rw.rw_uint32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_float32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_float32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_float32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_uint32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_uint32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_uint32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_float32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_float32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_float32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_float32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_float32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_float32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int32(self.unknown_0x70)
        self.unknown_0x74 = rw.rw_int32(self.unknown_0x74)
        self.unknown_0x78 = rw.rw_int32(self.unknown_0x78)
        self.unknown_0x7C = rw.rw_int32(self.unknown_0x7C)
        
        self.unknown_0x80 = rw.rw_int32(self.unknown_0x80)
        self.unknown_0x84 = rw.rw_int32(self.unknown_0x84)
        self.unknown_0x88 = rw.rw_int32(self.unknown_0x88)
        self.unknown_0x8C = rw.rw_int32(self.unknown_0x8C)
        
        self.unknown_0x90 = rw.rw_int32(self.unknown_0x90)
        self.unknown_0x94 = rw.rw_int32(self.unknown_0x94)
        self.unknown_0x98 = rw.rw_int32(self.unknown_0x98)
        self.unknown_0x9C = rw.rw_int32(self.unknown_0x9C)
        
        self.unknown_0xA0 = rw.rw_int32(self.unknown_0xA0)
        self.unknown_0xA4 = rw.rw_int32(self.unknown_0xA4)
        self.unknown_0xA8 = rw.rw_int32(self.unknown_0xA8)
        self.unknown_0xAC = rw.rw_int32(self.unknown_0xAC)
        
        self.unknown_0xB0 = rw.rw_int32(self.unknown_0xB0)
        self.unknown_0xB4 = rw.rw_int32(self.unknown_0xB4)
        self.unknown_0xB8 = rw.rw_int32(self.unknown_0xB8)
        self.unknown_0xBC = rw.rw_int32(self.unknown_0xBC)
        
        self.unknown_0xC0 = rw.rw_int32(self.unknown_0xC0)
        self.unknown_0xC4 = rw.rw_int32(self.unknown_0xC4)
        self.unknown_0xC8 = rw.rw_int32(self.unknown_0xC8)
        self.unknown_0xCC = rw.rw_int32(self.unknown_0xCC)
        
        self.unknown_0xD0 = rw.rw_int32(self.unknown_0xD0)
        self.unknown_0xD4 = rw.rw_int32(self.unknown_0xD4)
        self.unknown_0xD8 = rw.rw_int32(self.unknown_0xD8)
        self.unknown_0xDC = rw.rw_int32(self.unknown_0xDC)
        
        self.unknown_0xE0 = rw.rw_int32(self.unknown_0xE0)
        self.unknown_0xE4 = rw.rw_int32(self.unknown_0xE4)
        self.unknown_0xE8 = rw.rw_int32(self.unknown_0xE8)
        self.unknown_0xEC = rw.rw_int32(self.unknown_0xEC)
        
        self.unknown_0xF0 = rw.rw_int32(self.unknown_0xF0)
        self.unknown_0xF4 = rw.rw_int32(self.unknown_0xF4)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08, 
                 self.unknown_0x10,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC,
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC,
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC,
                 self.unknown_0xF0,  self.unknown_0xF4)
    
    def asset_table_offsets(self):
        return [0x08, 0x10]     
    
    def pof0_offsets(self):
        return [ 0x00, 0x04  ]
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,         0x10,         0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                  0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                  0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  0xB8,  0xBC,
                  0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                  0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4
               ]

    def get_string_ptrs(self):
        return [self.unknown_0x00, self.unknown_0x04]

class VlMxBookDecorationInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.id = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0

    def read_write(self, rw):
        self.id = rw.rw_uint32(self.id)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_pointer(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_pointer(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_pointer(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_pointer(self.unknown_0x14)
    
    def get_data(self):
        return (self.id, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C,
                self.unknown_0x10, self.unknown_0x14, )

    def get_string_ptrs(self):
        return [self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C, self.unknown_0x10, self.unknown_0x14]

class VlMxBookHistoryInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.id = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0

    def read_write(self, rw):
        self.id = rw.rw_uint32(self.id)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_uint32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_uint32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_uint32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_uint32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_uint32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_uint32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_uint32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_uint32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_uint32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_uint32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_uint32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_uint32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_uint32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_uint32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_uint32(self.unknown_0x54)
    
    def get_data(self):
        return (self.id, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C,
                self.unknown_0x10, self.unknown_0x14, self.unknown_0x18, self.unknown_0x1C,
                self.unknown_0x20, self.unknown_0x24, self.unknown_0x28, self.unknown_0x2C,
                self.unknown_0x30, self.unknown_0x34, self.unknown_0x38, self.unknown_0x3C,
                self.unknown_0x40, self.unknown_0x44, self.unknown_0x48, self.unknown_0x4C,
                self.unknown_0x50, self.unknown_0x54 )

    def get_string_ptrs(self):
        return (self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C,
                self.unknown_0x10, self.unknown_0x14, self.unknown_0x18, self.unknown_0x1C,
                self.unknown_0x20, self.unknown_0x24, self.unknown_0x28, self.unknown_0x2C,
                self.unknown_0x30, self.unknown_0x34, self.unknown_0x38, self.unknown_0x3C,
                self.unknown_0x40, self.unknown_0x44, self.unknown_0x48, self.unknown_0x4C,
                self.unknown_0x50, self.unknown_0x54 )

  
class VlMxBookPersonInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x74 = 0
        self.unknown_0x78 = 0
        self.unknown_0x7C = 0
        self.unknown_0x80 = 0
        self.unknown_0x84 = 0
        self.unknown_0x88 = 0
        self.unknown_0x8C = 0
        self.unknown_0x90 = 0
        self.unknown_0x94 = 0
        self.unknown_0x98 = 0
        self.unknown_0x9C = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA4 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xAC = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB4 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xBC = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC4 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xCC = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD4 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xDC = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE4 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xEC = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF4 = 0
        self.unknown_0xF8 = 0
        self.unknown_0xFC = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0104 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x010C = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x011C = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0124 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x012C = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x013C = 0
        self.unknown_0x0140 = 0
        self.unknown_0x0144 = 0
        self.unknown_0x0148 = 0
        self.unknown_0x014C = 0
        self.unknown_0x0150 = 0
        self.unknown_0x0154 = 0
        self.unknown_0x0158 = 0
        self.unknown_0x015C = 0
        self.unknown_0x0160 = 0
        self.unknown_0x0164 = 0
        self.unknown_0x0168 = 0
        self.unknown_0x016C = 0
        self.unknown_0x0170 = 0
        self.unknown_0x0174 = 0
        self.unknown_0x0178 = 0
        self.unknown_0x017C = 0
        self.unknown_0x0180 = 0
        self.unknown_0x0184 = 0
        self.unknown_0x0188 = 0
        self.unknown_0x018C = 0
        self.unknown_0x0190 = 0
        self.unknown_0x0194 = 0
        self.unknown_0x0198 = 0
        self.unknown_0x019C = 0
        self.unknown_0x01A0 = 0
        self.unknown_0x01A4 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_pointer(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_pointer(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_pointer(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_pointer(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_pointer(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_pointer(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_pointer(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_pointer(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pointer(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pointer(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pointer(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pointer(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pointer(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pointer(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_pointer(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_pointer(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_pointer(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_pointer(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_pointer(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_pointer(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_uint32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_uint32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_uint32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_uint32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_uint32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_uint32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_uint32(self.unknown_0x70)
        self.unknown_0x74 = rw.rw_uint32(self.unknown_0x74)
        self.unknown_0x78 = rw.rw_uint32(self.unknown_0x78)
        self.unknown_0x7C = rw.rw_uint32(self.unknown_0x7C)
        
        self.unknown_0x80 = rw.rw_uint32(self.unknown_0x80)
        self.unknown_0x84 = rw.rw_uint32(self.unknown_0x84)
        self.unknown_0x88 = rw.rw_uint32(self.unknown_0x88)
        self.unknown_0x8C = rw.rw_uint32(self.unknown_0x8C)
        
        self.unknown_0x90 = rw.rw_uint32(self.unknown_0x90)
        self.unknown_0x94 = rw.rw_uint32(self.unknown_0x94)
        self.unknown_0x98 = rw.rw_uint32(self.unknown_0x98)
        self.unknown_0x9C = rw.rw_uint32(self.unknown_0x9C)
        
        self.unknown_0xA0 = rw.rw_uint32(self.unknown_0xA0)
        self.unknown_0xA4 = rw.rw_uint32(self.unknown_0xA4)
        self.unknown_0xA8 = rw.rw_uint32(self.unknown_0xA8)
        self.unknown_0xAC = rw.rw_uint32(self.unknown_0xAC)
        
        self.unknown_0xB0 = rw.rw_uint32(self.unknown_0xB0)
        self.unknown_0xB4 = rw.rw_uint32(self.unknown_0xB4)
        self.unknown_0xB8 = rw.rw_uint32(self.unknown_0xB8)
        self.unknown_0xBC = rw.rw_uint32(self.unknown_0xBC)
        
        self.unknown_0xC0 = rw.rw_uint32(self.unknown_0xC0)
        self.unknown_0xC4 = rw.rw_uint32(self.unknown_0xC4)
        self.unknown_0xC8 = rw.rw_uint32(self.unknown_0xC8)
        self.unknown_0xCC = rw.rw_uint32(self.unknown_0xCC)
        
        self.unknown_0xD0 = rw.rw_uint32(self.unknown_0xD0)
        self.unknown_0xD4 = rw.rw_uint32(self.unknown_0xD4)
        self.unknown_0xD8 = rw.rw_uint32(self.unknown_0xD8)
        self.unknown_0xDC = rw.rw_uint32(self.unknown_0xDC)
        
        self.unknown_0xE0 = rw.rw_uint32(self.unknown_0xE0)
        self.unknown_0xE4 = rw.rw_uint32(self.unknown_0xE4)
        self.unknown_0xE8 = rw.rw_uint32(self.unknown_0xE8)
        self.unknown_0xEC = rw.rw_uint32(self.unknown_0xEC)
        
        self.unknown_0xF0 = rw.rw_uint32(self.unknown_0xF0)
        self.unknown_0xF4 = rw.rw_uint32(self.unknown_0xF4)
        self.unknown_0xF8 = rw.rw_uint32(self.unknown_0xF8)
        self.unknown_0xFC = rw.rw_uint32(self.unknown_0xFC)
        
        self.unknown_0x0100 = rw.rw_uint32(self.unknown_0x0100)
        self.unknown_0x0104 = rw.rw_uint32(self.unknown_0x0104)
        self.unknown_0x0108 = rw.rw_uint32(self.unknown_0x0108)
        self.unknown_0x010C = rw.rw_uint32(self.unknown_0x010C)
        
        self.unknown_0x0110 = rw.rw_uint32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_uint32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_uint32(self.unknown_0x0118)
        self.unknown_0x011C = rw.rw_uint32(self.unknown_0x011C)
        
        self.unknown_0x0120 = rw.rw_uint32(self.unknown_0x0120)
        self.unknown_0x0124 = rw.rw_uint32(self.unknown_0x0124)
        self.unknown_0x0128 = rw.rw_uint32(self.unknown_0x0128)
        self.unknown_0x012C = rw.rw_uint32(self.unknown_0x012C)
        
        self.unknown_0x0130 = rw.rw_uint32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_uint32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_uint32(self.unknown_0x0138)
        self.unknown_0x013C = rw.rw_uint32(self.unknown_0x013C)
        
        self.unknown_0x0140 = rw.rw_uint32(self.unknown_0x0140)
        self.unknown_0x0144 = rw.rw_uint32(self.unknown_0x0144)
        self.unknown_0x0148 = rw.rw_uint32(self.unknown_0x0148)
        self.unknown_0x014C = rw.rw_uint32(self.unknown_0x014C)
        
        self.unknown_0x0150 = rw.rw_uint32(self.unknown_0x0150)
        self.unknown_0x0154 = rw.rw_uint32(self.unknown_0x0154)
        self.unknown_0x0158 = rw.rw_uint32(self.unknown_0x0158)
        self.unknown_0x015C = rw.rw_uint32(self.unknown_0x015C)
        
        self.unknown_0x0160 = rw.rw_uint32(self.unknown_0x0160)
        self.unknown_0x0164 = rw.rw_uint32(self.unknown_0x0164)
        self.unknown_0x0168 = rw.rw_uint32(self.unknown_0x0168)
        self.unknown_0x016C = rw.rw_uint32(self.unknown_0x016C)
        
        self.unknown_0x0170 = rw.rw_uint32(self.unknown_0x0170)
        self.unknown_0x0174 = rw.rw_uint32(self.unknown_0x0174)
        self.unknown_0x0178 = rw.rw_uint32(self.unknown_0x0178)
        self.unknown_0x017C = rw.rw_uint32(self.unknown_0x017C)
        
        self.unknown_0x0180 = rw.rw_uint32(self.unknown_0x0180)
        self.unknown_0x0184 = rw.rw_uint32(self.unknown_0x0184)
        self.unknown_0x0188 = rw.rw_uint32(self.unknown_0x0188)
        self.unknown_0x018C = rw.rw_uint32(self.unknown_0x018C)
        
        self.unknown_0x0190 = rw.rw_uint32(self.unknown_0x0190)
        self.unknown_0x0194 = rw.rw_uint32(self.unknown_0x0194)
        self.unknown_0x0198 = rw.rw_uint32(self.unknown_0x0198)
        self.unknown_0x019C = rw.rw_uint32(self.unknown_0x019C)
        
        self.unknown_0x01A0 = rw.rw_uint32(self.unknown_0x01A0)
        self.unknown_0x01A4 = rw.rw_uint32(self.unknown_0x01A4)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC, 
                 
                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128,  self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134,  self.unknown_0x0138,  self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0144,  self.unknown_0x0148,  self.unknown_0x014C,
                 self.unknown_0x0150,  self.unknown_0x0154,  self.unknown_0x0158,  self.unknown_0x015C,
                 self.unknown_0x0160,  self.unknown_0x0164,  self.unknown_0x0168,  self.unknown_0x016C,
                 self.unknown_0x0170,  self.unknown_0x0174,  self.unknown_0x0178,  self.unknown_0x017C,
                
                 self.unknown_0x0180,  self.unknown_0x0184,  self.unknown_0x0188,  self.unknown_0x018C,
                 self.unknown_0x0190,  self.unknown_0x0194,  self.unknown_0x0198,  self.unknown_0x019C,
                 self.unknown_0x01A0,  self.unknown_0x01A4, )   

    def get_string_ptrs(self):
        return (self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C,
                self.unknown_0x10, self.unknown_0x14, self.unknown_0x18, self.unknown_0x1C,
                self.unknown_0x20, self.unknown_0x24, self.unknown_0x28, self.unknown_0x2C,
                self.unknown_0x30, self.unknown_0x34, self.unknown_0x38, self.unknown_0x3C,
                self.unknown_0x40, self.unknown_0x44, self.unknown_0x48, self.unknown_0x4C,
                self.unknown_0x50, self.unknown_0x54)

class VlMxBookSoundInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08, )

    def get_string_ptrs(self):
        return (self.unknown_0x04,)
    
class EnTalkEventObjParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x38 = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int64(self.unknown_0x30)
        self.unknown_0x38 = rw.rw_int64(self.unknown_0x38)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x38)
        
        self.unknown_0x40 = rw.rw_uint32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_uint32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_uint32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_uint32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_uint32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_uint32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_uint32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_uint32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_uint32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_uint32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_uint32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_uint32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_int64(self.unknown_0xF8)  # Padding
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_int64(self.unknown_0x0100)  # Padding
        self.unknown_0x0108 = rw.rw_int64(self.unknown_0x0108)  # Padding
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x28, 
                 self.unknown_0x30,  self.unknown_0x38, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C, 
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118
              ]
    
class EnEventDecorParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x100 = 0
        self.unknown_0x108 = 0
        self.unknown_0x110 = 0
        self.unknown_0x118 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_uint32(self.unknown_0x28)  # Padding
        self.unknown_0x2C = rw.rw_uint32(self.unknown_0x2C)  # Padding
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_uint32(self.unknown_0x30)  # Padding
        self.unknown_0x34 = rw.rw_uint32(self.unknown_0x34)  # Padding
        self.unknown_0x38 = rw.rw_uint32(self.unknown_0x38)  # Padding
        self.unknown_0x3C = rw.rw_uint32(self.unknown_0x3C)  # Padding
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_uint32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_uint32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_uint32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_uint32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_uint32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_uint32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_uint32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_uint32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_uint32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_uint32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_uint32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_uint32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_int64(self.unknown_0xF8)  # Padding
        
        self.unknown_0x100 = rw.rw_int64(self.unknown_0x100)  # Padding
        self.unknown_0x108 = rw.rw_int64(self.unknown_0x108)  # Padding
        
        self.unknown_0x110 = rw.rw_int64(self.unknown_0x110)
        self.unknown_0x118 = rw.rw_int64(self.unknown_0x118)  # Padding
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C,
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C,
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C,  
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C,
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C,
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C,
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C,
                 self.unknown_0x70,  self.unknown_0x78,  
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,  
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,  
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,  
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,  
                 self.unknown_0x100, self.unknown_0x108,
                 self.unknown_0x110, self.unknown_0x118
                 )   
         
    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,
                0x110,]
    
class EnHeightMapParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        # THESE ALL SEEM TO BE FLAGS
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)  # Padding
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)  # Padding

        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)

        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)  # Padding
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)  # Padding
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)  # Padding
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)  # Padding

        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)

        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)  # Padding
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)  # Padding
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)  # Padding
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C,
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C,
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C,  
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C,  
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C,
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C,
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C,
                 self.unknown_0x70,  self.unknown_0x78,  
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,  
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,  
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,  
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 self.unknown_0x0100, self.unknown_0x0108,
                 self.unknown_0x0110, self.unknown_0x0118)
    

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x118]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0, 
                 0x110, 0x118,
                 ]
      
class EnSkyParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x38 = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad64(self.unknown_0x30)
        self.unknown_0x38 = rw.rw_pad64(self.unknown_0x38)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x38)
        
        self.unknown_0x40 = rw.rw_uint32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_uint32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_uint32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_uint32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_uint32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_uint32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_uint32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_uint32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_uint32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_uint32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_uint32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_uint32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)  # Padding

        rw.assert_is_zero(self.unknown_0xF8)

        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)  # Padding
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)  # Padding

        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)

        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_pad64(self.unknown_0x0118)  # Padding

        rw.assert_is_zero(self.unknown_0x0118)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C,
                 self.unknown_0x30,  self.unknown_0x38, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,
                0x110, 0x114 ]
      
class VlMxBookWeaponInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.id = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x74 = 0
        self.unknown_0x78 = 0
        self.unknown_0x7C = 0
        self.unknown_0x80 = 0
        self.unknown_0x84 = 0
        self.unknown_0x88 = 0
        self.unknown_0x8C = 0
        self.unknown_0x90 = 0
        self.unknown_0x94 = 0
        self.unknown_0x98 = 0
        self.unknown_0x9C = 0

    def read_write(self, rw):
        self.id = rw.rw_uint32(self.id)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_pointer(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_pointer(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_pointer(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_pointer(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_pointer(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_pointer(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_pointer(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_pointer(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pointer(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pointer(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pointer(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pointer(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pointer(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pointer(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_pointer(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_pointer(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_pointer(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_pointer(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_pointer(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_pointer(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_pointer(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_uint32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_uint32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_uint32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_uint32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_uint32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_uint32(self.unknown_0x70)
        self.unknown_0x74 = rw.rw_uint32(self.unknown_0x74)
        self.unknown_0x78 = rw.rw_uint32(self.unknown_0x78)
        self.unknown_0x7C = rw.rw_uint32(self.unknown_0x7C)
        
        self.unknown_0x80 = rw.rw_uint32(self.unknown_0x80)
        self.unknown_0x84 = rw.rw_uint32(self.unknown_0x84)
        self.unknown_0x88 = rw.rw_uint32(self.unknown_0x88)
        self.unknown_0x8C = rw.rw_uint32(self.unknown_0x8C)
        
        self.unknown_0x90 = rw.rw_uint32(self.unknown_0x90)
        self.unknown_0x94 = rw.rw_uint32(self.unknown_0x94)
        self.unknown_0x98 = rw.rw_uint32(self.unknown_0x98)
        self.unknown_0x9C = rw.rw_uint32(self.unknown_0x9C)
    
    def get_data(self):
        return (self.id, self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C,
                self.unknown_0x10, self.unknown_0x14, self.unknown_0x18, self.unknown_0x1C,
                self.unknown_0x20, self.unknown_0x24, self.unknown_0x28, self.unknown_0x2C,
                self.unknown_0x30, self.unknown_0x34, self.unknown_0x38, self.unknown_0x3C,
                self.unknown_0x40, self.unknown_0x44, self.unknown_0x48, self.unknown_0x4C,
                self.unknown_0x50, self.unknown_0x54, self.unknown_0x58, self.unknown_0x5C,
                self.unknown_0x60, self.unknown_0x64, self.unknown_0x68, self.unknown_0x6C,
                self.unknown_0x70, self.unknown_0x74, self.unknown_0x78, self.unknown_0x7C,

                self.unknown_0x80, self.unknown_0x84, self.unknown_0x88, self.unknown_0x8C,
                self.unknown_0x90, self.unknown_0x94, self.unknown_0x98, self.unknown_0x9C )

    def get_string_ptrs(self):
        return (self.unknown_0x04, self.unknown_0x08, self.unknown_0x0C,
                self.unknown_0x10, self.unknown_0x14, self.unknown_0x18, self.unknown_0x1C,
                self.unknown_0x20, self.unknown_0x24, self.unknown_0x28, self.unknown_0x2C,
                self.unknown_0x30, self.unknown_0x34, self.unknown_0x38, self.unknown_0x3C,
                self.unknown_0x40, self.unknown_0x44, self.unknown_0x48, self.unknown_0x4C,
                self.unknown_0x50, self.unknown_0x54, self.unknown_0x58)
  
class VlMxCanvasShaderParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x74 = 0
        self.unknown_0x78 = 0
        self.unknown_0x7C = 0
        self.unknown_0x80 = 0
        self.unknown_0x84 = 0
        self.unknown_0x88 = 0
        self.unknown_0x8C = 0
        self.unknown_0x90 = 0
        self.unknown_0x94 = 0
        self.unknown_0x98 = 0
        self.unknown_0x9C = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA4 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xAC = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB4 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xBC = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC4 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xCC = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD4 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xDC = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE4 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xEC = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF4 = 0
        self.unknown_0xF8 = 0
        self.unknown_0xFC = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0104 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x010C = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x011C = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0124 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x012C = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x013C = 0
        self.unknown_0x0140 = 0
        self.unknown_0x0144 = 0
        self.unknown_0x0148 = 0
        self.unknown_0x014C = 0
        self.unknown_0x0150 = 0
        self.unknown_0x0154 = 0
        self.unknown_0x0158 = 0
        self.unknown_0x015C = 0
        self.unknown_0x0160 = 0
        self.unknown_0x0164 = 0
        self.unknown_0x0168 = 0
        self.unknown_0x016C = 0
        self.unknown_0x0170 = 0
        self.unknown_0x0174 = 0
        self.unknown_0x0178 = 0
        self.unknown_0x017C = 0
        self.unknown_0x0180 = 0
        self.unknown_0x0184 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_uint32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_uint32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_uint32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_uint32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_uint32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_uint32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_uint32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_uint32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_uint32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_uint32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_uint32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_uint32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_uint32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_uint32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_uint32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_uint32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_uint32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_uint32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_uint32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_uint32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_uint32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_uint32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_uint32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_uint32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_uint32(self.unknown_0x70)
        self.unknown_0x74 = rw.rw_uint32(self.unknown_0x74)
        self.unknown_0x78 = rw.rw_uint32(self.unknown_0x78)
        self.unknown_0x7C = rw.rw_uint32(self.unknown_0x7C)
        
        self.unknown_0x80 = rw.rw_uint32(self.unknown_0x80)
        self.unknown_0x84 = rw.rw_uint32(self.unknown_0x84)
        self.unknown_0x88 = rw.rw_uint32(self.unknown_0x88)
        self.unknown_0x8C = rw.rw_uint32(self.unknown_0x8C)
        
        self.unknown_0x90 = rw.rw_uint32(self.unknown_0x90)
        self.unknown_0x94 = rw.rw_uint32(self.unknown_0x94)
        self.unknown_0x98 = rw.rw_uint32(self.unknown_0x98)
        self.unknown_0x9C = rw.rw_uint32(self.unknown_0x9C)
        
        self.unknown_0xA0 = rw.rw_uint32(self.unknown_0xA0)
        self.unknown_0xA4 = rw.rw_uint32(self.unknown_0xA4)
        self.unknown_0xA8 = rw.rw_uint32(self.unknown_0xA8)
        self.unknown_0xAC = rw.rw_uint32(self.unknown_0xAC)
        
        self.unknown_0xB0 = rw.rw_uint32(self.unknown_0xB0)
        self.unknown_0xB4 = rw.rw_uint32(self.unknown_0xB4)
        self.unknown_0xB8 = rw.rw_uint32(self.unknown_0xB8)
        self.unknown_0xBC = rw.rw_uint32(self.unknown_0xBC)
        
        self.unknown_0xC0 = rw.rw_uint32(self.unknown_0xC0)
        self.unknown_0xC4 = rw.rw_uint32(self.unknown_0xC4)
        self.unknown_0xC8 = rw.rw_uint32(self.unknown_0xC8)
        self.unknown_0xCC = rw.rw_uint32(self.unknown_0xCC)
        
        self.unknown_0xD0 = rw.rw_uint32(self.unknown_0xD0)
        self.unknown_0xD4 = rw.rw_uint32(self.unknown_0xD4)
        self.unknown_0xD8 = rw.rw_uint32(self.unknown_0xD8)
        self.unknown_0xDC = rw.rw_uint32(self.unknown_0xDC)
        
        self.unknown_0xE0 = rw.rw_uint32(self.unknown_0xE0)
        self.unknown_0xE4 = rw.rw_uint32(self.unknown_0xE4)
        self.unknown_0xE8 = rw.rw_uint32(self.unknown_0xE8)
        self.unknown_0xEC = rw.rw_uint32(self.unknown_0xEC)
        
        self.unknown_0xF0 = rw.rw_uint32(self.unknown_0xF0)
        self.unknown_0xF4 = rw.rw_uint32(self.unknown_0xF4)
        self.unknown_0xF8 = rw.rw_uint32(self.unknown_0xF8)
        self.unknown_0xFC = rw.rw_uint32(self.unknown_0xFC)
        
        self.unknown_0x0100 = rw.rw_uint32(self.unknown_0x0100)
        self.unknown_0x0104 = rw.rw_uint32(self.unknown_0x0104)
        self.unknown_0x0108 = rw.rw_uint32(self.unknown_0x0108)
        self.unknown_0x010C = rw.rw_uint32(self.unknown_0x010C)
        
        self.unknown_0x0110 = rw.rw_uint32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_uint32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_uint32(self.unknown_0x0118)
        self.unknown_0x011C = rw.rw_uint32(self.unknown_0x011C)
        
        self.unknown_0x0120 = rw.rw_uint32(self.unknown_0x0120)
        self.unknown_0x0124 = rw.rw_uint32(self.unknown_0x0124)
        self.unknown_0x0128 = rw.rw_uint32(self.unknown_0x0128)
        self.unknown_0x012C = rw.rw_uint32(self.unknown_0x012C)
        
        self.unknown_0x0130 = rw.rw_uint32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_uint32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_uint32(self.unknown_0x0138)
        self.unknown_0x013C = rw.rw_uint32(self.unknown_0x013C)
        
        self.unknown_0x0140 = rw.rw_uint32(self.unknown_0x0140)
        self.unknown_0x0144 = rw.rw_uint32(self.unknown_0x0144)
        self.unknown_0x0148 = rw.rw_uint32(self.unknown_0x0148)
        self.unknown_0x014C = rw.rw_uint32(self.unknown_0x014C)
        
        self.unknown_0x0150 = rw.rw_uint32(self.unknown_0x0150)
        self.unknown_0x0154 = rw.rw_uint32(self.unknown_0x0154)
        self.unknown_0x0158 = rw.rw_uint32(self.unknown_0x0158)
        self.unknown_0x015C = rw.rw_uint32(self.unknown_0x015C)
        
        self.unknown_0x0160 = rw.rw_uint32(self.unknown_0x0160)
        self.unknown_0x0164 = rw.rw_uint32(self.unknown_0x0164)
        self.unknown_0x0168 = rw.rw_uint32(self.unknown_0x0168)
        self.unknown_0x016C = rw.rw_uint32(self.unknown_0x016C)
        
        self.unknown_0x0170 = rw.rw_uint32(self.unknown_0x0170)
        self.unknown_0x0174 = rw.rw_uint32(self.unknown_0x0174)
        self.unknown_0x0178 = rw.rw_uint32(self.unknown_0x0178)
        self.unknown_0x017C = rw.rw_uint32(self.unknown_0x017C)
        
        self.unknown_0x0180 = rw.rw_uint32(self.unknown_0x0180)
        self.unknown_0x0184 = rw.rw_uint32(self.unknown_0x0184)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC, 
                 
                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128,  self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134,  self.unknown_0x0138,  self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0144,  self.unknown_0x0148,  self.unknown_0x014C,
                 self.unknown_0x0150,  self.unknown_0x0154,  self.unknown_0x0158,  self.unknown_0x015C,
                 self.unknown_0x0160,  self.unknown_0x0164,  self.unknown_0x0168,  self.unknown_0x016C,
                 self.unknown_0x0170,  self.unknown_0x0174,  self.unknown_0x0178,  self.unknown_0x017C,
                
                 self.unknown_0x0180,  self.unknown_0x0184,  )   
    
 
class MxParameterTextureMerge(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x08 = 0
        self.padding_0x10 = 0
        self.padding_0x18 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int64(self.unknown_0x00)
        self.unknown_0x08 = rw.rw_int64(self.unknown_0x08)
        
        self.padding_0x10 = rw.rw_pad64(self.padding_0x10)
        self.padding_0x18 = rw.rw_pad64(self.padding_0x18)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x08, 
                 self.padding_0x10,  self.padding_0x18,  )
 
    def asset_table_offsets(self):
        return [0x00, 0x08]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x08 ]
    
class MxParameterMergeFile(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x08 = 0
        self.padding_0x10 = 0
        self.padding_0x18 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int64(self.unknown_0x00)
        self.unknown_0x08 = rw.rw_int64(self.unknown_0x08)

        self.padding_0x10 = rw.rw_pad64(self.padding_0x10)
        self.padding_0x18 = rw.rw_pad64(self.padding_0x18)
        
        rw.assert_is_zero(self.padding_0x10)
        rw.assert_is_zero(self.padding_0x18)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x08, 
                 self.padding_0x10,  self.padding_0x18,  )
    
    def asset_table_offsets(self):
        return [0x00, 0x08]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x08 ]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128, 0x12C,
                0x130, 0x134, 0x138]
    
class VlMxDrawModelLodParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_uint32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_uint32(self.unknown_0x14)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14, )
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14 ]
    
class VlMapObjectParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
    
    def get_data(self):
        return ( self.unknown_0x00,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00 ]
    
    
class EnTreeParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x012C = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x013C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)  # Padding
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)  # Padding
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)  # Padding
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
        self.unknown_0x0120 = rw.rw_int64(self.unknown_0x0120)
        self.unknown_0x0128 = rw.rw_int32(self.unknown_0x0128)
        self.unknown_0x012C = rw.rw_int32(self.unknown_0x012C)
        
        self.unknown_0x0130 = rw.rw_int32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_int32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_int32(self.unknown_0x0138)
        self.unknown_0x013C = rw.rw_int32(self.unknown_0x013C)
        
        rw.assert_is_zero(self.unknown_0x013C)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78, 
                 
                 self.unknown_0x80,  self.unknown_0x88, 
                 self.unknown_0x90,  self.unknown_0x98, 
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8, 
                 self.unknown_0xD0,  self.unknown_0xD8, 
                 self.unknown_0xE0,  self.unknown_0xE8, 
                 self.unknown_0xF0,  self.unknown_0xF8, 
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128, self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134, self.unknown_0x0138, self.unknown_0x013C )   

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118, 0x120]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128, 0x12C,
                0x130, 0x134, 0x138]

class EnWaterSurfaceParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34)
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34]
  
class SlgEnGrassPathNodeParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
                
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)

        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)

        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0
               ]
    
class SlgMapObjectParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.padding_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x10 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.padding_0x04 = rw.rw_pad32(self.padding_0x04)
        self.unknown_0x08 = rw.rw_int64(self.unknown_0x08)
        
        rw.assert_is_zero(self.padding_0x04)
        
        self.unknown_0x10 = rw.rw_int64(self.unknown_0x10)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08, 
                 self.unknown_0x10,  self.unknown_0x18,  self.unknown_0x1C,  )
        
    def asset_table_offsets(self):
        return [0x08, 0x10]    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x08,  0x10,  0x18,  0x1C ]
  
class SlgEnGrassParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0124 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x012C = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x013C = 0
        self.unknown_0x0140 = 0
        self.unknown_0x0144 = 0
        self.unknown_0x0148 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
        self.unknown_0x0120 = rw.rw_int32(self.unknown_0x0120)
        self.unknown_0x0124 = rw.rw_int32(self.unknown_0x0124)
        self.unknown_0x0128 = rw.rw_int32(self.unknown_0x0128)
        self.unknown_0x012C = rw.rw_int32(self.unknown_0x012C)
        
        self.unknown_0x0130 = rw.rw_int32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_int32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_int32(self.unknown_0x0138)
        self.unknown_0x013C = rw.rw_int32(self.unknown_0x013C)
        
        self.unknown_0x0140 = rw.rw_int32(self.unknown_0x0140)
        self.unknown_0x0144 = rw.rw_int32(self.unknown_0x0144)
        self.unknown_0x0148 = rw.rw_pad64(self.unknown_0x0148)

        rw.assert_is_zero(self.unknown_0x0148)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114, self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0124, self.unknown_0x0128, self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134, self.unknown_0x0138, self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0144, self.unknown_0x0148,
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x118]

    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118,
                0x120, 0x124, 0x128, 0x12C,
                0x130, 0x134, 0x138, 0x13C,
                0x140, 0x144]
    
class StaticBox(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_float32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        
        
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_float32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_float32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_float32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_float32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_float32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_float32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_float32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_float32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_float32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_float32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_float32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_float32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_pad32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_pad32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_pad32(self.unknown_0x4C)
        
        rw.assert_is_zero(self.unknown_0x44)
        rw.assert_is_zero(self.unknown_0x48)
        rw.assert_is_zero(self.unknown_0x4C)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C )
    
    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [0x00, 0x04, 0x08, 0x0C, 0x10, 0x14, 0x18, 0x1C,
                0x20, 0x24, 0x28, 0x2C, 0x30, 0x34, 0x38, 0x3C,
                0x40]
    
class EnUvScrollParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)  # Padding
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)  # Padding
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)  # Padding
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)  # Padding
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)  # Padding
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)  # Padding
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_pad64(self.unknown_0x0118)
        
        rw.assert_is_zero(self.unknown_0x0118)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110,]
    
    
class SlgEnBreakableStructureParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x013C = 0
        self.unknown_0x0140 = 0
        self.unknown_0x0148 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)

        rw.assert_is_zero(self.unknown_0xF8)

        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)

        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
        self.unknown_0x0120 = rw.rw_int64(self.unknown_0x0120)
        self.unknown_0x0128 = rw.rw_int64(self.unknown_0x0128)
        
        self.unknown_0x0130 = rw.rw_int32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_int32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_int32(self.unknown_0x0138)
        self.unknown_0x013C = rw.rw_int32(self.unknown_0x013C)
        
        self.unknown_0x0140 = rw.rw_int64(self.unknown_0x0140)
        self.unknown_0x0148 = rw.rw_int64(self.unknown_0x0148)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128,
                 self.unknown_0x0130,  self.unknown_0x0134, self.unknown_0x0138, self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0148
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x118, 0x120, 0x128, 0x140]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128,
                0x130, 0x134, 0x138, 0x13C,
                0x140, 0x148]
    
class EnConvexParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)  # Padding
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)  # Padding

        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)

        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)  # Padding
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)  # Padding
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)  # Padding
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)  # Padding

        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)

        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)  # Padding
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)  # Padding
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)  # Padding
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78, 
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8, 
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8, 
                 self.unknown_0xF0,  self.unknown_0xF8, 
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,)  
    
    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x118]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,
                0x110, 0x114, 0x118]
       
class EnCEffectParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0128 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)  # Padding
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)  # Padding
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)  # Padding
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)  # Padding
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)  # Padding
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)  # Padding
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)  # Padding
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)  # Padding
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)  # Padding
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
    
        self.unknown_0x0120 = rw.rw_int64(self.unknown_0x0120)
        self.unknown_0x0128 = rw.rw_pad64(self.unknown_0x0128)  # Padding
        
        rw.assert_is_zero(self.unknown_0x0128)
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88, 
                 self.unknown_0x90,  self.unknown_0x98, 
                 self.unknown_0xA0,  self.unknown_0xA8,
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8, 
                 self.unknown_0xD0,  self.unknown_0xD8, 
                 self.unknown_0xE0,  self.unknown_0xE8, 
                 self.unknown_0xF0,  self.unknown_0xF8, 
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128,)  
          
    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120,]
    
class VlMxBriefingInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x74 = 0
        self.unknown_0x78 = 0
        self.unknown_0x7C = 0
        self.unknown_0x80 = 0
        self.unknown_0x84 = 0
        self.unknown_0x88 = 0
        self.unknown_0x8C = 0
        self.unknown_0x90 = 0
        self.unknown_0x94 = 0
        self.unknown_0x98 = 0
        self.unknown_0x9C = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA4 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xAC = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB4 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xBC = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC4 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xCC = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD4 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xDC = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE4 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xEC = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF4 = 0
        self.unknown_0xF8 = 0
        self.unknown_0xFC = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pad32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_pointer(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_pointer(self.unknown_0x0C)

        # rw.assert_is_zero(self.unknown_0x04)
        
        self.unknown_0x10 = rw.rw_pointer(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_pointer(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_pointer(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_pointer(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_pointer(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_pointer(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pointer(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pointer(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pointer(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pointer(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pointer(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pointer(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_pointer(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_pointer(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_pointer(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_pointer(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_pointer(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_pointer(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int32(self.unknown_0x70)
        self.unknown_0x74 = rw.rw_int32(self.unknown_0x74)
        self.unknown_0x78 = rw.rw_int32(self.unknown_0x78)
        self.unknown_0x7C = rw.rw_int32(self.unknown_0x7C)
        
        self.unknown_0x80 = rw.rw_int32(self.unknown_0x80)
        self.unknown_0x84 = rw.rw_int32(self.unknown_0x84)
        self.unknown_0x88 = rw.rw_int32(self.unknown_0x88)
        self.unknown_0x8C = rw.rw_int32(self.unknown_0x8C)
        
        self.unknown_0x90 = rw.rw_int32(self.unknown_0x90)
        self.unknown_0x94 = rw.rw_int32(self.unknown_0x94)
        self.unknown_0x98 = rw.rw_int32(self.unknown_0x98)
        self.unknown_0x9C = rw.rw_int32(self.unknown_0x9C)
        
        self.unknown_0xA0 = rw.rw_int32(self.unknown_0xA0)
        self.unknown_0xA4 = rw.rw_int32(self.unknown_0xA4)
        self.unknown_0xA8 = rw.rw_int32(self.unknown_0xA8)
        self.unknown_0xAC = rw.rw_int32(self.unknown_0xAC)
        
        self.unknown_0xB0 = rw.rw_int32(self.unknown_0xB0)
        self.unknown_0xB4 = rw.rw_int32(self.unknown_0xB4)
        self.unknown_0xB8 = rw.rw_int32(self.unknown_0xB8)
        self.unknown_0xBC = rw.rw_int32(self.unknown_0xBC)
        
        self.unknown_0xC0 = rw.rw_int32(self.unknown_0xC0)
        self.unknown_0xC4 = rw.rw_int32(self.unknown_0xC4)
        self.unknown_0xC8 = rw.rw_int32(self.unknown_0xC8)
        self.unknown_0xCC = rw.rw_int32(self.unknown_0xCC)
        
        self.unknown_0xD0 = rw.rw_int32(self.unknown_0xD0)
        self.unknown_0xD4 = rw.rw_int32(self.unknown_0xD4)
        self.unknown_0xD8 = rw.rw_int32(self.unknown_0xD8)
        self.unknown_0xDC = rw.rw_int32(self.unknown_0xDC)
        
        self.unknown_0xE0 = rw.rw_int32(self.unknown_0xE0)
        self.unknown_0xE4 = rw.rw_int32(self.unknown_0xE4)
        self.unknown_0xE8 = rw.rw_int32(self.unknown_0xE8)
        self.unknown_0xEC = rw.rw_int32(self.unknown_0xEC)
        
        self.unknown_0xF0 = rw.rw_int32(self.unknown_0xF0)
        self.unknown_0xF4 = rw.rw_int32(self.unknown_0xF4)
        self.unknown_0xF8 = rw.rw_pointer(self.unknown_0xF8)
        self.unknown_0xFC = rw.rw_int32(self.unknown_0xFC)
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC,)
   
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [            0x08, 0x0C, 0x10, 0x14, 0x18, 0x1C,
                0x20, 0x24, 0x28, 0x2C, 0x30, 0x34, 0x38, 0x3C,
                0x40, 0x44, 0x48, 0x4C, 0x50, 0x54,
                0xF8
               ]
    
    def enrs_offsets(self):
        return [ 0x00,         0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                 0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                 0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  0xB8,  0xBC,
                 0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                 0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4,  0xF8,  0xFC
               ]

    def get_string_ptrs(self):
        return [ self.unknown_0x08,  self.unknown_0x0C,
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C,
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C,
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C,
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C,
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0xF8
               ]

class VlMxFieldInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x10 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x40 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int64(self.unknown_0x08)
        
        self.unknown_0x10 = rw.rw_int64(self.unknown_0x10)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_int64(self.unknown_0x38)
        
        self.unknown_0x40 = rw.rw_int64(self.unknown_0x40)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08, 
                 self.unknown_0x10,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38, 
                 self.unknown_0x40,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54 )
    
    def asset_table_offsets(self):
        return [0x08, 0x10, 0x40]
        
    
    def pof0_offsets(self):
        return [ 0x00, 0x04, 0x1C ]
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,         0x10,         0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,
                 0x40,  0x48,  0x4C,  0x50,  0x54
               ]
          
class VlMxResultInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pad32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)

        # rw.assert_is_zero(self.unknown_0x04)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_int32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_int32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return [ 0x08 ]
    
    def enrs_offsets(self):
        return [  0x00,         0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C
               ]
  
    
class VlMxStageInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x18 = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x74 = 0
        self.unknown_0x78 = 0
        self.unknown_0x7C = 0
        self.unknown_0x80 = 0
        self.unknown_0x84 = 0
        self.unknown_0x88 = 0
        self.unknown_0x8C = 0
        self.unknown_0x90 = 0
        self.unknown_0x94 = 0
        self.unknown_0x98 = 0
        self.unknown_0x9C = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA4 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xAC = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB4 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xBC = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC4 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xCC = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD4 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xDC = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE4 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xEC = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF4 = 0
        self.unknown_0xF8 = 0
        self.unknown_0xFC = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0104 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x010C = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x011C = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0124 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x012C = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x013C = 0
        self.unknown_0x0140 = 0
        self.unknown_0x0144 = 0
        self.unknown_0x0148 = 0
        self.unknown_0x014C = 0
        self.unknown_0x0150 = 0
        self.unknown_0x0154 = 0
        self.unknown_0x0158 = 0
        self.unknown_0x015C = 0
        self.unknown_0x0160 = 0
        self.unknown_0x0164 = 0
        self.unknown_0x0168 = 0
        self.unknown_0x016C = 0
        self.unknown_0x0170 = 0
        self.unknown_0x0174 = 0
        self.unknown_0x0178 = 0
        self.unknown_0x017C = 0
        self.unknown_0x0180 = 0
        self.unknown_0x0184 = 0
        self.unknown_0x0188 = 0
        self.unknown_0x018C = 0
        self.unknown_0x018E = 0
        self.unknown_0x0190 = 0
        self.unknown_0x0194 = 0
        self.unknown_0x0198 = 0
        self.unknown_0x019C = 0
        self.unknown_0x01A0 = 0
        self.unknown_0x01A4 = 0
        self.unknown_0x01A8 = 0
        self.unknown_0x01AC = 0
        self.unknown_0x01B0 = 0
        self.unknown_0x01B4 = 0
        self.unknown_0x01B8 = 0
        self.unknown_0x01BC = 0
        self.unknown_0x01C0 = 0
        self.unknown_0x01C4 = 0
        self.unknown_0x01C8 = 0
        self.unknown_0x01CC = 0
        self.unknown_0x01D0 = 0
        self.unknown_0x01D4 = 0
        self.unknown_0x01D8 = 0
        self.unknown_0x01DC = 0
        self.unknown_0x01E0 = 0
        self.unknown_0x01E4 = 0
        self.unknown_0x01E6 = 0
        self.unknown_0x01E8 = 0
        self.unknown_0x01EA = 0
        self.unknown_0x01EC = 0
        self.unknown_0x01EE = 0
        self.unknown_0x01F0 = 0
        self.unknown_0x01F2 = 0
        self.unknown_0x01F4 = 0
        self.unknown_0x01F6 = 0
        self.unknown_0x01F8 = 0
        self.unknown_0x01FA = 0
        self.unknown_0x01FC = 0
        self.unknown_0x01FE = 0
        self.unknown_0x0200 = 0
        self.unknown_0x0202 = 0
        self.unknown_0x0204 = 0
        self.unknown_0x0206 = 0
        self.unknown_0x0208 = 0
        self.unknown_0x020A = 0
        self.unknown_0x020C = 0
        self.unknown_0x0210 = 0
        self.unknown_0x0214 = 0
        self.unknown_0x0216 = 0
        self.unknown_0x0218 = 0
        self.unknown_0x021C = 0
        self.unknown_0x0220 = 0
        self.unknown_0x0224 = 0
        self.unknown_0x0228 = 0
        self.unknown_0x022C = 0
        self.unknown_0x0230 = 0
        self.unknown_0x0234 = 0
        self.unknown_0x0238 = 0
        self.unknown_0x023C = 0
        self.unknown_0x0240 = 0
        self.unknown_0x0244 = 0
        self.unknown_0x0248 = 0
        self.unknown_0x024C = 0
        self.unknown_0x0250 = 0
        self.unknown_0x0254 = 0
        self.unknown_0x0258 = 0
        self.unknown_0x025C = 0
        self.unknown_0x0260 = 0
        self.unknown_0x0264 = 0
        self.unknown_0x0268 = 0
        self.unknown_0x026C = 0
        self.unknown_0x026E = 0
        self.unknown_0x0270 = 0
        self.unknown_0x0272 = 0
        self.unknown_0x0274 = 0
        self.unknown_0x0276 = 0
        self.unknown_0x0278 = 0
        self.unknown_0x027A = 0
        self.unknown_0x027C = 0
        self.unknown_0x027E = 0
        self.unknown_0x0280 = 0
        self.unknown_0x0282 = 0
        self.unknown_0x0284 = 0
        self.unknown_0x0286 = 0
        self.unknown_0x0288 = 0
        self.unknown_0x028A = 0
        self.unknown_0x028C = 0
        self.unknown_0x028E = 0
        self.unknown_0x0290 = 0
        self.unknown_0x0292 = 0
        self.unknown_0x0294 = 0
        self.unknown_0x0298 = 0
        self.unknown_0x029C = 0
        self.unknown_0x02A0 = 0
        self.unknown_0x02A4 = 0
        self.unknown_0x02A8 = 0
        self.unknown_0x02AC = 0
        self.unknown_0x02B0 = 0
        self.unknown_0x02B4 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pad32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)

        # rw.assert_is_zero(self.unknown_0x04)

        self.unknown_0x10 = rw.rw_int64(self.unknown_0x10)
        self.unknown_0x18 = rw.rw_int64(self.unknown_0x18)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_int32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_int32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_uint32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_uint32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_uint32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_uint32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_uint32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_uint32(self.unknown_0x70)
        self.unknown_0x74 = rw.rw_uint32(self.unknown_0x74)
        self.unknown_0x78 = rw.rw_uint32(self.unknown_0x78)
        self.unknown_0x7C = rw.rw_int32(self.unknown_0x7C)
        
        self.unknown_0x80 = rw.rw_int32(self.unknown_0x80)
        self.unknown_0x84 = rw.rw_int32(self.unknown_0x84)
        self.unknown_0x88 = rw.rw_int32(self.unknown_0x88)
        self.unknown_0x8C = rw.rw_int32(self.unknown_0x8C)
        
        self.unknown_0x90 = rw.rw_int32(self.unknown_0x90)
        self.unknown_0x94 = rw.rw_int32(self.unknown_0x94)
        self.unknown_0x98 = rw.rw_int32(self.unknown_0x98)
        self.unknown_0x9C = rw.rw_int32(self.unknown_0x9C)
        
        self.unknown_0xA0 = rw.rw_int32(self.unknown_0xA0)
        self.unknown_0xA4 = rw.rw_int32(self.unknown_0xA4)
        self.unknown_0xA8 = rw.rw_uint32(self.unknown_0xA8)
        self.unknown_0xAC = rw.rw_int32(self.unknown_0xAC)
        
        self.unknown_0xB0 = rw.rw_int32(self.unknown_0xB0)
        self.unknown_0xB4 = rw.rw_int32(self.unknown_0xB4)
        self.unknown_0xB8 = rw.rw_int32(self.unknown_0xB8)
        self.unknown_0xBC = rw.rw_int32(self.unknown_0xBC)
        
        self.unknown_0xC0 = rw.rw_int32(self.unknown_0xC0)
        self.unknown_0xC4 = rw.rw_int32(self.unknown_0xC4)
        self.unknown_0xC8 = rw.rw_uint32(self.unknown_0xC8)
        self.unknown_0xCC = rw.rw_uint32(self.unknown_0xCC)
        
        self.unknown_0xD0 = rw.rw_uint32(self.unknown_0xD0)
        self.unknown_0xD4 = rw.rw_int32(self.unknown_0xD4)
        self.unknown_0xD8 = rw.rw_int32(self.unknown_0xD8)
        self.unknown_0xDC = rw.rw_int32(self.unknown_0xDC)
        
        self.unknown_0xE0 = rw.rw_int32(self.unknown_0xE0)
        self.unknown_0xE4 = rw.rw_int32(self.unknown_0xE4)
        self.unknown_0xE8 = rw.rw_int32(self.unknown_0xE8)
        self.unknown_0xEC = rw.rw_int32(self.unknown_0xEC)
        
        self.unknown_0xF0 = rw.rw_int32(self.unknown_0xF0)
        self.unknown_0xF4 = rw.rw_int32(self.unknown_0xF4)
        self.unknown_0xF8 = rw.rw_int32(self.unknown_0xF8)
        self.unknown_0xFC = rw.rw_int32(self.unknown_0xFC)
        
        self.unknown_0x0100 = rw.rw_int32(self.unknown_0x0100)
        self.unknown_0x0104 = rw.rw_int32(self.unknown_0x0104)
        self.unknown_0x0108 = rw.rw_int32(self.unknown_0x0108)
        self.unknown_0x010C = rw.rw_int32(self.unknown_0x010C)
        
        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_int32(self.unknown_0x0118)
        self.unknown_0x011C = rw.rw_int32(self.unknown_0x011C)
        
        self.unknown_0x0120 = rw.rw_int32(self.unknown_0x0120)
        self.unknown_0x0124 = rw.rw_int32(self.unknown_0x0124)
        self.unknown_0x0128 = rw.rw_int32(self.unknown_0x0128)
        self.unknown_0x012C = rw.rw_int32(self.unknown_0x012C)
        
        self.unknown_0x0130 = rw.rw_int32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_int32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_int32(self.unknown_0x0138)
        self.unknown_0x013C = rw.rw_int32(self.unknown_0x013C)
        
        self.unknown_0x0140 = rw.rw_int32(self.unknown_0x0140)
        self.unknown_0x0144 = rw.rw_int32(self.unknown_0x0144)
        self.unknown_0x0148 = rw.rw_int32(self.unknown_0x0148)
        self.unknown_0x014C = rw.rw_int32(self.unknown_0x014C)
        
        self.unknown_0x0150 = rw.rw_int32(self.unknown_0x0150)
        self.unknown_0x0154 = rw.rw_int32(self.unknown_0x0154)
        self.unknown_0x0158 = rw.rw_int32(self.unknown_0x0158)
        self.unknown_0x015C = rw.rw_int32(self.unknown_0x015C)
        
        self.unknown_0x0160 = rw.rw_int32(self.unknown_0x0160)
        self.unknown_0x0164 = rw.rw_int32(self.unknown_0x0164)
        self.unknown_0x0168 = rw.rw_int32(self.unknown_0x0168)
        self.unknown_0x016C = rw.rw_int32(self.unknown_0x016C)
        
        self.unknown_0x0170 = rw.rw_int32(self.unknown_0x0170)
        self.unknown_0x0174 = rw.rw_int32(self.unknown_0x0174)
        self.unknown_0x0178 = rw.rw_int32(self.unknown_0x0178)
        self.unknown_0x017C = rw.rw_int32(self.unknown_0x017C)
        
        self.unknown_0x0180 = rw.rw_int32(self.unknown_0x0180)
        self.unknown_0x0184 = rw.rw_int32(self.unknown_0x0184)
        self.unknown_0x0188 = rw.rw_int32(self.unknown_0x0188)
        self.unknown_0x018C = rw.rw_int16(self.unknown_0x018C)
        self.unknown_0x018E = rw.rw_int16(self.unknown_0x018E)
        
        self.unknown_0x0190 = rw.rw_int32(self.unknown_0x0190)
        self.unknown_0x0194 = rw.rw_int32(self.unknown_0x0194)
        self.unknown_0x0198 = rw.rw_int32(self.unknown_0x0198)
        self.unknown_0x019C = rw.rw_int32(self.unknown_0x019C)
        
        self.unknown_0x01A0 = rw.rw_int32(self.unknown_0x01A0)
        self.unknown_0x01A4 = rw.rw_int32(self.unknown_0x01A4)
        self.unknown_0x01A8 = rw.rw_int32(self.unknown_0x01A8)
        self.unknown_0x01AC = rw.rw_int32(self.unknown_0x01AC)
        
        self.unknown_0x01B0 = rw.rw_int32(self.unknown_0x01B0)
        self.unknown_0x01B4 = rw.rw_int32(self.unknown_0x01B4)
        self.unknown_0x01B8 = rw.rw_int32(self.unknown_0x01B8)
        self.unknown_0x01BC = rw.rw_int32(self.unknown_0x01BC)
        
        self.unknown_0x01C0 = rw.rw_int32(self.unknown_0x01C0)
        self.unknown_0x01C4 = rw.rw_int32(self.unknown_0x01C4)
        self.unknown_0x01C8 = rw.rw_int32(self.unknown_0x01C8)
        self.unknown_0x01CC = rw.rw_int32(self.unknown_0x01CC)
        
        self.unknown_0x01D0 = rw.rw_int32(self.unknown_0x01D0)
        self.unknown_0x01D4 = rw.rw_int32(self.unknown_0x01D4)
        self.unknown_0x01D8 = rw.rw_int32(self.unknown_0x01D8)
        self.unknown_0x01DC = rw.rw_int32(self.unknown_0x01DC)
        
        self.unknown_0x01E0 = rw.rw_int32(self.unknown_0x01E0)
        self.unknown_0x01E4 = rw.rw_int16(self.unknown_0x01E4)
        self.unknown_0x01E6 = rw.rw_int16(self.unknown_0x01E6)
        self.unknown_0x01E8 = rw.rw_int16(self.unknown_0x01E8)
        self.unknown_0x01EA = rw.rw_int16(self.unknown_0x01EA)
        self.unknown_0x01EC = rw.rw_int16(self.unknown_0x01EC)
        self.unknown_0x01EE = rw.rw_int16(self.unknown_0x01EE)
        
        self.unknown_0x01F0 = rw.rw_int16(self.unknown_0x01F0)
        self.unknown_0x01F2 = rw.rw_int16(self.unknown_0x01F2)
        self.unknown_0x01F4 = rw.rw_int16(self.unknown_0x01F4)
        self.unknown_0x01F6 = rw.rw_int16(self.unknown_0x01F6)
        self.unknown_0x01F8 = rw.rw_int16(self.unknown_0x01F8)
        self.unknown_0x01FA = rw.rw_int16(self.unknown_0x01FA)
        self.unknown_0x01FC = rw.rw_int16(self.unknown_0x01FC)
        self.unknown_0x01FE = rw.rw_int16(self.unknown_0x01FE)
        
        self.unknown_0x0200 = rw.rw_int16(self.unknown_0x0200)
        self.unknown_0x0202 = rw.rw_int16(self.unknown_0x0202)
        self.unknown_0x0204 = rw.rw_int16(self.unknown_0x0204)
        self.unknown_0x0206 = rw.rw_int16(self.unknown_0x0206)
        self.unknown_0x0208 = rw.rw_int16(self.unknown_0x0208)
        self.unknown_0x020A = rw.rw_int16(self.unknown_0x020A)
        self.unknown_0x020C = rw.rw_int32(self.unknown_0x020C)
        
        self.unknown_0x0210 = rw.rw_int32(self.unknown_0x0210)
        self.unknown_0x0214 = rw.rw_int16(self.unknown_0x0214)
        self.unknown_0x0216 = rw.rw_int16(self.unknown_0x0216)
        self.unknown_0x0218 = rw.rw_int32(self.unknown_0x0218)
        self.unknown_0x021C = rw.rw_int32(self.unknown_0x021C)
        
        self.unknown_0x0220 = rw.rw_int32(self.unknown_0x0220)
        self.unknown_0x0224 = rw.rw_int32(self.unknown_0x0224)
        self.unknown_0x0228 = rw.rw_int32(self.unknown_0x0228)
        self.unknown_0x022C = rw.rw_int32(self.unknown_0x022C)
        
        self.unknown_0x0230 = rw.rw_int32(self.unknown_0x0230)
        self.unknown_0x0234 = rw.rw_int32(self.unknown_0x0234)
        self.unknown_0x0238 = rw.rw_int32(self.unknown_0x0238)
        self.unknown_0x023C = rw.rw_int32(self.unknown_0x023C)
        
        self.unknown_0x0240 = rw.rw_int32(self.unknown_0x0240)
        self.unknown_0x0244 = rw.rw_int32(self.unknown_0x0244)
        self.unknown_0x0248 = rw.rw_int32(self.unknown_0x0248)
        self.unknown_0x024C = rw.rw_int32(self.unknown_0x024C)
        
        self.unknown_0x0250 = rw.rw_int32(self.unknown_0x0250)
        self.unknown_0x0254 = rw.rw_int32(self.unknown_0x0254)
        self.unknown_0x0258 = rw.rw_int32(self.unknown_0x0258)
        self.unknown_0x025C = rw.rw_int32(self.unknown_0x025C)
        
        self.unknown_0x0260 = rw.rw_int32(self.unknown_0x0260)
        self.unknown_0x0264 = rw.rw_int32(self.unknown_0x0264)
        self.unknown_0x0268 = rw.rw_int32(self.unknown_0x0268)
        self.unknown_0x026C = rw.rw_int16(self.unknown_0x026C)
        self.unknown_0x026E = rw.rw_int16(self.unknown_0x026E)
        
        self.unknown_0x0270 = rw.rw_int16(self.unknown_0x0270)
        self.unknown_0x0272 = rw.rw_int16(self.unknown_0x0272)
        self.unknown_0x0274 = rw.rw_int16(self.unknown_0x0274)
        self.unknown_0x0276 = rw.rw_int16(self.unknown_0x0276)
        self.unknown_0x0278 = rw.rw_int16(self.unknown_0x0278)
        self.unknown_0x027A = rw.rw_int16(self.unknown_0x027A)
        self.unknown_0x027C = rw.rw_int16(self.unknown_0x027C)
        self.unknown_0x027E = rw.rw_int16(self.unknown_0x027E)
        
        self.unknown_0x0280 = rw.rw_int16(self.unknown_0x0280)
        self.unknown_0x0282 = rw.rw_int16(self.unknown_0x0282)
        self.unknown_0x0284 = rw.rw_int16(self.unknown_0x0284)
        self.unknown_0x0286 = rw.rw_int16(self.unknown_0x0286)
        self.unknown_0x0288 = rw.rw_int16(self.unknown_0x0288)
        self.unknown_0x028A = rw.rw_int16(self.unknown_0x028A)
        self.unknown_0x028C = rw.rw_int16(self.unknown_0x028C)
        self.unknown_0x028E = rw.rw_int16(self.unknown_0x028E)
        
        self.unknown_0x0290 = rw.rw_int16(self.unknown_0x0290)
        self.unknown_0x0292 = rw.rw_int16(self.unknown_0x0292)
        self.unknown_0x0294 = rw.rw_int32(self.unknown_0x0294)
        self.unknown_0x0298 = rw.rw_int32(self.unknown_0x0298)
        self.unknown_0x029C = rw.rw_int32(self.unknown_0x029C)
        
        self.unknown_0x02A0 = rw.rw_int32(self.unknown_0x02A0)
        self.unknown_0x02A4 = rw.rw_int32(self.unknown_0x02A4)
        self.unknown_0x02A8 = rw.rw_int32(self.unknown_0x02A8)
        self.unknown_0x02AC = rw.rw_int32(self.unknown_0x02AC)
        
        self.unknown_0x02B0 = rw.rw_int32(self.unknown_0x02B0)
        self.unknown_0x02B4 = rw.rw_int32(self.unknown_0x02B4)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x18, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC, 
                 
                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C, 
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C, 
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128,  self.unknown_0x012C, 
                 self.unknown_0x0130,  self.unknown_0x0134,  self.unknown_0x0138,  self.unknown_0x013C, 
                 self.unknown_0x0140,  self.unknown_0x0144,  self.unknown_0x0148,  self.unknown_0x014C, 
                 self.unknown_0x0150,  self.unknown_0x0154,  self.unknown_0x0158,  self.unknown_0x015C, 
                 self.unknown_0x0160,  self.unknown_0x0164,  self.unknown_0x0168,  self.unknown_0x016C, 
                 self.unknown_0x0170,  self.unknown_0x0174,  self.unknown_0x0178,  self.unknown_0x017C, 
                 
                 self.unknown_0x0180,  self.unknown_0x0184,  self.unknown_0x0188,  self.unknown_0x018C, self.unknown_0x018E,
                 self.unknown_0x0190,  self.unknown_0x0194,  self.unknown_0x0198,  self.unknown_0x019C, 
                 self.unknown_0x01A0,  self.unknown_0x01A4,  self.unknown_0x01A8,  self.unknown_0x01AC, 
                 self.unknown_0x01B0,  self.unknown_0x01B4,  self.unknown_0x01B8,  self.unknown_0x01BC,
                 self.unknown_0x01C0,  self.unknown_0x01C4,  self.unknown_0x01C8,  self.unknown_0x01CC, 
                 self.unknown_0x01D0,  self.unknown_0x01D4,  self.unknown_0x01D8,  self.unknown_0x01DC, 
                 self.unknown_0x01E0,  self.unknown_0x01E4,  self.unknown_0x01E6,  
                 self.unknown_0x01E8,  self.unknown_0x01EA,  self.unknown_0x01EC,  self.unknown_0x01EE,
                 self.unknown_0x01F0,  self.unknown_0x01F2,  self.unknown_0x01F4,  self.unknown_0x01F6, 
                 self.unknown_0x01F8,  self.unknown_0x01FA,  self.unknown_0x01FC,  self.unknown_0x01FE,
                 
                 self.unknown_0x0200,  self.unknown_0x0202,  self.unknown_0x0204,  self.unknown_0x0206,
                 self.unknown_0x0208,  self.unknown_0x020A,  self.unknown_0x020C, 
                 self.unknown_0x0210,  self.unknown_0x0214,  self.unknown_0x0216,
                 self.unknown_0x0218,  self.unknown_0x021C, 
                 self.unknown_0x0220,  self.unknown_0x0224,  self.unknown_0x0228,  self.unknown_0x022C, 
                 self.unknown_0x0230,  self.unknown_0x0234,  self.unknown_0x0238,  self.unknown_0x023C, 
                 self.unknown_0x0240,  self.unknown_0x0244,  self.unknown_0x0248,  self.unknown_0x024C, 
                 self.unknown_0x0250,  self.unknown_0x0254,  self.unknown_0x0258,  self.unknown_0x025C, 
                 self.unknown_0x0260,  self.unknown_0x0264,  
                 self.unknown_0x0268,  self.unknown_0x026C,  self.unknown_0x026E,
                 self.unknown_0x0270,  self.unknown_0x0272,  self.unknown_0x0274,  self.unknown_0x0276, 
                 self.unknown_0x0278,  self.unknown_0x027A,  self.unknown_0x027C,  self.unknown_0x027E,
                
                 self.unknown_0x0280,  self.unknown_0x0282,  self.unknown_0x0284,  self.unknown_0x0286,
                 self.unknown_0x0288,  self.unknown_0x028A,  self.unknown_0x028C,  self.unknown_0x028E,
                 
                 self.unknown_0x0290,  self.unknown_0x0292,  self.unknown_0x0294,  
                 self.unknown_0x0298,  self.unknown_0x029C, 
                 self.unknown_0x02A0,  self.unknown_0x02A4,  self.unknown_0x02A8,  self.unknown_0x02AC, 
                 self.unknown_0x02B0,  self.unknown_0x02B4,  
                 )
    
    def asset_table_offsets(self):
        return [0x10, 0x18]   
    
    def pof0_offsets(self):
        return [ 0x5C, 
                 0x60, 0x64, 0x68, 0x6C, 0x70, 0x74, 0x78, 
                 0xA8, 0xC8, 0xCC, 0xD0 
               ]
    
    def enrs_offsets(self):
        return [  0x00,         0x08,  0x0C,  0x10,         0x18,
                  0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C, 
                  0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C, 
                  0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                  0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                  0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  0xB8,  0xBC,
                  0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                  0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4,  0xF8,  0xFC,
                 0x100, 0x104, 0x108, 0x10C, 0x110, 0x114, 0x118, 0x11C,
                 0x120, 0x124, 0x128, 0x12C, 0x130, 0x134, 0x138, 0x13C,
                 0x140, 0x144, 0x148, 0x14C, 0x150, 0x154, 0x158, 0x15C,
                 0x160, 0x164, 0x168, 0x16C, 0x170, 0x174, 0x178, 0x17C,
                 0x180, 0x184, 0x188, 0x18C, 0x18E, 
                 0x190, 0x194, 0x198, 0x19C, 0x1A0, 0x1A4, 0x1A8, 0x1AC,
                 0x1B0, 0x1B4, 0x1B8, 0x1BC, 0x1C0, 0x1C4, 0x1C8, 0x1CC,
                 0x1D0, 0x1D4, 0x1D8, 0x1DC, 
                 0x1E0, 0x1E4, 0x1E6, 0x1E8, 0x1EA, 0x1EC, 0x1EE,
                 0x1F0, 0x1F2, 0x1F4, 0x1F6, 0x1F8, 0x1FA, 0x1FC, 0x1FE,
                 0x200, 0x202, 0x204, 0x206, 0x208, 0x20A, 0x20C,
                 0x210,        0x214, 0x216, 0x218,        0x21C,
                 0x220, 0x224, 0x228, 0x22C, 0x230, 0x234, 0x238, 0x23C,
                 0x240, 0x244, 0x248, 0x24C, 0x250, 0x254, 0x258, 0x25C,
                 0x260,        0x264,        0x268,        0x26C, 0x26E,
                 0x270, 0x272, 0x274, 0x276, 0x278, 0x27A, 0x27C, 0x27E,
                 0x280, 0x282, 0x284, 0x286, 0x288, 0x28A, 0x28C, 0x28E,
                 0x290, 0x292, 0x294,        0x298,        0x29C,
                 0x2A0, 0x2A4, 0x2A8, 0x2AC, 0x2B0, 0x2B4
               ]
    
class VlMxCountryInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pointer(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08)

    def get_shiftjis_string_ptrs(self):
        return [self.unknown_0x04]
        
class VlMxSlgCameraInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_float32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_float32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_float32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_float32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_float32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_float32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_float32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_float32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_float32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_float32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_float32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_float32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_float32(self.unknown_0x40)
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  )
  
    
class VlMxSlgCommandCursorInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_float32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C )
   
    
class VlMxTargetModeGazeFixedInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_float32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_float32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_float32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_float32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_float32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_float32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_float32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_float32(self.unknown_0x30)
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30 )
  
class VlMxPhysicsMaterialInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C )
    
class VlMxSurroundInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)
        
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C )  


class MxParameterPvs(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x08 = 0
        self.unknown_0x10 = 0
        self.unknown_0x18 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int64(self.unknown_0x00)
        self.unknown_0x08 = rw.rw_pad64(self.unknown_0x08)

        rw.assert_is_zero(self.unknown_0x08)

        self.unknown_0x10 = rw.rw_pad64(self.unknown_0x10)
        self.unknown_0x18 = rw.rw_pad64(self.unknown_0x18)

        rw.assert_is_zero(self.unknown_0x10)
        rw.assert_is_zero(self.unknown_0x18)
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x08, 
                 self.unknown_0x10,  self.unknown_0x18, )  
    
    def asset_table_offsets(self):
        return [0x00]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00, ]
    
class SlgEnStrongholdPathNodeParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
        
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0
               ]
    
class SlgEnStrongholdParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x0140 = 0
        self.unknown_0x0148 = 0
        self.unknown_0x014C = 0
        self.unknown_0x0150 = 0
        self.unknown_0x0154 = 0
        self.unknown_0x0158 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
        self.unknown_0x0120 = rw.rw_int64(self.unknown_0x0120)
        self.unknown_0x0128 = rw.rw_int64(self.unknown_0x0128)
        
        self.unknown_0x0130 = rw.rw_int64(self.unknown_0x0130)
        self.unknown_0x0138 = rw.rw_int64(self.unknown_0x0138)
        
        self.unknown_0x0140 = rw.rw_int64(self.unknown_0x0140)
        self.unknown_0x0148 = rw.rw_int32(self.unknown_0x0148)
        self.unknown_0x014C = rw.rw_int32(self.unknown_0x014C)
        
        self.unknown_0x0150 = rw.rw_int32(self.unknown_0x0150)
        self.unknown_0x0154 = rw.rw_int32(self.unknown_0x0154)
        self.unknown_0x0158 = rw.rw_int64(self.unknown_0x0158)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128,
                 self.unknown_0x0130,  self.unknown_0x0138,
                 self.unknown_0x0140,  self.unknown_0x0148,  self.unknown_0x014C,
                 self.unknown_0x0150,  self.unknown_0x0154, self.unknown_0x0158
                 )

    def asset_table_offsets(self):
        return [ 0x70,  0x78,  0x80,  0x88,  0x90,  0x98,  0xa0, 0xa8, 
                0x110, 0x118, 0x120, 0x128, 0x130, 0x138, 0x140       ]
        
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128,
                0x130, 0x138,
                0x140, 0x148, 0x14C,
                0x150, 0x154, 0x158
               ]

class EnWindmillParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x011C = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0124 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x012C = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x013C = 0
        self.unknown_0x0140 = 0
        self.unknown_0x0144 = 0
        self.unknown_0x0148 = 0
        self.unknown_0x014C = 0
        self.unknown_0x0150 = 0
        self.unknown_0x0154 = 0
        self.unknown_0x0158 = 0
        self.unknown_0x015C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int32(self.unknown_0x0118)
        self.unknown_0x011C = rw.rw_int32(self.unknown_0x011C)
        
        
        self.unknown_0x0120 = rw.rw_int32(self.unknown_0x0120)
        self.unknown_0x0124 = rw.rw_int32(self.unknown_0x0124)
        self.unknown_0x0128 = rw.rw_int32(self.unknown_0x0128)
        self.unknown_0x012C = rw.rw_int32(self.unknown_0x012C)
        
        self.unknown_0x0130 = rw.rw_int32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_int32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_int32(self.unknown_0x0138)
        self.unknown_0x013C = rw.rw_int32(self.unknown_0x013C)
        
        self.unknown_0x0140 = rw.rw_int32(self.unknown_0x0140)
        self.unknown_0x0144 = rw.rw_int32(self.unknown_0x0144)
        self.unknown_0x0148 = rw.rw_int32(self.unknown_0x0148)
        self.unknown_0x014C = rw.rw_int32(self.unknown_0x014C)
        
        self.unknown_0x0150 = rw.rw_int32(self.unknown_0x0150)
        self.unknown_0x0154 = rw.rw_int32(self.unknown_0x0154)
        self.unknown_0x0158 = rw.rw_pad32(self.unknown_0x0158)
        self.unknown_0x015C = rw.rw_pad32(self.unknown_0x015C)

        rw.assert_is_zero(self.unknown_0x0158)
        rw.assert_is_zero(self.unknown_0x015C)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118, self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124, self.unknown_0x0128, self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134, self.unknown_0x0138, self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0144, self.unknown_0x0148, self.unknown_0x014C,
                 self.unknown_0x0150,  self.unknown_0x0154, self.unknown_0x0158, self.unknown_0x015C
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118, 0x11C,
                0x120, 0x124, 0x128, 0x12C,
                0x130, 0x134, 0x138, 0x13C,
                0x140, 0x144, 0x148, 0x14C,
                0x150, 0x154]
    
class AISlgUnitMxParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x74 = 0
        self.unknown_0x78 = 0
        self.unknown_0x7C = 0
        self.unknown_0x80 = 0
        self.unknown_0x84 = 0
        self.unknown_0x88 = 0
        self.unknown_0x8C = 0
        self.unknown_0x90 = 0
        self.unknown_0x94 = 0
        self.unknown_0x98 = 0
        self.unknown_0x9C = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA4 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xAC = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB4 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xBC = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC4 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xCC = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD4 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xDC = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE4 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xEC = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF4 = 0
        self.unknown_0xF8 = 0
        self.unknown_0xFC = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0104 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x010C = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x011C = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0124 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)  # Ptr
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)  # Ptr
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_int32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_int32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int32(self.unknown_0x70)
        self.unknown_0x74 = rw.rw_int32(self.unknown_0x74)
        self.unknown_0x78 = rw.rw_int32(self.unknown_0x78)
        self.unknown_0x7C = rw.rw_int32(self.unknown_0x7C)
        
        self.unknown_0x80 = rw.rw_int32(self.unknown_0x80)
        self.unknown_0x84 = rw.rw_int32(self.unknown_0x84)
        self.unknown_0x88 = rw.rw_int32(self.unknown_0x88)
        self.unknown_0x8C = rw.rw_int32(self.unknown_0x8C)
        
        self.unknown_0x90 = rw.rw_int32(self.unknown_0x90)
        self.unknown_0x94 = rw.rw_int32(self.unknown_0x94)
        self.unknown_0x98 = rw.rw_int32(self.unknown_0x98)
        self.unknown_0x9C = rw.rw_int32(self.unknown_0x9C)
        
        self.unknown_0xA0 = rw.rw_int32(self.unknown_0xA0)
        self.unknown_0xA4 = rw.rw_int32(self.unknown_0xA4)
        self.unknown_0xA8 = rw.rw_int32(self.unknown_0xA8)
        self.unknown_0xAC = rw.rw_int32(self.unknown_0xAC)
        
        self.unknown_0xB0 = rw.rw_int32(self.unknown_0xB0)
        self.unknown_0xB4 = rw.rw_int32(self.unknown_0xB4)
        self.unknown_0xB8 = rw.rw_int32(self.unknown_0xB8)
        self.unknown_0xBC = rw.rw_int32(self.unknown_0xBC)
        
        self.unknown_0xC0 = rw.rw_int32(self.unknown_0xC0)
        self.unknown_0xC4 = rw.rw_int32(self.unknown_0xC4)
        self.unknown_0xC8 = rw.rw_int32(self.unknown_0xC8)
        self.unknown_0xCC = rw.rw_int32(self.unknown_0xCC)
        
        self.unknown_0xD0 = rw.rw_int32(self.unknown_0xD0)
        self.unknown_0xD4 = rw.rw_int32(self.unknown_0xD4)
        self.unknown_0xD8 = rw.rw_int32(self.unknown_0xD8)
        self.unknown_0xDC = rw.rw_int32(self.unknown_0xDC)
        
        self.unknown_0xE0 = rw.rw_int32(self.unknown_0xE0)
        self.unknown_0xE4 = rw.rw_int32(self.unknown_0xE4)
        self.unknown_0xE8 = rw.rw_int32(self.unknown_0xE8)
        self.unknown_0xEC = rw.rw_int32(self.unknown_0xEC)
        
        self.unknown_0xF0 = rw.rw_int32(self.unknown_0xF0)
        self.unknown_0xF4 = rw.rw_int32(self.unknown_0xF4)
        self.unknown_0xF8 = rw.rw_int32(self.unknown_0xF8)
        self.unknown_0xFC = rw.rw_int32(self.unknown_0xFC)
        
        self.unknown_0x0100 = rw.rw_int32(self.unknown_0x0100)
        self.unknown_0x0104 = rw.rw_int32(self.unknown_0x0104)
        self.unknown_0x0108 = rw.rw_int32(self.unknown_0x0108)
        self.unknown_0x010C = rw.rw_int32(self.unknown_0x010C)
        
        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_int32(self.unknown_0x0118)
        self.unknown_0x011C = rw.rw_int32(self.unknown_0x011C)
        
        self.unknown_0x0120 = rw.rw_int32(self.unknown_0x0120)
        self.unknown_0x0124 = rw.rw_int32(self.unknown_0x0124)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x74,  self.unknown_0x78,  self.unknown_0x7C, 
                 
                 self.unknown_0x80,  self.unknown_0x84,  self.unknown_0x88,  self.unknown_0x8C, 
                 self.unknown_0x90,  self.unknown_0x94,  self.unknown_0x98,  self.unknown_0x9C, 
                 self.unknown_0xA0,  self.unknown_0xA4,  self.unknown_0xA8,  self.unknown_0xAC, 
                 self.unknown_0xB0,  self.unknown_0xB4,  self.unknown_0xB8,  self.unknown_0xBC,
                 self.unknown_0xC0,  self.unknown_0xC4,  self.unknown_0xC8,  self.unknown_0xCC, 
                 self.unknown_0xD0,  self.unknown_0xD4,  self.unknown_0xD8,  self.unknown_0xDC, 
                 self.unknown_0xE0,  self.unknown_0xE4,  self.unknown_0xE8,  self.unknown_0xEC, 
                 self.unknown_0xF0,  self.unknown_0xF4,  self.unknown_0xF8,  self.unknown_0xFC, 
                 
                 self.unknown_0x0100,  self.unknown_0x0104,  self.unknown_0x0108,  self.unknown_0x010C, 
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C, 
                 self.unknown_0x0120,  self.unknown_0x0124, )
    

    def asset_table_offsets(self):
        return []

    def pof0_offsets(self):
        return [0x00, 0x04]
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  0x70,  0x74,  0x78,  0x7C,
                 0x80,  0x84,  0x88,  0x8C,  0x90,  0x94,  0x98,  0x9C,
                 0xA0,  0xA4,  0xA8,  0xAC,  0xB0,  0xB4,  0xB8,  0xBC,
                 0xC0,  0xC4,  0xC8,  0xCC,  0xD0,  0xD4,  0xD8,  0xDC,
                 0xE0,  0xE4,  0xE8,  0xEC,  0xF0,  0xF4,  0xF8,  0xFC,
                0x100, 0x104, 0x108, 0x10C, 0x110, 0x114, 0x118, 0x11C,
                0x120, 0x124]
    
class SlgEnUnitPlacementPointParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x011C = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0124 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x012C = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x013C = 0
        self.unknown_0x0140 = 0
        self.unknown_0x0144 = 0
        self.unknown_0x0148 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
                
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_int32(self.unknown_0x0118)
        self.unknown_0x011C = rw.rw_int32(self.unknown_0x011C)
        
        self.unknown_0x0120 = rw.rw_int32(self.unknown_0x0120)
        self.unknown_0x0124 = rw.rw_int32(self.unknown_0x0124)
        self.unknown_0x0128 = rw.rw_int32(self.unknown_0x0128)
        self.unknown_0x012C = rw.rw_int32(self.unknown_0x012C)
        
        self.unknown_0x0130 = rw.rw_int32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_int32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_int32(self.unknown_0x0138)
        self.unknown_0x013C = rw.rw_int32(self.unknown_0x013C)
        
        self.unknown_0x0140 = rw.rw_int32(self.unknown_0x0140)
        self.unknown_0x0144 = rw.rw_int32(self.unknown_0x0144)
        self.unknown_0x0148 = rw.rw_int64(self.unknown_0x0148)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100, self.unknown_0x0108,
                 self.unknown_0x0110, self.unknown_0x0114, self.unknown_0x0118, self.unknown_0x011C,
                 self.unknown_0x0120, self.unknown_0x0124, self.unknown_0x0128, self.unknown_0x012C,
                 self.unknown_0x0130, self.unknown_0x0134, self.unknown_0x0138, self.unknown_0x013C,
                 self.unknown_0x0140, self.unknown_0x0144, self.unknown_0x0148
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118, 0x11C,
                0x120, 0x124, 0x128, 0x12C,
                0x130, 0x134, 0x138, 0x13C,
                0x140, 0x144, 0x148
               ]
    
class SlgEnMedicPointParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
        
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0
               ]
    
class SlgEnWarpPointParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x011C = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x013C = 0
        self.unknown_0x0140 = 0
        self.unknown_0x0148 = 0
        self.unknown_0x0150 = 0
        self.unknown_0x0154 = 0
        self.unknown_0x0158 = 0
        self.unknown_0x015C = 0
        self.unknown_0x0160 = 0
        self.unknown_0x0168 = 0
        self.unknown_0x0170 = 0
        self.unknown_0x0174 = 0
        self.unknown_0x0178 = 0
        self.unknown_0x017C = 0
        self.unknown_0x0180 = 0
        self.unknown_0x0188 = 0
        self.unknown_0x0190 = 0
        self.unknown_0x0194 = 0
        self.unknown_0x0198 = 0
        self.unknown_0x019C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
                
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_int32(self.unknown_0x0118)
        self.unknown_0x011C = rw.rw_int32(self.unknown_0x011C)
        
        self.unknown_0x0120 = rw.rw_int64(self.unknown_0x0120)
        self.unknown_0x0128 = rw.rw_pad64(self.unknown_0x0128)
        
        rw.assert_is_zero(self.unknown_0x0128)
        
        self.unknown_0x0130 = rw.rw_int32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_int32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_int32(self.unknown_0x0138)
        self.unknown_0x013C = rw.rw_int32(self.unknown_0x013C)
        
        self.unknown_0x0140 = rw.rw_int64(self.unknown_0x0140)
        self.unknown_0x0148 = rw.rw_pad64(self.unknown_0x0148)
        
        rw.assert_is_zero(self.unknown_0x0148)
        
        self.unknown_0x0150 = rw.rw_int32(self.unknown_0x0150)
        self.unknown_0x0154 = rw.rw_int32(self.unknown_0x0154)
        self.unknown_0x0158 = rw.rw_int32(self.unknown_0x0158)
        self.unknown_0x015C = rw.rw_int32(self.unknown_0x015C)
        
        self.unknown_0x0160 = rw.rw_int64(self.unknown_0x0160)
        self.unknown_0x0168 = rw.rw_pad64(self.unknown_0x0168)
        
        rw.assert_is_zero(self.unknown_0x0168)
        
        self.unknown_0x0170 = rw.rw_int32(self.unknown_0x0170)
        self.unknown_0x0174 = rw.rw_int32(self.unknown_0x0174)
        self.unknown_0x0178 = rw.rw_int32(self.unknown_0x0178)
        self.unknown_0x017C = rw.rw_int32(self.unknown_0x017C)
        
        self.unknown_0x0180 = rw.rw_int64(self.unknown_0x0180)
        self.unknown_0x0188 = rw.rw_pad64(self.unknown_0x0188)
        
        rw.assert_is_zero(self.unknown_0x0188)
        
        self.unknown_0x0190 = rw.rw_int32(self.unknown_0x0190)
        self.unknown_0x0194 = rw.rw_int32(self.unknown_0x0194)
        self.unknown_0x0198 = rw.rw_int32(self.unknown_0x0198)
        self.unknown_0x019C = rw.rw_int32(self.unknown_0x019C)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114, self.unknown_0x0118, self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0128,
                 self.unknown_0x0130,  self.unknown_0x0114, self.unknown_0x0138, self.unknown_0x013C,
                 self.unknown_0x0140,  self.unknown_0x0148,
                 self.unknown_0x0150,  self.unknown_0x0154, self.unknown_0x0158, self.unknown_0x015C,
                 self.unknown_0x0160,  self.unknown_0x0168,
                 self.unknown_0x0170,  self.unknown_0x0174, self.unknown_0x0178, self.unknown_0x017C,
                 self.unknown_0x0180,  self.unknown_0x0188,
                 self.unknown_0x0190,  self.unknown_0x0194, self.unknown_0x0198, self.unknown_0x019C
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
        
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118, 0x11C,
                0x120,
                0x130, 0x134, 0x138, 0x13C,
                0x140,
                0x150, 0x154, 0x158, 0x15C,
                0x160, 
                0x170, 0x174, 0x178, 0x17C,
                0x180,
                0x190, 0x194, 0x198, 0x19C
               ]
    
class SlgEnExplosiveParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        
        
    def get_data(self):
        return ( self.unknown_0x00, )
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00 ]
    
class SlgEnTriggerBaseParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x013C = 0
        self.unknown_0x0140 = 0
        self.unknown_0x0144 = 0
        self.unknown_0x0148 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
                
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)

        rw.assert_is_zero(self.unknown_0xF8)

        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)

        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)

        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
        self.unknown_0x0120 = rw.rw_int64(self.unknown_0x0120)
        self.unknown_0x0128 = rw.rw_int64(self.unknown_0x0128)
        
        self.unknown_0x0130 = rw.rw_int32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_int32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_int32(self.unknown_0x0138)
        self.unknown_0x013C = rw.rw_int32(self.unknown_0x013C)
        
        self.unknown_0x0140 = rw.rw_int32(self.unknown_0x0140)
        self.unknown_0x0144 = rw.rw_int32(self.unknown_0x0144)
        self.unknown_0x0148 = rw.rw_int64(self.unknown_0x0148)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100, self.unknown_0x0108,
                 self.unknown_0x0110, self.unknown_0x0118,
                 self.unknown_0x0120, self.unknown_0x0128,
                 self.unknown_0x0130, self.unknown_0x0134, self.unknown_0x0138, self.unknown_0x013C,
                 self.unknown_0x0140, self.unknown_0x0144, self.unknown_0x0148
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x118, 0x120, 0x128]
          
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128,
                0x130, 0x134, 0x138, 0x13C,
                0x140, 0x144, 0x148
               ]
    
class SlgEnMineParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x10 = 0
        self.unknown_0x18 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_pad32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int64(self.unknown_0x08)
        
        rw.assert_is_zero(self.unknown_0x04)
        
        self.unknown_0x10 = rw.rw_int64(self.unknown_0x10)
        self.unknown_0x18 = rw.rw_int64(self.unknown_0x18)
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x08, 
                 self.unknown_0x10,  self.unknown_0x18 )
    
    def asset_table_offsets(self):
        return [0x08, 0x10]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x08,  0x10,  0x18
               ]

class SlgEnAreaSurveillancePathNodeParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0]
    

class SlgEnAreaSurveillanceParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_pad64(self.unknown_0x0118)
        
        rw.assert_is_zero(self.unknown_0x0118)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110]
    
class EnMovePathNodeParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)  # Padding
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)  # Padding
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)  # Padding
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)  # Padding
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)  # Padding
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)  # Padding
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)  # Padding
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100, self.unknown_0x0108,
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0
               ]
    
class EnMovePathParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)  # Padding
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)  # Padding
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)  # Padding
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)  # Padding
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)  # Padding
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)  # Padding
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8) # Padding

        rw.assert_is_zero(self.unknown_0xF8)

        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)  # Padding
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)  # Padding

        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)

        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114, self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118
               ]
    
    
class SlgEnReinforcePointParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x011C = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0138 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_int32(self.unknown_0x0118)
        self.unknown_0x011C = rw.rw_int32(self.unknown_0x011C)
        
        self.unknown_0x0120 = rw.rw_int64(self.unknown_0x0120)
        self.unknown_0x0128 = rw.rw_int64(self.unknown_0x0128)
        
        self.unknown_0x0130 = rw.rw_int64(self.unknown_0x0130)
        self.unknown_0x0138 = rw.rw_pad64(self.unknown_0x0138)
        
        rw.assert_is_zero(self.unknown_0x0138)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114, self.unknown_0x0118, self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0128,
                 self.unknown_0x0130,  self.unknown_0x0138
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118, 0x11C,
                0x120, 0x124, 0x128, 0x12C,
                0x130
               ]

class SlgEnGregoalStayPointParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_pad64(self.unknown_0x0118)
        
        rw.assert_is_zero(self.unknown_0x0118)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110
              ]
      
class SlgEnGregoalParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x0140 = 0
        self.unknown_0x0148 = 0
        self.unknown_0x0150 = 0
        self.unknown_0x0158 = 0
        self.unknown_0x0160 = 0
        self.unknown_0x0168 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
        self.unknown_0x0120 = rw.rw_int64(self.unknown_0x0120)
        self.unknown_0x0128 = rw.rw_int64(self.unknown_0x0128)
        
        self.unknown_0x0130 = rw.rw_int64(self.unknown_0x0130)
        self.unknown_0x0138 = rw.rw_int64(self.unknown_0x0138)
        
        self.unknown_0x0140 = rw.rw_int64(self.unknown_0x0140)
        self.unknown_0x0148 = rw.rw_int64(self.unknown_0x0148)
        
        self.unknown_0x0150 = rw.rw_int64(self.unknown_0x0150)
        self.unknown_0x0158 = rw.rw_int64(self.unknown_0x0158)
        
        self.unknown_0x0160 = rw.rw_int64(self.unknown_0x0160)
        self.unknown_0x0168 = rw.rw_pad64(self.unknown_0x0168)
        
        rw.assert_is_zero(self.unknown_0x0168)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128,
                 self.unknown_0x0130,  self.unknown_0x0138,
                 self.unknown_0x0140,  self.unknown_0x0148,
                 self.unknown_0x0150,  self.unknown_0x0158,
                 self.unknown_0x0160,  self.unknown_0x0168
                 )

    def asset_table_offsets(self):
        return [              0x70,   0x78,  0x80,  0x88,  0x90,  0x98,  0xa0,  0xa8,
                0x110, 0x118, 0x120, 0x128, 0x130, 0x138, 0x140, 0x148, 0x150, 0x158 ]

    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128,
                0x130, 0x138,
                0x140, 0x148,
                0x150, 0x158,
                0x160
              ]

class SlgEnDummyTankParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        
        
    def get_data(self):
        return ( self.unknown_0x00, )
    
    def asset_table_offsets(self):
        return []
        
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00 ]

class SlgEnBreakableBridgeParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        
        
    def get_data(self):
        return ( self.unknown_0x00, )
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00 ]
    

class SlgEnControlLancePieceParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C)
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C ]

class SlgEnDefenseWallParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x02 = 0
        self.unknown_0x04 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int16(self.unknown_0x00)
        self.unknown_0x02 = rw.rw_int16(self.unknown_0x02)
        self.unknown_0x04 = rw.rw_int16(self.unknown_0x04)
        
        
    def get_data(self):
        return ( self.unknown_0x00, self.unknown_0x04,)
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x02, 0x04, ]
    
class SlgEnTemplePartsParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x10 = 0
        self.unknown_0x18 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int64(self.unknown_0x08)
        
        self.unknown_0x10 = rw.rw_int64(self.unknown_0x10)
        self.unknown_0x18 = rw.rw_int64(self.unknown_0x18)
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08, 
                 self.unknown_0x10,  self.unknown_0x18, )
    
    def asset_table_offsets(self):
        return [0x08, 0x10, 0x18]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x10,  0x18 ]
    

class SlgEnLancePieceParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C )
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C ]
    
class SlgEnTowerParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08 )
    
    def asset_table_offsets(self):
        return []
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08 ]
    
      
class VlMxUnitResourceInfo(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x18 = 0
        self.unknown_0x20 = 0
        self.unknown_0x28 = 0
        self.unknown_0x30 = 0
        self.unknown_0x38 = 0
        self.unknown_0x40 = 0
        self.unknown_0x48 = 0
        self.unknown_0x50 = 0
        self.unknown_0x58 = 0
        self.unknown_0x60 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int64(self.unknown_0x10)
        self.unknown_0x18 = rw.rw_int64(self.unknown_0x18)
        
        self.unknown_0x20 = rw.rw_int64(self.unknown_0x20)
        self.unknown_0x28 = rw.rw_int64(self.unknown_0x28)
        
        self.unknown_0x30 = rw.rw_int64(self.unknown_0x30)
        self.unknown_0x38 = rw.rw_int64(self.unknown_0x38)
        
        self.unknown_0x40 = rw.rw_int64(self.unknown_0x40)
        self.unknown_0x48 = rw.rw_int64(self.unknown_0x48)
        
        self.unknown_0x50 = rw.rw_int64(self.unknown_0x50)
        self.unknown_0x58 = rw.rw_int64(self.unknown_0x58)
        
        self.unknown_0x60 = rw.rw_int64(self.unknown_0x60)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x18, 
                 self.unknown_0x20,  self.unknown_0x28, 
                 self.unknown_0x30,  self.unknown_0x38, 
                 self.unknown_0x40,  self.unknown_0x48, 
                 self.unknown_0x50,  self.unknown_0x58, 
                 self.unknown_0x60,)
    
    def asset_table_offsets(self):
        return [0x10, 0x18, 0x20, 0x28, 0x30, 0x38, 0x40, 0x48, 0x50, 0x58, 0x60]

    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [  0x00,  0x04,  0x08,  0x0C,  0x10,  0x18,
                  0x20,  0x28,  0x30,  0x38,  0x40,  0x48,  0x50,  0x58, 
                  0x60
               ]

class EnSimpleWallParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)  # Padding
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)  # Padding
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)  # Padding
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)  # Padding
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)  # Padding
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)  # Padding
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)  # Padding

        rw.assert_is_zero(self.unknown_0xF8)

        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)  # Padding
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)  # Padding

        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)

        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_pad64(self.unknown_0x0118)  # Padding

        rw.assert_is_zero(self.unknown_0x0118)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,
                0x110,
               ]

class SlgEnProduceBorderParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
               ]
    
class SlgEnProduceGndParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)

        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114, self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x118]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118
               ]
    
class SlgEnBreakableGateParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        
        
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04 )
    
    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04 ]

      
class SlgEnChainBreakdownParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x012C = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)

        rw.assert_is_zero(self.unknown_0xF8)

        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)

        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)

        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
        self.unknown_0x0120 = rw.rw_int64(self.unknown_0x0120)
        self.unknown_0x0128 = rw.rw_int32(self.unknown_0x0128)
        self.unknown_0x012C = rw.rw_int32(self.unknown_0x012C)
        
        self.unknown_0x0130 = rw.rw_int32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_int32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_int64(self.unknown_0x0138)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128, self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134, self.unknown_0x0138
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118, 0x120]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128, 0x12C,
                0x130, 0x134, 0x138]
      
      
class SlgEnSlayingAreaParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_int32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_int32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_pad32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_pad32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_pad32(self.unknown_0x4C)
        
        rw.assert_is_zero(self.unknown_0x44)
        rw.assert_is_zero(self.unknown_0x48)
        rw.assert_is_zero(self.unknown_0x4C)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
               )
    
    def asset_table_offsets(self):
        return []
          
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40,  
               ]
    
class SlgEnSurroundPathNodeParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
                
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
        
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0
               ]
    
class SlgEnOrderAllAttackPointParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)

        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0
               ]
    
class SlgEnSurroundParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x011C = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0124 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x012C = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_int32(self.unknown_0x0118)
        self.unknown_0x011C = rw.rw_int32(self.unknown_0x011C)
        
        self.unknown_0x0120 = rw.rw_int32(self.unknown_0x0120)
        self.unknown_0x0124 = rw.rw_int32(self.unknown_0x0124)
        self.unknown_0x0128 = rw.rw_int32(self.unknown_0x0128)
        self.unknown_0x012C = rw.rw_int32(self.unknown_0x012C)
        
        self.unknown_0x0130 = rw.rw_int32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_int32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_int64(self.unknown_0x0138)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128,
                 self.unknown_0x0130,  self.unknown_0x0138
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
        
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118, 0x11C,
                0x120, 0x124, 0x128, 0x12C,
                0x130, 0x134, 0x138
               ]
    
class SlgEnTriggerEnterParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_int32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_int32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_pad32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_pad32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_pad32(self.unknown_0x5C)
        
        rw.assert_is_zero(self.unknown_0x54)
        rw.assert_is_zero(self.unknown_0x58)
        rw.assert_is_zero(self.unknown_0x5C)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C,)
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40,  0x44,  0x48,  0x4C,  0x50
               ]
    
class SlgEnAlterOperationMapParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x08 = 0
        self.unknown_0x10 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int64(self.unknown_0x00)
        self.unknown_0x08 = rw.rw_int64(self.unknown_0x08)
        
        self.unknown_0x10 = rw.rw_int64(self.unknown_0x10)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x08, 
                 self.unknown_0x10,  self.unknown_0x18, self.unknown_0x1C,
                 self.unknown_0x20,  self.unknown_0x24, )
    
    def asset_table_offsets(self):
        return [0x00, 0x08, 0x10]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24
               ]
    
class SlgEnSandstormParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        
    
    def get_data(self):
        return ( self.unknown_0x00, )
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00 ]

class SlgEnTerrainParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
                
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)

        rw.assert_is_zero(self.unknown_0xF8)

        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)

        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)

        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118
               ]
    
class StaticSphere(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_float32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_pad32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_pad32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_pad32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_float32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_pad32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x14)
        rw.assert_is_zero(self.unknown_0x18)
        rw.assert_is_zero(self.unknown_0x1C)
        
        rw.assert_is_zero(self.unknown_0x24)
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, ) 

    def asset_table_offsets(self):
        return []

    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [0x00, 0x04, 0x08, 0x0C, 0x10, 0x20]
    
class SlgEnSearchLightPathNodeParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_pad64(self.unknown_0x0118)
        
        rw.assert_is_zero(self.unknown_0x0118)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78, 
                 
                 self.unknown_0x80,  self.unknown_0x88, 
                 self.unknown_0x90,  self.unknown_0x98, 
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8, 
                 self.unknown_0xD0,  self.unknown_0xD8, 
                 self.unknown_0xE0,  self.unknown_0xE8, 
                 self.unknown_0xF0,  self.unknown_0xF8, 
                 
                 self.unknown_0x0100,  self.unknown_0x0108, 
                 self.unknown_0x0110,  self.unknown_0x0118, 
                 )
    
    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
      
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110
               ]
    
class SlgEnLongRangeHEProposedImpactParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)

        rw.assert_is_zero(self.unknown_0xF8)

        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)

        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)

        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_pad64(self.unknown_0x0118)

        rw.assert_is_zero(self.unknown_0x0118)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110,
               ]

class SlgEnSearchLightJointParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, ) 

    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C ]


class SlgEnTriggerHerbParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_uint32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_uint32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_uint32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_float32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_float32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_float32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_float32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_pad32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_pad32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_pad32(self.unknown_0x4C)

        rw.assert_is_zero(self.unknown_0x44)
        rw.assert_is_zero(self.unknown_0x48)
        rw.assert_is_zero(self.unknown_0x4C)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, ) 
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40
               ]

    
class SlgEnSearchLightParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x011C = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0124 = 0
        self.unknown_0x0128 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_int32(self.unknown_0x0118)
        self.unknown_0x011C = rw.rw_int32(self.unknown_0x011C)
        
        self.unknown_0x0120 = rw.rw_int32(self.unknown_0x0120)
        self.unknown_0x0124 = rw.rw_int32(self.unknown_0x0124)
        self.unknown_0x0128 = rw.rw_pad64(self.unknown_0x0128)

        rw.assert_is_zero(self.unknown_0x0128)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,  self.unknown_0x011C,
                 self.unknown_0x0120,  self.unknown_0x0124,  self.unknown_0x0128,
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118, 0x11C,
                0x120, 0x124
               ]

class SlgEnCentralLorryParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04, ) 
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04 ]

    
class SlgEnLorryParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x012C = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x013C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)

        rw.assert_is_zero(self.unknown_0xF8)

        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)

        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)

        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
        self.unknown_0x0120 = rw.rw_int64(self.unknown_0x0120)
        self.unknown_0x0128 = rw.rw_int32(self.unknown_0x0128)
        self.unknown_0x012C = rw.rw_int32(self.unknown_0x012C)
        
        self.unknown_0x0130 = rw.rw_int32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_int32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_int32(self.unknown_0x0138)
        self.unknown_0x013C = rw.rw_int32(self.unknown_0x013C)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128, self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134, self.unknown_0x0138, self.unknown_0x013C
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118, 0x120]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128, 0x12C,
                0x130, 0x134, 0x138, 0x13C
               ]

class SlgEnLiftJointParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04, )
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04 ]
    
class SlgEnLiftSwitchParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_uint32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_uint32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_uint32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_float32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_float32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_float32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_float32(self.unknown_0x3C)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, ) 

    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C
               ]
    
class SlgEnSteepleBarrierParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118
               ]
    
class SlgEnLiftParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x011C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_int32(self.unknown_0x0118)
        self.unknown_0x011C = rw.rw_int32(self.unknown_0x011C)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114, self.unknown_0x0118, self.unknown_0x011C
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]

    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118, 0x11C
               ]

class SlgEnBunkerCannonParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0128 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
        self.unknown_0x0120 = rw.rw_int64(self.unknown_0x0120)
        self.unknown_0x0128 = rw.rw_int64(self.unknown_0x0128)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118, 0x120]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128
               ]
    
class SlgEnReplaceModelParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0128 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
        self.unknown_0x0120 = rw.rw_int64(self.unknown_0x0120)
        self.unknown_0x0128 = rw.rw_pad64(self.unknown_0x0128)
        
        rw.assert_is_zero(self.unknown_0x0128)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120
               ]

class SlgEnRailWaySwitchParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_float32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_float32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_float32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_float32(self.unknown_0x3C)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, ) 
    
    def asset_table_offsets(self):
        return []    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C
               ]
    
class SlgEnSwitchDoorParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int64(self.unknown_0x00)
        self.unknown_0x08 = rw.rw_pad32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_pad32(self.unknown_0x0C)
        
        rw.assert_is_zero(self.unknown_0x08)
        rw.assert_is_zero(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_uint32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_uint32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_uint32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_float32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_float32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_float32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_float32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_float32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_float32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_pad32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_pad32(self.unknown_0x5C)
        
        rw.assert_is_zero(self.unknown_0x58)
        rw.assert_is_zero(self.unknown_0x5C)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C,
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, )
    
    def asset_table_offsets(self):
        return [0x00]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,
               ]

class SlgEnMarmot1stPathParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_pad64(self.unknown_0x0118)
        
        rw.assert_is_zero(self.unknown_0x0118)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110
               ]
    
class SlgEnMarmot1stStopNodeParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  )  
    
    def asset_table_offsets(self):
        return []
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
               ]
    
class SlgEnCliffExplosiveParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
    
    def get_data(self):
        return ( self.unknown_0x00, )
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00 ]

class SlgEnMarmot1stParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x012C = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
        self.unknown_0x0120 = rw.rw_int64(self.unknown_0x0120)
        self.unknown_0x0128 = rw.rw_int32(self.unknown_0x0128)
        self.unknown_0x012C = rw.rw_int32(self.unknown_0x012C)
        
        self.unknown_0x0130 = rw.rw_int32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_int32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_pad64(self.unknown_0x0138)

        rw.assert_is_zero(self.unknown_0x0138)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128,  self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0134,  self.unknown_0x0138
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118, 0x120]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128, 0x12C,
                0x130, 0x134
               ]
    

class SlgEnCatwalkParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x012C = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x0140 = 0
        self.unknown_0x0148 = 0
        self.unknown_0x014C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int64(self.unknown_0x0110)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
        self.unknown_0x0120 = rw.rw_int64(self.unknown_0x0120)
        self.unknown_0x0128 = rw.rw_int32(self.unknown_0x0128)
        self.unknown_0x012C = rw.rw_int32(self.unknown_0x012C)
        
        self.unknown_0x0130 = rw.rw_int64(self.unknown_0x0130)
        self.unknown_0x0138 = rw.rw_int64(self.unknown_0x0138)
        
        self.unknown_0x0140 = rw.rw_int64(self.unknown_0x0140)
        self.unknown_0x0148 = rw.rw_int32(self.unknown_0x0148)
        self.unknown_0x014C = rw.rw_int32(self.unknown_0x014C)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128, self.unknown_0x012C,
                 self.unknown_0x0130,  self.unknown_0x0138,
                 self.unknown_0x0140,  self.unknown_0x0148, self.unknown_0x014C,
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x110, 0x118, 0x120, 0x138, 0x140]
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x118,
                0x120, 0x128, 0x12C,
                0x130, 0x138,
                0x140, 0x148, 0x14C]

class SlgEnCatwalkHoleParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_int32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_int32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_int32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_int32(self.unknown_0x3C)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C,  
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C,  )   
    
    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,  0x28,  0x2C,  0x30,  0x34,  0x38,  0x3C,
               ]

class SlgEnPropellerParam(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0
        self.unknown_0x50 = 0
        self.unknown_0x54 = 0
        self.unknown_0x58 = 0
        self.unknown_0x5C = 0
        self.unknown_0x60 = 0
        self.unknown_0x64 = 0
        self.unknown_0x68 = 0
        self.unknown_0x6C = 0
        self.unknown_0x70 = 0
        self.unknown_0x78 = 0
        self.unknown_0x80 = 0
        self.unknown_0x88 = 0
        self.unknown_0x90 = 0
        self.unknown_0x98 = 0
        self.unknown_0xA0 = 0
        self.unknown_0xA8 = 0
        self.unknown_0xB0 = 0
        self.unknown_0xB8 = 0
        self.unknown_0xC0 = 0
        self.unknown_0xC8 = 0
        self.unknown_0xD0 = 0
        self.unknown_0xD8 = 0
        self.unknown_0xE0 = 0
        self.unknown_0xE8 = 0
        self.unknown_0xF0 = 0
        self.unknown_0xF8 = 0
        self.unknown_0x0100 = 0
        self.unknown_0x0108 = 0
        self.unknown_0x0110 = 0
        self.unknown_0x0114 = 0
        self.unknown_0x0118 = 0
        self.unknown_0x0120 = 0
        self.unknown_0x0128 = 0
        self.unknown_0x0130 = 0
        self.unknown_0x0134 = 0
        self.unknown_0x0138 = 0
        self.unknown_0x013C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_int32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_int32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_int32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_int32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_int32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pad32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pad32(self.unknown_0x2C)
        
        rw.assert_is_zero(self.unknown_0x28)
        rw.assert_is_zero(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_pad32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_pad32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_pad32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_pad32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.unknown_0x30)
        rw.assert_is_zero(self.unknown_0x34)
        rw.assert_is_zero(self.unknown_0x38)
        rw.assert_is_zero(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_int32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_int32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_int32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_int32(self.unknown_0x4C)
        
        self.unknown_0x50 = rw.rw_int32(self.unknown_0x50)
        self.unknown_0x54 = rw.rw_int32(self.unknown_0x54)
        self.unknown_0x58 = rw.rw_int32(self.unknown_0x58)
        self.unknown_0x5C = rw.rw_int32(self.unknown_0x5C)
        
        self.unknown_0x60 = rw.rw_int32(self.unknown_0x60)
        self.unknown_0x64 = rw.rw_int32(self.unknown_0x64)
        self.unknown_0x68 = rw.rw_int32(self.unknown_0x68)
        self.unknown_0x6C = rw.rw_int32(self.unknown_0x6C)
        
        self.unknown_0x70 = rw.rw_int64(self.unknown_0x70)
        self.unknown_0x78 = rw.rw_int64(self.unknown_0x78)
        
        self.unknown_0x80 = rw.rw_int64(self.unknown_0x80)
        self.unknown_0x88 = rw.rw_int64(self.unknown_0x88)
        
        self.unknown_0x90 = rw.rw_int64(self.unknown_0x90)
        self.unknown_0x98 = rw.rw_int64(self.unknown_0x98)
        
        self.unknown_0xA0 = rw.rw_int64(self.unknown_0xA0)
        self.unknown_0xA8 = rw.rw_int64(self.unknown_0xA8)
        
        self.unknown_0xB0 = rw.rw_int64(self.unknown_0xB0)
        self.unknown_0xB8 = rw.rw_int64(self.unknown_0xB8)
        
        self.unknown_0xC0 = rw.rw_int64(self.unknown_0xC0)
        self.unknown_0xC8 = rw.rw_int64(self.unknown_0xC8)
        
        self.unknown_0xD0 = rw.rw_int64(self.unknown_0xD0)
        self.unknown_0xD8 = rw.rw_int64(self.unknown_0xD8)
        
        self.unknown_0xE0 = rw.rw_int64(self.unknown_0xE0)
        self.unknown_0xE8 = rw.rw_int64(self.unknown_0xE8)
        
        self.unknown_0xF0 = rw.rw_int64(self.unknown_0xF0)
        self.unknown_0xF8 = rw.rw_pad64(self.unknown_0xF8)
        
        rw.assert_is_zero(self.unknown_0xF8)
        
        self.unknown_0x0100 = rw.rw_pad64(self.unknown_0x0100)
        self.unknown_0x0108 = rw.rw_pad64(self.unknown_0x0108)
        
        rw.assert_is_zero(self.unknown_0x0100)
        rw.assert_is_zero(self.unknown_0x0108)
        
        self.unknown_0x0110 = rw.rw_int32(self.unknown_0x0110)
        self.unknown_0x0114 = rw.rw_int32(self.unknown_0x0114)
        self.unknown_0x0118 = rw.rw_int64(self.unknown_0x0118)
        
        self.unknown_0x0120 = rw.rw_int64(self.unknown_0x0120)
        self.unknown_0x0128 = rw.rw_int64(self.unknown_0x0128)
        
        self.unknown_0x0130 = rw.rw_int32(self.unknown_0x0130)
        self.unknown_0x0134 = rw.rw_int32(self.unknown_0x0134)
        self.unknown_0x0138 = rw.rw_int32(self.unknown_0x0138)
        self.unknown_0x013C = rw.rw_int32(self.unknown_0x013C)
        
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C, 
                 self.unknown_0x50,  self.unknown_0x54,  self.unknown_0x58,  self.unknown_0x5C, 
                 self.unknown_0x60,  self.unknown_0x64,  self.unknown_0x68,  self.unknown_0x6C, 
                 self.unknown_0x70,  self.unknown_0x78,
                 
                 self.unknown_0x80,  self.unknown_0x88,
                 self.unknown_0x90,  self.unknown_0x98,
                 self.unknown_0xA0,  self.unknown_0xA8, 
                 self.unknown_0xB0,  self.unknown_0xB8,
                 self.unknown_0xC0,  self.unknown_0xC8,
                 self.unknown_0xD0,  self.unknown_0xD8,
                 self.unknown_0xE0,  self.unknown_0xE8,
                 self.unknown_0xF0,  self.unknown_0xF8,
                 
                 self.unknown_0x0100,  self.unknown_0x0108,
                 self.unknown_0x0110,  self.unknown_0x0114,  self.unknown_0x0118,
                 self.unknown_0x0120,  self.unknown_0x0128,
                 self.unknown_0x0130,  self.unknown_0x0130, self.unknown_0x0138, self.unknown_0x013C
                 )

    def asset_table_offsets(self):
        return [0x70, 0x78, 0x80, 0x88, 0x90, 0x98, 0xa0, 0xa8, 0x120, 0x128]
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ 0x00,  0x04,  0x08,  0x0C,  0x10,  0x14,  0x18,  0x1C,
                 0x20,  0x24,
                 0x40,  0x44,  0x48,  0x4C,  0x50,  0x54,  0x58,  0x5C,
                 0x60,  0x64,  0x68,  0x6C,  
                 0x70,  0x78,
                 0x80,  0x88,  0x90,  0x98,
                 0xA0,  0xA8,  0xB0,  0xB8,
                 0xC0,  0xC8,  0xD0,  0xD8,
                 0xE0,  0xE8,  0xF0,  
                0x110, 0x114, 0x118,
                0x120, 0x128,
                0x130, 0x134, 0x138, 0x13C
               ]
    
class StaticPyramid(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = 0
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.unknown_0x0C = 0
        self.unknown_0x10 = 0
        self.unknown_0x14 = 0
        self.unknown_0x18 = 0
        self.unknown_0x1C = 0
        self.unknown_0x20 = 0
        self.unknown_0x24 = 0
        self.unknown_0x28 = 0
        self.unknown_0x2C = 0
        self.unknown_0x30 = 0
        self.unknown_0x34 = 0
        self.unknown_0x38 = 0
        self.unknown_0x3C = 0
        self.unknown_0x40 = 0
        self.unknown_0x44 = 0
        self.unknown_0x48 = 0
        self.unknown_0x4C = 0

    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_float32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_float32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_float32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_float32(self.unknown_0x1C)
        
        self.unknown_0x20 = rw.rw_float32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_float32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_float32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_uint32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_float32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_float32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_float32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_uint32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_float32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_pad32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_pad32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_pad32(self.unknown_0x4C)
    
        rw.assert_is_zero(self.unknown_0x44)
        rw.assert_is_zero(self.unknown_0x48)
        rw.assert_is_zero(self.unknown_0x4C)
    
    def get_data(self):
        return ( self.unknown_0x00,  self.unknown_0x04,  self.unknown_0x08,  self.unknown_0x0C, 
                 self.unknown_0x10,  self.unknown_0x14,  self.unknown_0x18,  self.unknown_0x1C, 
                 self.unknown_0x20,  self.unknown_0x24,  self.unknown_0x28,  self.unknown_0x2C, 
                 self.unknown_0x30,  self.unknown_0x34,  self.unknown_0x38,  self.unknown_0x3C, 
                 self.unknown_0x40,  self.unknown_0x44,  self.unknown_0x48,  self.unknown_0x4C ) 

    def asset_table_offsets(self):
        return []

    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [0x00, 0x04, 0x08, 0x0C, 0x10, 0x14, 0x18, 0x1C,
                0x20, 0x24, 0x28, 0x2C, 0x30, 0x34, 0x38, 0x3C,
                0x40]
    
class void(Serializable):
    def __init__(self, context):
        super().__init__(context)

    def read_write(self, rw):
        pass
    
    def get_data(self):
        return []
    
    def asset_table_offsets(self):
        return []

    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ ]
    
class SlgEnGlowFlyParam(Serializable):
    def __init__(self, context):
        super().__init__(context)

    def read_write(self, rw):
        pass
    
    def get_data(self):
        []

    def asset_table_offsets(self):
        return []
    
    
    def pof0_offsets(self):
        return []
    
    def enrs_offsets(self):
        return [ ]

# TYPES ARE ALPHABETICALLY ORDERED
data_types = {clas.__name__: clas for clas in
              [
                 AISlgUnitMxParam,
                 EnCEffectParam,
                 EnConvexParam,
                 EnEventDecorParam,
                 EnHeightMapParam,
                 EnMovePathParam,
                 EnMovePathNodeParam,
                 EnSimpleWallParam,
                 EnSkyParam,
                 EnTalkEventMapParam,
                 EnTalkEventObjParam,
                 EnTreeParam,
                 EnUvScrollParam,
                 EnWaterSurfaceParam,
                 EnWindmillParam,
                 HyColor,
                 MxParameterFog,
                 MxParameterLight,
                 MxParameterStaticLight,
                 MxParameterTextureMerge,
                 MxParameterMergeFile,
                 MxParameterPvs,
                 SlgEnAlterOperationMapParam,
                 SlgEnAreaSurveillanceParam,
                 SlgEnAreaSurveillancePathNodeParam,
                 SlgEnBreakableBridgeParam,
                 SlgEnBreakableGateParam,
                 SlgEnBreakableStructureParam,
                 SlgEnBunkerCannonParam,
                 SlgEnCatwalkParam,
                 SlgEnCatwalkHoleParam,
                 SlgEnCentralLorryParam,
                 SlgEnChainBreakdownParam,
                 SlgEnCliffExplosiveParam,
                 SlgEnControlLancePieceParam,
                 SlgEnDefenseWallParam,
                 SlgEnDummyTankParam,
                 SlgEnExplosiveParam,
                 SlgEnGlowFlyParam,
                 SlgEnGrassParam,
                 SlgEnGrassPathNodeParam,
                 SlgEnGregoalParam,
                 SlgEnGregoalStayPointParam,
                 SlgEnLancePieceParam,
                 SlgEnLiftJointParam,
                 SlgEnLiftParam,
                 SlgEnLiftSwitchParam,
                 SlgEnLongRangeHEProposedImpactParam,
                 SlgEnLorryParam,
                 SlgEnMarmot1stParam,
                 SlgEnMarmot1stPathParam,
                 SlgEnMarmot1stStopNodeParam,
                 SlgEnMedicPointParam,
                 SlgEnMineParam,
                 SlgEnOrderAllAttackPointParam,
                 SlgEnProduceBorderParam,
                 SlgEnProduceGndParam,
                 SlgEnPropellerParam,
                 SlgEnRailWaySwitchParam,
                 SlgEnReinforcePointParam,
                 SlgEnReplaceModelParam,
                 SlgEnSandstormParam,
                 SlgEnSearchLightJointParam,
                 SlgEnSearchLightParam,
                 SlgEnSearchLightPathNodeParam,
                 SlgEnSlayingAreaParam,
                 SlgEnSteepleBarrierParam,
                 SlgEnStrongholdParam,
                 SlgEnStrongholdPathNodeParam,
                 SlgEnSurroundParam,
                 SlgEnSurroundPathNodeParam,
                 SlgEnSwitchDoorParam,
                 SlgEnTemplePartsParam,
                 SlgEnTerrainParam,
                 SlgEnTriggerBaseParam,
                 SlgEnTriggerEnterParam,
                 SlgEnTriggerHerbParam,
                 SlgEnTowerParam,
                 SlgEnTriggerBaseParam,
                 SlgEnUnitPlacementPointParam,
                 SlgEnWarpPointParam,
                 SlgMapObjectParam,
                 StaticBox,
                 StaticPyramid,
                 StaticSphere,
                 void,
                 VlMapObjectParam,
                 VlMxBookDecorationInfo,
                 VlMxBookHistoryInfo,
                 VlMxBookPersonInfo,
                 VlMxBookSoundInfo,
                 VlMxBookWeaponInfo,
                 VlMxCanvasShaderParam,
                 VlMxDrawModelLodParam,
                 VlMxFogParam,
                 VlMxShaderParamSetId,
                 VlMxStandardLightParam,
                 VlMxAddEsdInfo,
                 VlMxBriefingInfo,
                 VlMxCharacterAffinityInfo,
                 VlMxCharacterCommonInfo,
                 VlMxCharacterEachInfo,
                 VlMxCharacterInfo,
                 VlMxClothesInfo,
                 VlMxCountryInfo,
                 VlMxExplosiveInfo,
                 VlMxFieldInfo,
                 VlMxForceInfo,
                 VlMxGalliaRareWeaponCandidateInfo,
                 VlMxGeneralCharInfo,
                 VlMxGeneralCharParamSetInfo,
                 VlMxJobInfo,
                 VlMxMapObjectCommonInfo,
                 VlMxMapObjectInfo,
                 VlMxNewsPaperInfo,
                 VlMxOrderDirectionInfo,
                 VlMxOrderInfo,
                 VlMxParameterConvertTable,
                 VlMxPhysicsMaterialInfo,
                 VlMxPotentialInfo,
                 VlMxResultInfo,
                 VlMxSlgCameraInfo,
                 VlMxSlgCommandCursorInfo,
                 VlMxSlgInfo,
                 VlMxSlgLandformInfo,
                 VlMxSlgStrongholdCommonInfo,
                 VlMxStageInfo,
                 VlMxSurroundInfo,
                 VlMxTargetModeGazeFixedInfo,
                 VlMxUnitCommonInfo,
                 VlMxUnitGrowthTypeInfo,
                 VlMxVehicleCommonInfo,
                 VlMxVehicleDevChangeParamInfo,
                 VlMxVehicleDevInfo,
                 VlMxVehicleEachInfo,
                 VlMxVehicleInfo,
                 VlMxWeaponBringOnUnwholesomeInfo,
                 VlMxWeaponCommonInfo,
                 VlMxWeaponInfo,
                 VlMxUnitResourceInfo
              ]}

data_types["+StaticBox"] = StaticBox
data_types["+StaticPyramid"] = StaticPyramid
data_types["+StaticSphere"] = StaticSphere
