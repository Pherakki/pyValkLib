from pyValkLib.serialisation.Serializable import Serializable
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray

class EntryTable(Serializable):
    def __init__(self, entry_cls, endianness):
        super().__init__(endianness)
        self.entry_cls = entry_cls
        self.entries = PointerIndexableArray()
    
    def read_write(self, rw):
        self.padding_0x00 = rw.rw_uint32(self.padding_0x00)
        self.entry_count  = rw.rw_uint32(self.entry_count)
        self.entry_ptr    = rw.rw_uint32(self.entry_ptr)
        self.padding_0x0C = rw.rw_uint32(self.padding_0x0C)
        
        self.padding_0x10 = rw.rw_uint32(self.padding_0x10)
        self.padding_0x14 = rw.rw_uint32(self.padding_0x14)
        self.padding_0x18 = rw.rw_uint32(self.padding_0x18)
        self.padding_0x1C = rw.rw_uint32(self.padding_0x1C)
        
        self.padding_0x20 = rw.rw_uint32(self.padding_0x20)
        self.padding_0x24 = rw.rw_uint32(self.padding_0x24)
        self.padding_0x28 = rw.rw_uint32(self.padding_0x28)
        self.padding_0x2C = rw.rw_uint32(self.padding_0x2C)
        
        self.padding_0x30 = rw.rw_uint32(self.padding_0x30)
        self.padding_0x34 = rw.rw_uint32(self.padding_0x34)
        self.padding_0x38 = rw.rw_uint32(self.padding_0x38)
        self.padding_0x3C = rw.rw_uint32(self.padding_0x3C)
                
        rw.assert_is_zero(self.padding_0x00)
        rw.assert_is_zero(self.padding_0x0C)
        
        rw.assert_is_zero(self.padding_0x10)
        rw.assert_is_zero(self.padding_0x14)
        rw.assert_is_zero(self.padding_0x18)
        rw.assert_is_zero(self.padding_0x1C)
        
        rw.assert_is_zero(self.padding_0x20)
        rw.assert_is_zero(self.padding_0x24)
        rw.assert_is_zero(self.padding_0x28)
        rw.assert_is_zero(self.padding_0x2C)
        
        rw.assert_is_zero(self.padding_0x30)
        rw.assert_is_zero(self.padding_0x34)
        rw.assert_is_zero(self.padding_0x38)
        rw.assert_is_zero(self.padding_0x3C)
        
        if self.rw_method == "read":
            self.entries.data = [self.entry_cls(self.endianness) for _ in range(self.entry_count)]
            
    def rw_entry_headers(self, glob_tell, loc_tell):
        for entry in self.entries.data:
            n_entries =  len(self.entries.ptr_to_idx)
            curpos = self.bytestream.tell() - glob_tell + loc_tell
            self.entries.ptr_to_idx[curpos] = n_entries
            self.entries.idx_to_ptr.append(curpos)
            
            self.rw_readwriter(entry)
            


