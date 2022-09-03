import os

from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter
from pyValkLib.containers.MXMF.MXMFReadWriter import MXMFReadWriter
from pyValkLib.serialisation.Serializable import Context, Serializable


class MMFReadWriter(Serializable):
    def __init__(self, context=None):
        if context is None:
            context = Context()
        super().__init__(context)
        self.MXMF = MXMFReadWriter(endianness=">")
        self.EOFC = EOFCReadWriter(endianness="<")
    
    def read_write(self, rw):
        rw.rw_obj(self.MXMF)
        rw.rw_obj(self.EOFC)
        rw.assert_at_eof()
        
class MMF:
    class FileEntry:
        def __init__(self, folder, file, file_bytes):
            self.folder = folder
            self.file = file
            self.file_bytes = file_bytes
    
    def __init__(self):
        self.__filedata = []
        
    @classmethod
    def from_file(cls, filepath):
        instance = cls()
        
        mmf_rw = MMFReadWriter()
        mmf_rw.read(filepath)
        for mxmi in mmf_rw.MXMF.MXMB.MXMIs:
            instance.add_file(mxmi.MXMH.asset_folder_name, mxmi.MXMH.asset_file_name, mxmi.file_blob)
            
        return instance
        
    @property
    def filedata(self):
        return self.__filedata
    
    def add_file(self, folder_name, file_name, file_bytes=None):
        if file_bytes is None:
            with open(os.path.join(folder_name, file_name), 'rb') as F:
                file_bytes = F.read()
        self.__filedata.append(MMF.FileEntry(folder_name, file_name, file_bytes))
        
    def extract_file(self, idx, location=None):
        filedata = self.__filedata[idx]
        if location is None:
            filepath = os.path.join(filedata.folder, filedata.file)
        else:
            filepath = os.path.join(location, filedata.file)
        with open(filepath, 'wb') as F:
            F.write(filedata.file_bytes)
    
    def extract_all_files(self, location=None):
        for idx in range(len(self.__filedata)):
            self.extract_file(idx, location)
        