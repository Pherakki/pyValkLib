from pyValkLib.serialisation.Serializable import Serializable

class AssetReference(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.file_type = None
        self.mmf_offset = None
        
    def read_write(self, rw):
        self.file_type = rw.rw_uint32(self.file_type)
        self.mmf_offset = rw.rw_uint32(self.mmf_offset)
        rw.align(rw.local_tell(), 0x10)

    def __repr__(self):
        return f"[Asset Reference] Filetype: {self.file_type} Offset: {self.mmf_offset}"
