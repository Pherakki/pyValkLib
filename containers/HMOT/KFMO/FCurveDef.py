from pyValkLib.serialisation.Serializable import Serializable

class FCurveDef(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = 1
        self.type = None
        self.divisor = None
        self.unknown_0x04 = 0
        self.unknown_0x08 = 0
        self.offset = None
        
        self.frame_data = []
        
    def __repr__(self):
        return f"[KFMO::FCurveDef] {self.unknown_0x00} {self.type} {self.divisor} "\
               f"{self.unknown_0x04} {self.unknown_0x08} {self.offset}"
        
    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint8(self.unknown_0x00)
        self.type         = rw.rw_uint8(self.type)
        self.divisor      = rw.rw_uint8(self.divisor)
        rw.align(rw.local_tell(), 0x04)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.offset       = rw.rw_pointer(self.offset)
        
        rw.assert_equal(self.unknown_0x00, 1)
        rw.assert_is_zero(self.unknown_0x04)
        rw.assert_is_zero(self.unknown_0x08)

    def rw_framedata(self, rw, frame_count):
        divisor = 2**self.divisor
        
        if self.type == 1:
            op = rw.rw_float32s
        elif self.type == 2:
            op = lambda x, shape: rw.rw_ratio16s(x, divisor, shape)
        elif self.type == 3:
            op = lambda x, shape: rw.rw_ratio8s(x, divisor, shape)
        
        self.frame_data = op(self.frame_data, frame_count + 1)
