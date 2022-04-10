from pyValkLib.serialisation.ValkyriaBaseRW import BaseRW, PointerIndexableArray


    
class EntityEntry(BaseRW):
    __slots__ = ("ID", "name_offset", "count", "data_offset")

    def __init__(self, endianness):
        super().__init__(endianness)
        self.ID = 0
        self.name_offset = 0
        self.count = 0
        self.data_offset = 0
        
        self.data = None
        

    def read_write(self):
        self.rw_var("ID", "I")
        self.rw_var("name_offset", "I")
        self.rw_var("count", "I")
        self.rw_var("data_offset", "I")
        
        self.rw_var("padding_0x10", "I")
        self.rw_var("padding_0x14", "I")
        self.rw_var("count_4", "I")
        self.rw_var("padding_0x1C", "I")
        
        self.rw_var("padding_0x20", "I")
        self.rw_var("padding_0x24", "I")
        self.rw_var("unknown_0x28", "I")  # 0 or 1?
        self.rw_var("unknown_0x2C", "I")  # Ptr
        
        self.rw_var("padding_0x30", "I")
        self.rw_var("padding_0x34", "I")
        self.rw_var("padding_0x38", "I")
        self.rw_var("padding_0x3C", "I")
        
        self.assert_is_zero("padding_0x10")
        self.assert_is_zero("padding_0x14")
        self.assert_is_zero("padding_0x1C")
        
        self.assert_is_zero("padding_0x20")
        self.assert_is_zero("padding_0x24")
        
        self.assert_is_zero("padding_0x30")
        self.assert_is_zero("padding_0x34")
        self.assert_is_zero("padding_0x38")
        self.assert_is_zero("padding_0x3C")
        
    def rw_data(self, local_tell):
        if self.rw_method == "read":
            self.data = EntityData(self.count, local_tell - self.bytestream.tell())
        
        self.rw_readwriter(self.data)
        
    def __repr__(self):
        return f"::Entity Entry:: ID: [{self.ID}], Components: [{self.count}], Count4: [{self.count_4}], Unk_0x28: [{self.unknown_0x28}], Unk_0x2C: [{self.unknown_0x2C}]"
       
class EntityData(BaseRW):
    def __init__(self, count, global_to_local_offset):
        self.count = count
        self.global_to_local_offset = global_to_local_offset
        self.subentries = PointerIndexableArray()
        self.data = []
    
    def read_write(self):
        if self.rw_method == "read":
            self.subentries.data = [EntitySubEntry() for _ in range(self.count)]
        
        for i, subentry in enumerate(self.subentries.data):
            curpos = self.bytestream.tell() + self.global_to_local_offset
            self.subentries.ptr_to_idx[curpos] = i
            self.subentries.idx_to_ptr.append(curpos)
            getattr(subentry, self.rw_method)(self.bytestream)
            
        # Should make this a PointerIndexableArray
        n_to_rw = sum([subentry.count for subentry in self.subentries.data])
        self.rw_varlist('data', 'I', n_to_rw, endianness='>')
    
    def get_data(self):
        return ( self.subentries, self.data, )
    
    
class EntitySubEntry(BaseRW):
    def __init__(self):
        super().__init__()
        
    def read_write(self):
        self.rw_var("name_ptr", "I", endianness='>')
        self.rw_var("count", "I", endianness='>')
        self.rw_var("offset", "I", endianness='>')
        self.rw_var("padding_0x0C", "I", endianness='>')
        
    def __repr__(self):
        return f"::EntitySubEntry:: Name: {self.name_ptr}, Count: {self.count}, Offset: {self.offset}"
        
         