import os

from pyValkLib.containers.EOFC.EOFCReadWriter import EOFCReadWriter
from pyValkLib.containers.HTEX.HTEXInterface import HTEXInterface, HTEXReadWriter
from pyValkLib.containers.HTEX.HTSF.HTSFInterface import HTSFInterface
from pyValkLib.serialisation.Serializable import Context, Serializable


class HTXReadWriter(Serializable):
    def __init__(self, context=None):
        if context is None:
            context = Context()
        super().__init__(context)
        self.HTEX = HTEXReadWriter(endianness=">")
        self.EOFC = EOFCReadWriter(endianness="<")
    
    def read_write(self, rw):
        rw.rw_obj(self.HTEX)
        rw.rw_obj(self.EOFC)
        rw.assert_at_eof()

class HTX:
    def __init__(self):
        # Should replace if the flags can be calculated
        self.HTSFs = []
        
    def read(self, filepath):
        htx_rw = HTXReadWriter()
        htx_rw.read(filepath)
        hi = HTEXInterface.from_subreader(htx_rw.HTEX)
        self.HTSFs = [htsf for htsf in hi.HTSFs]
        
    def write(self, filepath):
        hi = HTEXInterface()
        hi.HTSFs = [htsf for htsf in self.HTSFs]
        
        htx_rw = HTXReadWriter()
        htx_rw.HTEX = hi.to_subreader(0)
        htx_rw.EOFC.header.depth = 0
        
        htx_rw.write(filepath)
        
    def extract_dds(self, filepath, idx):
        with open(filepath, 'wb') as F:
            F.write(self.HTSFs[idx].dds_data)
            
    def extract_all_dds(self, dirpath):
        for i, htsf in enumerate(self.HTSFs):
            self.extract_dds(os.path.join(dirpath, str(i) + os.path.extsep + "dds"), i)

    def add_dds(self, dds_data, flags):
        hi = HTSFInterface()
        hi.flags = flags
        hi.dds_data = dds_data
        self.HTSFs.append(hi)
        
    def import_dds(self, filepath, flags):
        with open(filepath, "rb") as F:
            self.add_dds(F.read(), flags)