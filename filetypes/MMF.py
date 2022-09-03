from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter
from pyValkLib.containers.MXMF.MXMFReadWriter import MXMFReadWriter
from pyValkLib.serialisation.Serializable import Context, Serializable


class MMFReadWriter(Serializable):
    def __init__(self, context=None):
        if context is None:
            context = Context()
        super().__init__(context)
        self.MXMF = MXMFReadWriter(endianness=">")
        self.EOFC = EOFCReadWriter(endianness="<")
    
    def read_write(self, rw):
        rw.rw_obj(self.MXMF)
        rw.rw_obj(self.EOFC)
        rw.assert_at_eof()
