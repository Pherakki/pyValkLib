from pyValkLib.serialisation.ValkyriaBaseRW import ValkyriaBaseRW32BH

class MXECReadWriter(ValkyriaBaseRW32BH):
    FILETYPE = "MXEC"
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        
        #self.MXEC = containers["MXEC"](containers, endianness)
        
        #self.subcontainers.extend([self.MXEC])
    
    def read_write_contents(self):
        self.assert_equal("flags", 0x18000000, self.header, lambda x: hex(x))