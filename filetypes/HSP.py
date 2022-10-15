import os

from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter
from pyValkLib.containers.IZCA.HSPR.HSPRReadWriter import HSPRReadWriter
from pyValkLib.serialisation.Serializable import Context, Serializable


class HSPReadWriter(Serializable):
    def __init__(self, context=None):
        if context is None:
            context = Context()
        super().__init__(context)
        self.HSPR = HSPRReadWriter(endianness=">")
        self.EOFC = EOFCReadWriter(endianness="<")
    
    def read_write(self, rw):
        rw.rw_obj(self.HSPR)
        rw.rw_obj(self.EOFC)
        rw.assert_at_eof()
