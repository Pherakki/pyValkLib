from .HTEXReadWriter import HTEXReadWriter
from .HTSF.HTSFInterface import HTSFInterface


class HTEXInterface:
    def __init__(self):
        self.HTSFs = []
        
    @classmethod
    def from_subreader(cls, htex_rw):
        instance = cls()
        instance.HTSFs = [HTSFInterface.from_subreader(htsf) for htsf in htex_rw.HTSFs]
        return instance
    
    def to_subreader(self, depth):
        htex_rw = HTEXReadWriter(">")
        htex_rw.header.depth = depth
        htex_rw.header.contents_length = 0
        for htsf in self.HTSFs:
            htex_rw.HTSFs.append(htsf.to_subreader(depth + 1))
            htex_rw.header.contents_length += htex_rw.HTSFs[-1].header.header_length
            htex_rw.header.contents_length += htex_rw.HTSFs[-1].header.contents_length
        htex_rw.header.contents_length += htex_rw.EOFC.header.header_length
        htex_rw.header.contents_length += htex_rw.EOFC.header.contents_length
        htex_rw.EOFC.header.depth = depth
        return htex_rw
    