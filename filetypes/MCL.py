from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter
from pyValkLib.containers.CCOL.CCOLReadWriter import CCOLReadWriter
from pyValkLib.serialisation.Serializable import Context, Serializable


class MCLReadWriter(Serializable):
    def __init__(self, context=None):
        if context is None:
            context = Context()
        super().__init__(context)
        self.CCOL = CCOLReadWriter(">")
        self.EOFC = EOFCReadWriter(endianness="<")
    
    def read_write(self, rw):
        rw.rw_obj(self.CCOL)
        rw.rw_obj(self.EOFC)
        rw.assert_at_eof()
