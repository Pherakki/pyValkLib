from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter0x10
from pyValkLib.containers.IZCA.IZCAReadWriter import IZCAReadWriter
from pyValkLib.serialisation.Serializable import Context, Serializable


class MLXReadWriter(Serializable):
    def __init__(self, context=None):
        if context is None:
            context = Context()
        super().__init__(context)
        self.IZCA = IZCAReadWriter("<", ">")
        self.EOFC = EOFCReadWriter0x10(endianness="<")
    
    def read_write(self, rw):
        rw.rw_obj(self.IZCA)
        rw.rw_obj(self.EOFC)
        rw.assert_at_eof()
