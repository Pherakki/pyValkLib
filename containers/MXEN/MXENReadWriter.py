from pyValkLib.serialisation.ValkyriaBaseRW import ValkyriaBaseRW32BH

class MXENReadWriter(ValkyriaBaseRW32BH):
    FILETYPE = "MXEN"
    
    def read_write_contents(self):
        pass