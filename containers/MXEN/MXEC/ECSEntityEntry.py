from pyValkLib.serialisation.Serializable import Serializable
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray
    
class EntityEntry(Serializable):
    __slots__ = ("ID", "name_offset", "count", "data_offset")

    def __init__(self, endianness):
        super().__init__(endianness)
        self.ID = 0
        self.name_offset = 0
        self.count = 0
        self.data_offset = 0
        
        self.data = None
        

    def read_write(self, rw):
        self.ID                    = rw.rw_uint32(self.ID)
        self.name_offset           = rw.rw_uint32(self.name_offset)
        self.count                 = rw.rw_uint32(self.count)
        self.data_offset           = rw.rw_uint32(self.data_offset)
        
        self.padding_0x10          = rw.rw_uint32(self.padding_0x10)
        self.padding_0x14          = rw.rw_uint32(self.padding_0x14)
        self.controller_entity_id  = rw.rw_uint32(self.controller_entity_id)
        self.padding_0x1C          = rw.rw_uint32(self.padding_0x1C)
        
        self.padding_0x20          = rw.rw_uint32(self.padding_0x20)
        self.padding_0x24          = rw.rw_uint32(self.padding_0x24)
        self.unknown_0x28          = rw.rw_uint32(self.unknown_0x28) # 0 or 1
        self.unknown_0x2C          = rw.rw_uint32(self.unknown_0x2C) # Ptr
        
        self.padding_0x30          = rw.rw_uint32(self.padding_0x30)
        self.padding_0x34          = rw.rw_uint32(self.padding_0x34)
        self.unknown_0x38          = rw.rw_uint32(self.unknown_0x38)
        self.unknown_0x3C          = rw.rw_uint32(self.unknown_0x3C)
        
        rw.assert_is_zero(self.padding_0x10)
        rw.assert_is_zero(self.padding_0x14)
        rw.assert_is_zero(self.padding_0x1C)
        
        rw.assert_is_zero(self.padding_0x20)
        rw.assert_is_zero(self.padding_0x24)
        
        rw.assert_is_zero(self.padding_0x30)
        rw.assert_is_zero(self.padding_0x34)
        rw.assert_is_zero(self.padding_0x38)
        rw.assert_is_zero(self.padding_0x3C)
        
    def rw_data(self, local_tell):
        if self.rw_method == "read":
            self.data = EntityData(self.count, local_tell - self.bytestream.tell())
        
        self.rw_readwriter(self.data)
        
    def __repr__(self):
        return f"::Entity Entry:: ID: [{self.ID}], Components: [{self.count}], Controller ID: [{self.controller_entity_id}], Unk_0x28: [{self.unknown_0x28}], Unk_0x2C: [{self.unknown_0x2C}]"
       
class EntityData(Serializable):
    def __init__(self, count, global_to_local_offset):
        self.count = count
        self.global_to_local_offset = global_to_local_offset
        self.subentries = PointerIndexableArray()
        self.data = []
    
    def read_write(self, rw):
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
    
    
class EntitySubEntry(Serializable):
    def __init__(self):
        super().__init__()
        
    def read_write(self, rw):
        self.name_offset  = rw.rw_uint32(self.name_offset)
        self.count        = rw.rw_uint32(self.count)
        self.offset       = rw.rw_uint32(self.offset)
        self.padding_0x0C = rw.rw_uint32(self.padding_0x0C)
        rw.assert_is_zero(self.padding_0x0C)
        
    def __repr__(self):
        return f"::EntitySubEntry:: Name: {self.name_offset}, Count: {self.count}, Offset: {self.offset}"
        
         