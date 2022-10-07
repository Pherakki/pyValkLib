from pyValkLib.serialisation.ValkSerializable import Serializable, ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray
from pyValkLib.containers.Metadata.POF0.POF0ReadWriter import POF0ReadWriter
from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.CCRS.CCRSReadWriter import CCRSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

class KSPRReadWriter(ValkSerializable32BH):
    FILETYPE = "KSPR"
    
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x18000000
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.unk_obj_1_count = None
        self.unk_obj_1_offset = None
        self.unknown_0x10 = None
        self.unknown_0x14 = None
        self.unknown_0x18 = None
        self.unknown_0x1C = None
        
        self.unk_obj_1s = []
        self.unknown_index_list = PointerIndexableArray(self.context)
        self.unk_obj_3s = PointerIndexableArray(self.context)
        self.unk_obj_4s = PointerIndexableArray(self.context)
        self.unk_obj_5s = PointerIndexableArray(self.context)
        self.unk_obj_6s = PointerIndexableArray(self.context)
        
        self.POF0 = POF0ReadWriter("<")
        self.ENRS = ENRSReadWriter("<")
        self.CCRS = CCRSReadWriter("<")
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.POF0, self.ENRS, self.CCRS, self.EOFC]
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))
        
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unk_obj_1_count = rw.rw_uint32(self.unk_obj_1_count)
        self.unk_obj_1_offset = rw.rw_pointer(self.unk_obj_1_offset)
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_float32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_float32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_float32(self.unknown_0x1C)
        rw.align(0x20, 0x40)
        
        print(self.unknown_0x00, self.unknown_0x04, self.unk_obj_1_count, self.unk_obj_1_offset)
        print(self.unknown_0x10, self.unknown_0x14, self.unknown_0x18, self.unknown_0x1C)
        print(">>", rw.local_tell())
        
        
        # Obj list 1
        self.unk_obj_1s = rw.rw_obj_array(self.unk_obj_1s, lambda: UnknownObject1(self.context), self.unk_obj_1_count)
        for obj in self.unk_obj_1s:
            rw.rw_obj_method(obj, obj.rw_unknown_floats)
        print(">>", rw.local_tell())
        print(self.unk_obj_1s)
        
        rw.align(0x10, 0x50)
        print(">>", rw.local_tell())
        
        
        # Obj list 2
        info = sorted(set((o.unknown_0x28, o.unknown_float_count) for o in self.unk_obj_1s if o.unknown_0x28 != 0))
        if rw.mode() == "read":
            self.unknown_index_list.data = [UnknownObject2(self.context, count) for ptr, count in info]
        self.unknown_index_list = rw.rw_obj(self.unknown_index_list)
        print(self.unknown_index_list)
        rw.align(rw.local_tell(), 0x40)
        print(">>", rw.local_tell())
        
        
        # Obj list 3
        info = sorted(set((o.unknown_0x20, o.unknown_float_count) for o in self.unk_obj_1s if o.unknown_0x20 != 0))
        if rw.mode() == "read":
            self.unk_obj_3s.data = [UnknownObject3(self.context, count) for ptr, count in info]
        self.unk_obj_3s = rw.rw_obj(self.unk_obj_3s)
        print(self.unk_obj_3s)
        print(">>", rw.local_tell())
        
        # Obj list 4
        info = sorted(set((so.unknown_offset_2) for o in self.unk_obj_3s for so in o.subobjs if so.unknown_offset_2 != 0))
        if rw.mode() == "read":
            self.unk_obj_4s.data = [UnknownObject4(self.context) for ptr in info]
        self.unk_obj_4s = rw.rw_obj(self.unk_obj_4s)
        rw.align(rw.local_tell(), 0x10)
        print(self.unk_obj_4s)
        print(">>", rw.local_tell())
                
        # Obj list 5
        info = sorted(set((o.offset) for o in self.unk_obj_4s if o.offset != 0))
        if rw.mode() == "read":
            self.unk_obj_5s.data = [UnknownObject5(self.context) for ptr in info]
        self.unk_obj_5s = rw.rw_obj(self.unk_obj_5s)
        
        print(self.unk_obj_5s)
        print(">>", rw.local_tell())
                       
        # Obj list 6
        info = sorted(set((o.unknown_0x24, o.unknown_float_count) for o in self.unk_obj_1s if o.unknown_0x24 != 0))
        if rw.mode() == "read":
            self.unk_obj_6s.data = [UnknownObject6(self.context, count) for ptr, count in info]
        self.unk_obj_6s = rw.rw_obj(self.unk_obj_6s)
        print(self.unk_obj_6s)
        rw.align(0x50*sum(o[1] for o in info), 0x40)
        print(">>", rw.local_tell())
        print(">>>>", self.header.data_length)
        print(rw.peek_bytestring(0x80))
        print(rw.rw_int32s(None, 0x74))

    def __repr__(self):
        return f"KSPR Object [{self.header.depth}] [0x{self.header.flags:0>8x}]."

