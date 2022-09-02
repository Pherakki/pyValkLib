import os

from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter
from pyValkLib.containers.MXMR.MXMRReadWriter import MXMRReadWriter
from pyValkLib.serialisation.Serializable import Context, Serializable


class MMRReadWriter(Serializable):
    def __init__(self, context=None):
        if context is None:
            context = Context()
        super().__init__(context)
        self.MXMR = MXMRReadWriter(endianness=">")
        self.EOFC = EOFCReadWriter(endianness="<")
    
    def read_write(self, rw):
        rw.rw_obj(self.MXMR)
        rw.rw_obj(self.EOFC)
        rw.assert_at_eof()
