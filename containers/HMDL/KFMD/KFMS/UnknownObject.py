from pyValkLib.serialisation.Serializable import Context, Serializable

class UnknownObject(Serializable):
    def __init__(self, context=None):
        if context is None:
            self.context = Context()
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x02 = None
        self.unknown_0x03 = None
        self.unknown_0x04 = None
        self.unknown_0x05 = None
        self.unknown_0x06 = None
        self.unknown_0x07 = None
        self.unknown_0x08 = None
        self.unknown_0x09 = None
        self.unknown_0x0A = None
        self.unknown_0x0B = None
        self.unknown_0x0C = None
        self.unknown_0x0D = None
        self.unknown_0x0E = None
        self.unknown_0x0F = None
        
    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint16(self.unknown_0x00)
        self.unknown_0x02 = rw.rw_uint8(self.unknown_0x02)
        self.unknown_0x03 = rw.rw_uint8(self.unknown_0x03)
        self.unknown_0x04 = rw.rw_uint8(self.unknown_0x04)
        self.unknown_0x05 = rw.rw_uint8(self.unknown_0x05)
        self.unknown_0x06 = rw.rw_uint8(self.unknown_0x06)
        self.unknown_0x07 = rw.rw_uint8(self.unknown_0x07)
        self.unknown_0x08 = rw.rw_uint8(self.unknown_0x08)
        self.unknown_0x09 = rw.rw_uint8(self.unknown_0x09)
        self.unknown_0x0A = rw.rw_uint8(self.unknown_0x0A)
        self.unknown_0x0B = rw.rw_uint8(self.unknown_0x0B)
        self.unknown_0x0C = rw.rw_uint8(self.unknown_0x0C)
        self.unknown_0x0D = rw.rw_uint8(self.unknown_0x0D)
        self.unknown_0x0E = rw.rw_uint8(self.unknown_0x0E)
        self.unknown_0x0F = rw.rw_uint8(self.unknown_0x0F)
        