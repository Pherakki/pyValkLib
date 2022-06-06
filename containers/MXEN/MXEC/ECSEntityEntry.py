from pyValkLib.serialisation.Serializable import Serializable
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray, PointerIndexableArrayUint32
    
class EntityEntry(Serializable):
    __slots__ = ("ID", "name_offset", "count", "data_offset", "data", "component_type",
                 "padding_0x10", "padding_0x14", "controller_entity_id", "padding_0x1C",
                 "padding_0x20", "padding_0x24", "unknown_0x28", "unknown_0x2C",
                 "padding_0x30", "padding_0x34", "padding_0x38", "padding_0x3C")

    def __init__(self, endianness):
        super().__init__(endianness)
        self.ID = 0
        self.name_offset = 0
        self.count = 0
        self.data_offset = 0
        
        self.padding_0x10          = 0
        self.padding_0x14          = 0
        self.controller_entity_id  = 0
        self.padding_0x1C          = 0
        
        self.padding_0x20          = 0
        self.padding_0x24          = 0
        self.unknown_0x28          = 0
        self.unknown_0x2C          = 0
        
        self.padding_0x30          = 0
        self.padding_0x34          = 0
        self.padding_0x38          = 0
        self.padding_0x3C          = 0
        
        self.data = None
        self.component_type = None
        

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
        
        self.padding_0x30          = rw.rw_pad32(self.padding_0x30)
        self.padding_0x34          = rw.rw_pad32(self.padding_0x34)
        self.padding_0x38          = rw.rw_pad32(self.padding_0x38)
        self.padding_0x3C          = rw.rw_pad32(self.padding_0x3C)
        
        rw.assert_is_zero(self.padding_0x10)
        rw.assert_is_zero(self.padding_0x14)
        rw.assert_is_zero(self.padding_0x1C)
        
        rw.assert_is_zero(self.padding_0x20)
        rw.assert_is_zero(self.padding_0x24)
        
        rw.assert_is_zero(self.padding_0x30)
        rw.assert_is_zero(self.padding_0x34)
        rw.assert_is_zero(self.padding_0x38)
        rw.assert_is_zero(self.padding_0x3C)
        
    def rw_data(self, rw, component_type):
        if rw.mode() == "read":
            self.data = EntityData(self.count, self.context)
        
        rw.rw_obj(self.data)
        
    def __repr__(self):
        return f"::Entity Entry:: ID: [{self.ID}], Components: [{self.count}], Controller ID: [{self.controller_entity_id}], Unk_0x28: [{self.unknown_0x28}], Unk_0x2C: [{self.unknown_0x2C}]"


class EntityData(Serializable):
    def __init__(self, count, context):
        super().__init__(context)
        self.count = count
        self.subentries = PointerIndexableArray(context)
        self.data       = PointerIndexableArrayUint32(context)
    
    def read_write(self, rw):
        if rw.mode() == "read":
            self.subentries.data = [EntitySubEntry(self.context) for _ in range(self.count)] 
        rw.rw_obj(self.subentries)
        if rw.mode() == "read":
            n_to_rw = sum([subentry.count for subentry in self.subentries.data])
            self.data.data = [0 for _ in range(n_to_rw)]
        rw.rw_obj(self.data)

    def get_data(self):
        return ( self.subentries, self.data, )
    
    
class EntitySubEntry(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.name_offset = 0
        self.count = 0
        self.offset = 0
        self.padding_0x0C = 0
        
    def read_write(self, rw):
        self.name_offset  = rw.rw_uint32(self.name_offset)
        self.count        = rw.rw_uint32(self.count)
        self.offset       = rw.rw_uint32(self.offset)
        self.padding_0x0C = rw.rw_uint32(self.padding_0x0C)
        rw.assert_is_zero(self.padding_0x0C)
        
    def __repr__(self):
        return f"::EntitySubEntry:: Name: {self.name_offset}, Count: {self.count}, Offset: {self.offset}"
