from .HTSFReadWriter import HTSFReadWriter


class HTSFInterface:
    def __init__(self):
        self.flags = None
        self.dds_data = None
        
    @classmethod
    def from_subreader(cls, htsf_rw):
        instance = cls()
        instance.flags = htsf_rw.header.flags
        instance.dds_data = htsf_rw.dds_data
        return instance
    
    def to_subreader(self, depth):
        htsf_rw = HTSFReadWriter(">")
        htsf_rw.flags = self.flags
        htsf_rw.dds_data = self.dds_data
        htsf_rw.header.data_length = len(htsf_rw.dds_data) + 0x20
        htsf_rw.header.contents_length = htsf_rw.header.data_length
        htsf_rw.header.depth = depth

        return htsf_rw
    