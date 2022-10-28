from pyValkLib.serialisation.ValkSerializable import Serializable, ValkSerializable16BH


class MXTFReadWriter(ValkSerializable16BH):
    FILETYPE = "MXTF"
    
    
    def __init__(self, endianness=None):
        super().__init__({}, "<")
        
        self.count = None
        self.entries = []
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x00000000, lambda x: hex(x))
        self.count = rw.rw_uint32(self.count)
        
        if rw.mode() == "read":
            self.entries = [Entry(self.context) for _ in range(self.count)]
            
        for o in self.entries:
            rw.rw_obj(o)
            
        
class Entry(Serializable):
    def __init__(self, context):
        super().__init__(context)
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.id           = None
        
    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.id           = rw.rw_uint32(self.id)
