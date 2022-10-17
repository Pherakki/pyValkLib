from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter
from pyValkLib.containers.HMRP.HMRPReadWriter import HMRPReadWriter
from pyValkLib.serialisation.Serializable import Context, Serializable


class HMOReadWriter(Serializable):
    def __init__(self, context=None):
        if context is None:
            context = Context()
        super().__init__(context)
        self.HMRP = HMRPReadWriter(endianness=">")
        self.EOFC = EOFCReadWriter(endianness="<")
    
    def read_write(self, rw):
        rw.rw_obj(self.HMRP)
        rw.rw_obj(self.EOFC)
        rw.assert_at_eof()
