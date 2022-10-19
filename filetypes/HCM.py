from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter
from pyValkLib.containers.HCMT.HCMTReadWriter import HCMTReadWriter
from pyValkLib.serialisation.Serializable import Context, Serializable


class HCMReadWriter(Serializable):
    def __init__(self, context=None):
        if context is None:
            context = Context()
        super().__init__(context)
        self.HCMT = HCMTReadWriter(endianness=">")
        self.EOFC = EOFCReadWriter(endianness="<")
    
    def read_write(self, rw):
        rw.rw_obj(self.HCMT)
        rw.rw_obj(self.EOFC)
        rw.assert_at_eof()
