from pyValkLib.serialisation.Serializable import Serializable

class FCurve(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.flags = None
        self.padding_0x04 = 0
        self.padding_0x08 = 0
        self.offset = None
        
        self.frame_data = []
        
    def read_write(self, rw):
        self.flags        = rw.rw_uint32(self.flags)
        self.padding_0x04 = rw.rw_uint32(self.padding_0x04)
        self.padding_0x08 = rw.rw_uint32(self.padding_0x08)
        self.offset       = rw.rw_pointer(self.offset)
        
        rw.assert_is_zero(self.padding_0x04)
        rw.assert_is_zero(self.padding_0x08)
    
    def rw_framedata(self, rw, frame_count):
        unknown = (self.flags & 0xFF000000) >> 0x18
        type_   = (self.flags & 0x00FF0000) >> 0x10
        divisor = (self.flags & 0x0000FF00) >> 0x08
        divisor = 2**divisor
        
        rw.assert_equal(unknown, 1)
        
        if type_ == 1:
            op = rw.rw_float32s
        elif type_ == 2:
            op = lambda x, shape: rw.rw_ratio16s(x, divisor, shape)
        elif type_ == 3:
            op = lambda x, shape: rw.rw_ratio8s(x, divisor, shape)
        
        self.frame_data = op(self.frame_data, frame_count + 1)
        