class UnknownObject1(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.ID = None
        self.flags = None
        self.unknown_float_count = None
        self.unknown_0x0C = None
        self.unknown_0x10 = None
        self.unknown_0x14 = None
        self.unknown_0x18 = None
        self.unknown_0x1C = None
        self.unknown_0x20 = None
        self.unknown_0x24 = None
        self.unknown_0x28 = None
        self.unknown_0x2C = None
        self.unknown_0x30 = None
        self.unknown_0x34 = None
        self.unknown_0x38 = None
        self.unknown_0x3C = None
        
        self.unknown_floats = []
        
    def __repr__(self):
        return f"[KSPR::UnkObj1] {self.ID} {hex(self.flags)} {self.unknown_float_count} {self.unknown_0x0C} "\
               f"{self.unknown_0x10} {self.unknown_0x14} {self.unknown_0x18} {self.unknown_0x1C} " \
               f"{self.unknown_0x20} {self.unknown_0x24} {self.unknown_0x28} {self.unknown_0x2C} " \
               f"{self.unknown_0x30} {self.unknown_0x34} {self.unknown_0x38} {self.unknown_0x3C} " \
               f"{list(self.unknown_floats)}"
    
    def read_write(self, rw):
        self.ID = rw.rw_uint32(self.ID)
        self.flags = rw.rw_uint32(self.ID)
        self.unknown_float_count = rw.rw_uint32(self.unknown_float_count)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        self.unknown_0x10 = rw.rw_uint32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_uint32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_uint32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_pointer(self.unknown_0x1C)
        self.unknown_0x20 = rw.rw_pointer(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_pointer(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_pointer(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_pointer(self.unknown_0x2C)
        self.unknown_0x30 = rw.rw_pointer(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_uint32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_uint32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_uint32(self.unknown_0x3C)
        
    def rw_unknown_floats(self, rw):
        self.unknown_floats = rw.rw_uint32s(self.unknown_floats, self.unknown_float_count)
        rw.align(self.unknown_float_count*4, 0x40)
        
class UnknownObject2(Serializable):
    def __init__(self, context, count):
        super().__init__(context)
        
        self.indices = None
        self.count = count
        
    def __repr__(self):
        return f"[KSPR::UnkObj2] {list(self.indices)}"
        
    def read_write(self, rw):
        self.indices = rw.rw_uint16s(self.indices, self.count)
        rw.align(rw.local_tell(), 0x10)

class UnknownObject3(Serializable):
    def __init__(self, context, count):
        super().__init__(context)
        
        self.__count = count
        self.subobjs = PointerIndexableArray(self.context)
        
    def __repr__(self):
        return f"[KSPR::UnkObj3] {self.subobjs}"
        
    def read_write(self, rw):
        if rw.mode() == "read":
            self.subobjs.data = [UnknownObject3SubObject(self.context) for _ in range(self.__count)]
        rw.rw_obj(self.subobjs)
        
class UnknownObject3SubObject(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.ID = None
        self.flags = None
        self.unknown_0x08 = None
        self.unknown_offset_1 = None
        self.unknown_0x10 = None
        self.unknown_offset_2 = None
        self.unknown_0x18 = None
        self.unknown_0x1C = None
        
    def __repr__(self):
        return f"[KSPR::UnkObj3SubObj] {self.ID} {hex(self.flags)} {self.unknown_0x08} {self.unknown_offset_1} " \
               f"{self.unknown_0x10} {self.unknown_offset_2} {self.unknown_0x18} {self.unknown_0x1C}"
        
    def read_write(self, rw):
        self.ID = rw.rw_uint32(self.ID)
        self.flags = rw.rw_uint32(self.flags)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_offset_1 = rw.rw_pointer(self.unknown_offset_1)
        
        self.unknown_0x10 = rw.rw_uint32(self.unknown_0x10)
        self.unknown_offset_2 = rw.rw_pointer(self.unknown_offset_2)
        self.unknown_0x18 = rw.rw_uint32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_uint32(self.unknown_0x1C)
        
class UnknownObject4(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.idx = None
        self.offset = None
        
    def __repr__(self):
        return f"[KSPR::UnkObj4] {self.idx} {self.offset}"
        
    def read_write(self, rw):
        self.idx = rw.rw_uint32(self.idx)
        self.offset = rw.rw_pointer(self.offset)
        
class UnknownObject5(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        
    def __repr__(self):
        return f"[KSPR::UnkObj5] {self.unknown_0x00} {self.unknown_0x04} {self.unknown_0x08} {self.unknown_0x0C}"
        
    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_float32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
            
class UnknownObject6(Serializable):
    def __init__(self, context, count):
        super().__init__(context)
        
        self.__count = count
        self.subobjs = PointerIndexableArray(self.context)
        
    def __repr__(self):
        return f"[KSPR::UnkObj6] {self.subobjs}"
        
    def read_write(self, rw):
        if rw.mode() == "read":
            self.subobjs.data = [UnknownObject6SubObject(self.context) for _ in range(self.__count)]
        rw.rw_obj(self.subobjs)
        
class UnknownObject6SubObject(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        self.unknown_0x10 = None
        self.unknown_0x14 = None
        self.unknown_0x18 = None
        self.unknown_0x1C = None
        self.unknown_0x20 = None
        self.unknown_0x24 = None
        self.unknown_0x28 = None
        self.unknown_0x2C = None
        self.unknown_0x30 = None
        self.unknown_0x34 = None
        self.unknown_0x38 = None
        self.unknown_0x3C = None
        self.unknown_0x40 = None
        self.unknown_0x44 = None
        self.unknown_0x48 = None
        self.unknown_0x4C = None
        
    def __repr__(self):
        return f"[KSPR::UnkObj6SubObj] "\
            f"{self.unknown_0x00} {self.unknown_0x04} {self.unknown_0x08} {self.unknown_0x0C} "\
            f"{self.unknown_0x10} {self.unknown_0x14} {self.unknown_0x18} {self.unknown_0x1C} "\
            f"{self.unknown_0x20} {self.unknown_0x24} {self.unknown_0x28} {self.unknown_0x2C} "\
            f"{self.unknown_0x30} {self.unknown_0x34} {self.unknown_0x38} {self.unknown_0x3C} "\
            f"{self.unknown_0x40} {self.unknown_0x44} {self.unknown_0x48} {self.unknown_0x4C} "
        
    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_float32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_int32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_int32(self.unknown_0x1C)
        self.unknown_0x20 = rw.rw_int32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_int32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_int32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_int32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_uint32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_uint32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_uint32(self.unknown_0x38)
        self.unknown_0x3C = rw.rw_uint32(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_uint32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_uint32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_uint32(self.unknown_0x48)
        self.unknown_0x4C = rw.rw_uint32(self.unknown_0x4C)