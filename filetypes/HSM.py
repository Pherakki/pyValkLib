from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter
from pyValkLib.containers.HSCM.HSCMReadWriter import HSCMReadWriter
from pyValkLib.serialisation.Serializable import Context, Serializable


class HSMReadWriter(Serializable):
    def __init__(self, context=None):
        if context is None:
            context = Context()
        super().__init__(context)
        self.HSCM = HSCMReadWriter(endianness=">")
        self.EOFC = EOFCReadWriter(endianness="<")
    
    def read_write(self, rw):
        rw.rw_obj(self.HSCM)
        rw.rw_obj(self.EOFC)
        rw.assert_at_eof()
