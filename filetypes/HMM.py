from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter
from pyValkLib.containers.HMMT.HMMTReadWriter import HMMTReadWriter
from pyValkLib.serialisation.Serializable import Context, Serializable


class HMMReadWriter(Serializable):
    def __init__(self, context=None):
        if context is None:
            context = Context()
        super().__init__(context)
        self.HMMT = HMMTReadWriter(endianness=">")
        self.EOFC = EOFCReadWriter(endianness="<")
    
    def read_write(self, rw):
        rw.rw_obj(self.HMMT)
        rw.rw_obj(self.EOFC)
        rw.assert_at_eof()
