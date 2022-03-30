from pyValkLib.serialisation.BaseRW import BaseRW
from pyValkLib.serialisation.ValkyriaBaseRW import PointerIndexableArray


class EntryTable(BaseRW):
    def __init__(self, entry_cls, endianness):
        super().__init__(endianness)
        self.entry_cls = entry_cls
        self.entries = PointerIndexableArray()
    
    def read_write(self):
        self.rw_var("padding_0x00", "I", endianness='>')
        self.rw_var("entry_count", "I", endianness='>')
        self.rw_var("entry_ptr", "I", endianness='>')
        self.rw_var("padding_0x0C", "I", endianness='>')
        
        self.rw_var("padding_0x10", "I", endianness='>')
        self.rw_var("padding_0x14", "I", endianness='>')
        self.rw_var("padding_0x18", "I", endianness='>')
        self.rw_var("padding_0x1C", "I", endianness='>')
        
        self.rw_var("padding_0x20", "I", endianness='>')
        self.rw_var("padding_0x24", "I", endianness='>')
        self.rw_var("padding_0x28", "I", endianness='>')
        self.rw_var("padding_0x2C", "I", endianness='>')
        
        self.rw_var("padding_0x30", "I", endianness='>')
        self.rw_var("padding_0x34", "I", endianness='>')
        self.rw_var("padding_0x38", "I", endianness='>')
        self.rw_var("padding_0x3C", "I", endianness='>')
                
        self.assert_equal("padding_0x00", 0)
        self.assert_equal("padding_0x0C", 0)
        
        self.assert_equal("padding_0x10", 0)
        self.assert_equal("padding_0x14", 0)
        self.assert_equal("padding_0x18", 0)
        self.assert_equal("padding_0x1C", 0)
        
        self.assert_equal("padding_0x20", 0)
        self.assert_equal("padding_0x24", 0)
        self.assert_equal("padding_0x28", 0)
        self.assert_equal("padding_0x2C", 0)
        
        self.assert_equal("padding_0x30", 0)
        self.assert_equal("padding_0x34", 0)
        self.assert_equal("padding_0x38", 0)
        self.assert_equal("padding_0x3C", 0)
        
        if self.rw_method == "read":
            self.entries.data = [self.entry_cls() for _ in range(self.entry_count)]
            
    def rw_entry_headers(self, glob_tell, loc_tell):
        for entry in self.entries.data:
            n_entries =  len(self.entries.ptr_to_idx)
            curpos = self.bytestream.tell() - glob_tell + loc_tell
            self.entries.ptr_to_idx[curpos] = n_entries
            self.entries.idx_to_ptr.append(curpos)
            
            self.rw_readwriter(entry)
            #getattr(entry, self.rw_method)(self.bytestream)
            


