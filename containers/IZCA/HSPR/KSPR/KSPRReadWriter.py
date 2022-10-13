from collections import defaultdict

from pyValkLib.serialisation.ValkSerializable import Serializable, ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray, PointerIndexableArrayUint16, PointerIndexableArrayUint32

from pyValkLib.containers.Metadata.POF0.POF0ReadWriter import POF0ReadWriter
from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.CCRS.CCRSReadWriter import CCRSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

def gen_element_count(objs, element_size, offset_accessor, count_accessor=lambda x: x.element_count):
    offsets = set()
    for o in objs:
        offset = offset_accessor(o)
        count = count_accessor(o)
        if offset == 0:
            continue
        for i in range(count):
            offsets.add(offset + element_size*i)
    offsets = sorted(offsets)
                
    return ((offsets[-1] - offsets[0]) // element_size) + 1, offsets
    

class KSPRRipper(ValkSerializable32BH):
    FILETYPE = "KSPR"
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x18000000
        
        self.unknown_0x00 = None
        self.padding_0x04 = None
        self.obj_count = None
        self.objs_offset = None
        self.unknown_0x10 = None
        self.unknown_0x14 = None
        self.unknown_0x18 = None
        self.unknown_0x1C = None
        
        self.objects = []
        
        self.POF0 = POF0ReadWriter("<")
        self.ENRS = ENRSReadWriter("<")
        self.CCRS = CCRSReadWriter("<")
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.POF0, self.ENRS, self.CCRS, self.EOFC]
        
    def read_write_contents(self, rw):
        rw.mark_new_contents_array()
        rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))
        
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.padding_0x04 = rw.rw_pad32(self.padding_0x04)
        self.unk_obj_1_count = rw.rw_uint32(self.unk_obj_1_count)
        self.unk_obj_1_offset = rw.rw_pointer(self.unk_obj_1_offset)
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_float32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_float32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_float32(self.unknown_0x1C)
        rw.assert_is_zero(self.padding_0x04)
        rw.align(0x20, 0x40)
        
        
        rw.assert_local_file_pointer_now_at("RippedObjs", self.objs_offset)
        self.objects = [RippedObj(self.context) for _ in range(self.obj_count)]
        for obj in self.objects:
            rw.rw_obj(obj)
            
        rw.local_seek(self.header.data_length + self.header.header_length)
        

class RippedObj(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.ID = None
        self.type = None
        self.element_count = None
        self.unknown_0x0C = None
        self.unknown_0x0E = None
        self.unknown_0x10 = None
        self.padding_0x12 = None
        self.unknown_0x14 = None
        self.unknown_0x18 = None
        self.data_7_offset = None
        self.data_4_offset = None
        self.data_5_offset = None
        self.data_3_offset = None
        self.data_1_offset = None
        self.data_2_offset = None
        self.padding_0x34 = None
        self.unknown_0x38 = None
        self.data_6_offset = None
        
        self.data_1 = None
        self.data_2 = None
        self.data_3 = None
        self.data_4 = None
        self.data_5 = None
        self.data_6 = None
        self.data_7 = None
        
    def __repr__(self):
        return f"[KSPR::RippedObj] {self.ID} {self.type} {self.element_count} "\
               f"{self.unknown_0x10} {self.unknown_0x38} " \
               f"{self.data_1_offset} {self.data_2_offset} {self.data_3_offset} " \
               f"{self.data_4_offset} {self.data_5_offset} " \
               f"{self.data_6_offset} {self.data_7_offset} "
    
    def read_write(self, rw):
        self.ID = rw.rw_uint32(self.ID)
        self.type = rw.rw_bytestring(self.type, 4)
        self.element_count = rw.rw_uint32(self.element_count)
        self.unknown_0x0C = rw.rw_uint16(self.unknown_0x0C)
        self.unknown_0x0E = rw.rw_uint16(self.unknown_0x0E)
        self.unknown_0x10 = rw.rw_uint16(self.unknown_0x10)
        self.padding_0x12 = rw.rw_pad16(self.padding_0x12)
        self.unknown_0x14 = rw.rw_uint32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_uint32(self.unknown_0x18)
        self.data_7_offset = rw.rw_pointer(self.data_7_offset)
        self.data_4_offset = rw.rw_pointer(self.data_4_offset)
        self.data_5_offset = rw.rw_pointer(self.data_5_offset)
        self.data_3_offset = rw.rw_pointer(self.data_3_offset)
        self.data_1_offset = rw.rw_pointer(self.data_1_offset)
        self.data_2_offset = rw.rw_pointer(self.data_2_offset)
        self.padding_0x34 = rw.rw_pad32(self.padding_0x34)
        self.unknown_0x38 = rw.rw_uint32(self.unknown_0x38)
        self.data_6_offset = rw.rw_pointer(self.data_6_offset)
        
        rw.assert_is_zero(self.unknown_0x0C)
        rw.assert_is_zero(self.unknown_0x0E)
        rw.assert_is_zero(self.padding_0x12)
        rw.assert_is_zero(self.unknown_0x14)
        rw.assert_is_zero(self.unknown_0x18)
        rw.assert_is_zero(self.padding_0x34)
        
        offset = rw.local_tell()
        
        if self.data_1_offset:
            rw.local_seek(self.data_1_offset)
            self.data_1 = rw.rw_uint32s(self.data_1, self.element_count)
        if self.data_2_offset:
            rw.local_seek(self.data_2_offset)
            self.data_2 = rw.rw_uint32s(self.data_2, self.element_count)
        if self.data_3_offset:
            rw.local_seek(self.data_3_offset)
            self.data_3 = rw.rw_uint16s(self.data_3, self.element_count)
        if self.data_4_offset:
            rw.local_seek(self.data_4_offset)
            self.data_4 = [UnknownObject3SubObject(self.context) for _ in range(self.element_count)]
            for i, o in enumerate(self.data_4): 
                self.data_4[i] = rw.rw_obj(o)
                pos = rw.local_tell()
                rw.local_seek(o.unknown_offset_2)
                o.obj = UnknownObject4(self.context)
                rw.rw_obj(o.obj)
                o.obj.obj = UnknownObject5(self.context)
                rw.rw_obj(o.obj.obj)
                rw.local_seek(pos)
        if self.data_5_offset:
            rw.local_seek(self.data_5_offset)
            self.data_5 = [UnknownObject6SubObject(self.context) for _ in range(self.element_count)]
            for i, o in enumerate(self.data_5): self.data_5[i] = rw.rw_obj(o)
        if self.data_6_offset:
            rw.local_seek(self.data_6_offset)
            self.data_6 = [UnknownObject7(self.context) for _ in range(self.element_count)]
            for i, o in enumerate(self.data_6): self.data_6[i] = rw.rw_obj(o)
        if self.data_7_offset:
            rw.local_seek(self.data_7_offset)
            self.data_7 = [UnknownObject9(self.context) for _ in range(self.element_count)]
            for i, o in enumerate(self.data_7): self.data_7[i] = rw.rw_obj(o)
        
        rw.local_seek(offset)
        

class KSPRReadWriter(ValkSerializable32BH):
    FILETYPE = "KSPR"
    
    
    def __init__(self, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x18000000
        
        self.unknown_0x00 = None
        self.padding_0x04 = None
        self.obj_count = None
        self.objs_offset = None
        self.unknown_0x10 = None
        self.unknown_0x14 = None
        self.unknown_0x18 = None
        self.unknown_0x1C = None
        
        self.objects  = []
        self.data_1   = PointerIndexableArrayUint32(self.context)
        self.data_2   = PointerIndexableArrayUint32(self.context)
        self.data_3   = PointerIndexableArrayUint16(self.context)
        self.data_4   = PointerIndexableArray(self.context)
        self.data_4A  = PointerIndexableArray(self.context)
        self.data_4AA = PointerIndexableArray(self.context)
        self.data_5   = PointerIndexableArray(self.context)
        self.data_6   = PointerIndexableArray(self.context)
        self.data_6A  = PointerIndexableArrayUint32(self.context)
        self.data_6B  = PointerIndexableArray(self.context)
        self.data_6BA = PointerIndexableArray(self.context)
        self.data_6BB = PointerIndexableArray(self.context)
        self.data_7   = PointerIndexableArray(self.context)
        
        self.POF0 = POF0ReadWriter("<")
        self.ENRS = ENRSReadWriter("<")
        self.CCRS = CCRSReadWriter("<")
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.POF0, self.ENRS, self.CCRS, self.EOFC]
        
    def read_write_contents(self, rw):
        self.rw_header(rw)
        self.rw_sprite_objs(rw)
        self.rw_data_1(rw)
        self.rw_data_2(rw)
        self.rw_data_3(rw)
        self.rw_data_4(rw)
        self.rw_data_4A(rw)
        self.rw_data_4AA(rw)
        self.rw_data_5(rw)
        self.rw_data_6(rw)
        self.rw_data_6A(rw)
        self.rw_data_6B(rw)
        self.rw_data_6BA(rw)
        self.rw_data_6BB(rw)
        self.rw_data_7(rw)
        
    def rw_header(self, rw):
        rw.mark_new_contents_array()
        rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))
        
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.padding_0x04 = rw.rw_pad32(self.padding_0x04)
        self.obj_count    = rw.rw_uint32(self.obj_count)
        self.objs_offset  = rw.rw_pointer(self.objs_offset)
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_float32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_float32(self.unknown_0x18)
        self.unknown_0x1C = rw.rw_float32(self.unknown_0x1C)
        rw.assert_is_zero(self.padding_0x04)
        rw.align(0x20, 0x40)
        
        
    def rw_sprite_objs(self, rw):
        rw.mark_new_contents_array()
        rw.assert_local_file_pointer_now_at("SpriteObjects", self.objs_offset)
        self.objects = rw.rw_obj_array(self.objects, lambda: SpriteObject(self.context), self.obj_count)
        
        
    def rw_data_1(self, rw):
        element_size = 4
        element_count, offsets = gen_element_count(self.objects, element_size, lambda x: x.data_1_offset)
        rw.assert_local_file_pointer_now_at("Data 1", offsets[0])
        if rw.mode() == "read":
            self.data_1.data = [None for _ in range(element_count)]
        self.data_1 = rw.rw_obj(self.data_1)
        rw.align(element_count*element_size, 0x40)
        
    def rw_data_2(self, rw):
        element_size = 4
        element_count, offsets = gen_element_count(self.objects, element_size, lambda x: x.data_2_offset)
        rw.assert_local_file_pointer_now_at("Data 2", offsets[0])
        if rw.mode() == "read":
            self.data_2.data = [None for _ in range(element_count)]
        self.data_2 = rw.rw_obj(self.data_2)
        rw.align(element_count*element_size, 0x40)
        rw.assert_equal(list(self.data_2), [0]*element_count)
        
    def rw_data_3(self, rw):
        rw.mark_new_contents_array()
        element_size = 2
        element_count, offsets = gen_element_count(self.objects, element_size, lambda x: x.data_3_offset)
        rw.assert_local_file_pointer_now_at("Data 3", offsets[0])
        if rw.mode() == "read":
            self.data_3.data = [None for _ in range(element_count)]
        self.data_3 = rw.rw_obj(self.data_3)
        rw.align(rw.local_tell(), 0x40)
        
    def rw_data_4(self, rw):
        rw.mark_new_contents_array()
        element_size = 0x20
        element_count, offsets = gen_element_count(self.objects, element_size, lambda x: x.data_4_offset)
        rw.assert_local_file_pointer_now_at("Data 4", offsets[0])
        if rw.mode() == "read":
            self.data_4.data = [UnknownObject4(self.context) for _ in range(element_count)]
        self.data_4 = rw.rw_obj(self.data_4)
        
    def rw_data_4A(self, rw):
        rw.mark_new_contents_array()
        element_size = 0x08
        offsets = sorted(set([o.unknown_offset_3 for o in self.data_4]))
        element_count = ((offsets[-1] - offsets[0]) // element_size) + 1
        rw.assert_local_file_pointer_now_at("Data 4A", offsets[0])
        if rw.mode() == "read":
            self.data_4A.data = [UnknownObject4A(self.context) for _ in range(element_count)]
        self.data_4A = rw.rw_obj(self.data_4A)
        rw.align(rw.local_tell(), 0x10)
                
    def rw_data_4AA(self, rw):
        rw.mark_new_contents_array()
        element_size = 0x10
        offsets = sorted(set([o.offset for o in self.data_4A]))
        element_count = ((offsets[-1] - offsets[0]) // element_size) + 1
        rw.assert_local_file_pointer_now_at("Data 4AA", offsets[0])
        if rw.mode() == "read":
            self.data_4AA.data = [UnknownObject4AA(self.context) for _ in range(element_count)]
        self.data_4AA = rw.rw_obj(self.data_4AA)
        rw.align(element_count*element_size, 0x50) # Not convinced this is right
                       
    def rw_data_5(self, rw):
        rw.mark_new_contents_array()
        element_size = 0x50
        element_count, offsets = gen_element_count(self.objects, element_size, lambda x: x.data_5_offset)
        rw.assert_local_file_pointer_now_at("Data 5", offsets[0])
        if rw.mode() == "read":
            self.data_5.data = [UnknownObject5(self.context) for _ in range(element_count)]
        self.data_5 = rw.rw_obj(self.data_5)
        rw.align(element_count*element_size, 0x40)
        
    def rw_data_6(self, rw):
        rw.mark_new_contents_array()
        element_size = 0x20
        element_count, offsets = gen_element_count(self.objects, element_size, lambda x: x.data_6_offset, lambda x: x.unknown_0x38)
        rw.assert_local_file_pointer_now_at("Data 6", offsets[0])
        if rw.mode() == "read":
            self.data_6.data = [UnknownObject6(self.context) for _ in range(element_count)]
        self.data_6 = rw.rw_obj(self.data_6)
        rw.align(element_count*element_size, 0x40)
        
    def rw_data_6A(self, rw):
        rw.mark_new_contents_array()
        element_size = 0x04
        element_count, offsets = gen_element_count(self.data_6, element_size, lambda x: x.unknown_offset_1, lambda x: x.unknown_0x08)
        rw.assert_local_file_pointer_now_at("Data 6A", offsets[0])
        if rw.mode() == "read":
            self.data_6A.data = [None for _ in range(element_count)]
        self.data_6A = rw.rw_obj(self.data_6A) # Flags?
        rw.align(element_count*element_size, 0x40)
        
        
    def rw_data_6B(self, rw):
        element_size = 0x10
        element_count, offsets = gen_element_count(self.data_6, element_size, lambda x: x.unknown_offset_2, lambda x: x.unknown_0x08)
        rw.assert_local_file_pointer_now_at("Data 6B", offsets[0])
        if rw.mode() == "read":
            # Element count is not correct...
            self.data_6B.data = [UnknownObject6B(self.context) for _ in range(element_count+1)]
        self.data_6B = rw.rw_obj(self.data_6B)
        rw.align(element_count*element_size, 0x40) # Alignment also wrong
        

    def rw_data_6BA(self, rw):
        rw.mark_new_contents_array()
        element_size = 0x10
        
        offsets = set()
        for o in self.data_6B:
            if o.unknown_offset_2 is not None and o.unknown_offset_2 != 0:
                offsets.update((o.unknown_offset_2 + element_size*i for i in range(1+o.unknown_0x04)))
        offsets = sorted(offsets)
        element_count = ((offsets[-1] - offsets[0]) // element_size) + 1
        rw.assert_local_file_pointer_now_at("Data 6BA", offsets[0])
        if rw.mode() == "read":
            self.data_6BA.data = [UnknownObject6BA(self.context) for _ in range(element_count)]
        self.data_6BA = rw.rw_obj(self.data_6BA)

    
    def rw_data_6BB(self, rw):
        rw.mark_new_contents_array()
        element_size = 0x10
        
        offsets = set()
        for o in self.data_6B:
            if o.unknown_offset_1 is not None and o.unknown_offset_1 != 0:
                offsets.add(o.unknown_offset_1)
        offsets = sorted(offsets)
        element_count = ((offsets[-1] - offsets[0]) // element_size) + 1
        
        rw.assert_local_file_pointer_now_at("Data 6BA", offsets[0])
        if rw.mode() == "read":
            self.data_6BB.data = [UnknownObject6BB(self.context) for _ in range(element_count)]
        self.data_6BB = rw.rw_obj(self.data_6BB)
            
    def rw_data_7(self, rw):
        rw.mark_new_contents_array()
        element_size = 0x10
        
        element_count, offsets = gen_element_count(self.objects, element_size, lambda x: x.data_7_offset, lambda x: 1)
        rw.assert_local_file_pointer_now_at("Data 7", offsets[0])
        if rw.mode() == "read":
            self.data_7.data = [UnknownObject7(self.context) for _ in range(element_count)]
        self.data_7 = rw.rw_obj(self.data_7)
        rw.mark_new_contents_array()

    def __repr__(self):
        return f"KSPR Object [{self.header.depth}] [0x{self.header.flags:0>8x}]."

def print_flag(flag):
    return hex(flag[0] << 0x18 | flag[1] << 0x10 | flag[2] << 0x08 | flag[3] << 0x00)

class SpriteObject(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.ID = None
        self.type = None
        self.element_count = None
        self.unknown_0x0C = None
        self.unknown_0x0E = None
        self.unknown_0x10 = None
        self.padding_0x12 = None
        self.unknown_0x14 = None
        self.unknown_0x18 = None
        self.data_7_offset = None
        self.data_4_offset = None
        self.data_5_offset = None
        self.data_3_offset = None
        self.data_1_offset = None
        self.data_2_offset = None
        self.padding_0x34 = None
        self.unknown_0x38 = None
        self.data_6_offset = None
        
    def __repr__(self):
        return f"[KSPR::SpriteObject] {self.ID} {self.type} {self.element_count} "\
               f"{self.unknown_0x10} {self.unknown_0x38} " \
               f"{self.data_1_offset} {self.data_2_offset} {self.data_3_offset} " \
               f"{self.data_4_offset} {self.data_5_offset} " \
               f"{self.data_6_offset} {self.data_7_offset} "
    
    def read_write(self, rw):
        self.ID = rw.rw_uint32(self.ID)
        self.type = rw.rw_bytestring(self.type, 4)
        self.element_count = rw.rw_uint32(self.element_count)
        self.unknown_0x0C = rw.rw_uint16(self.unknown_0x0C)
        self.unknown_0x0E = rw.rw_uint16(self.unknown_0x0E)
        self.unknown_0x10 = rw.rw_uint16(self.unknown_0x10)
        self.padding_0x12 = rw.rw_pad16(self.padding_0x12)
        self.unknown_0x14 = rw.rw_uint32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_uint32(self.unknown_0x18)
        self.data_7_offset = rw.rw_pointer(self.data_7_offset)
        self.data_4_offset = rw.rw_pointer(self.data_4_offset)
        self.data_5_offset = rw.rw_pointer(self.data_5_offset)
        self.data_3_offset = rw.rw_pointer(self.data_3_offset)
        self.data_1_offset = rw.rw_pointer(self.data_1_offset)
        self.data_2_offset = rw.rw_pointer(self.data_2_offset)
        self.padding_0x34 = rw.rw_pad32(self.padding_0x34)
        self.unknown_0x38 = rw.rw_uint32(self.unknown_0x38)
        self.data_6_offset = rw.rw_pointer(self.data_6_offset)
        
class UnknownObject4(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.ID = None
        self.type = None
        self.unknown_0x08 = None
        self.unknown_offset_1 = None
        self.unknown_offset_2 = None
        self.unknown_offset_3 = None
        self.unknown_0x18 = None
        self.unknown_0x1A = None
        self.unknown_0x1C = None
        self.unknown_0x1E = None
        
    def __repr__(self):
        return f"[KSPR::UnknownObject4] {self.ID} {self.type} {self.unknown_0x08} {self.unknown_offset_1} " \
               f"{self.unknown_offset_2} {self.unknown_offset_3} "\
               f"{self.unknown_0x18} {self.unknown_0x1A} {self.unknown_0x1C} {self.unknown_0x1E}"
        
    def read_write(self, rw):
        self.ID = rw.rw_uint32(self.ID)
        self.type = rw.rw_bytestring(self.type, 4)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_offset_1 = rw.rw_pointer(self.unknown_offset_1)
        
        self.unknown_offset_2 = rw.rw_pointer(self.unknown_offset_2)
        self.unknown_offset_3 = rw.rw_pointer(self.unknown_offset_3)
        self.unknown_0x18 = rw.rw_uint16(self.unknown_0x18)
        self.unknown_0x1A = rw.rw_uint16(self.unknown_0x1A)
        self.unknown_0x1C = rw.rw_uint16(self.unknown_0x1C)
        self.unknown_0x1E = rw.rw_uint16(self.unknown_0x1E)
        
class UnknownObject4A(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.idx = None
        self.offset = None
        
    def __repr__(self):
        return f"[KSPR::UnknownObject4A] {self.idx} {self.offset}"
        
    def read_write(self, rw):
        self.idx = rw.rw_int32(self.idx)
        self.offset = rw.rw_pointer(self.offset)
        
class UnknownObject4AA(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        
    def __repr__(self):
        return f"[KSPR::UnknownObject4AA] {self.unknown_0x00} {self.unknown_0x04} {self.unknown_0x08} {self.unknown_0x0C}"
        
    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_float32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)

        
class UnknownObject5(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        self.unknown_0x10 = None
        self.unknown_0x14 = None
        self.unknown_0x18 = None
        self.unknown_0x1A = None
        self.unknown_0x1C = None
        self.unknown_0x20 = None
        self.unknown_0x24 = None
        self.unknown_0x28 = None
        self.unknown_0x2C = None
        self.unknown_0x30 = None
        self.unknown_0x34 = None
        self.unknown_0x38 = None
        self.unknown_0x3A = None
        self.unknown_0x3C = None
        self.unknown_0x40 = None
        self.unknown_0x44 = None
        self.unknown_0x48 = None
        self.unknown_0x4A = None
        self.unknown_0x4C = None
        self.unknown_0x4E = None
        
    def __repr__(self):
        return f"[KSPR::UnknownObject5] "\
            f"{self.unknown_0x00} {self.unknown_0x04} {self.unknown_0x08} {self.unknown_0x0C} "\
            f"{self.unknown_0x10} {self.unknown_0x14} {self.unknown_0x18} {self.unknown_0x1A} {self.unknown_0x1C} "\
            f"{self.unknown_0x20} {self.unknown_0x24} {self.unknown_0x28} {self.unknown_0x2C} "\
            f"{self.unknown_0x30} {self.unknown_0x34} {self.unknown_0x38} {self.unknown_0x3A} {self.unknown_0x3C} "\
            f"{self.unknown_0x40} {self.unknown_0x44} {self.unknown_0x48} "\
            f"{self.unknown_0x4A} {self.unknown_0x4C} {self.unknown_0x4E} "
        
    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_float32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_float32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_float32(self.unknown_0x0C)
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_color32(self.unknown_0x14)
        self.unknown_0x18 = rw.rw_int32(self.unknown_0x18)
        self.unknown_0x1A = rw.rw_int16(self.unknown_0x1A)
        self.unknown_0x1C = rw.rw_int16(self.unknown_0x1C)
        self.unknown_0x20 = rw.rw_color32(self.unknown_0x20)
        self.unknown_0x24 = rw.rw_color32(self.unknown_0x24)
        self.unknown_0x28 = rw.rw_color32(self.unknown_0x28)
        self.unknown_0x2C = rw.rw_color32(self.unknown_0x2C)
        
        self.unknown_0x30 = rw.rw_uint32(self.unknown_0x30)
        self.unknown_0x34 = rw.rw_uint32(self.unknown_0x34)
        self.unknown_0x38 = rw.rw_uint32(self.unknown_0x38)
        self.unknown_0x3A = rw.rw_uint16(self.unknown_0x3A)
        self.unknown_0x3C = rw.rw_uint16(self.unknown_0x3C)
        
        self.unknown_0x40 = rw.rw_uint32(self.unknown_0x40)
        self.unknown_0x44 = rw.rw_uint32(self.unknown_0x44)
        self.unknown_0x48 = rw.rw_uint16(self.unknown_0x48)
        self.unknown_0x4A = rw.rw_uint16(self.unknown_0x4A)
        self.unknown_0x4C = rw.rw_uint16(self.unknown_0x4C)
        self.unknown_0x4E = rw.rw_uint16(self.unknown_0x4E)
        

class UnknownObject6(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.flags        = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        self.unknown_0x10 = None
        self.unknown_0x14 = None
        self.unknown_offset_1 = None
        self.unknown_offset_2 = None
        
    def __repr__(self):
        return f"[KSPR::UnkObj6] "\
            f"{self.unknown_0x00} {self.flags} {self.unknown_0x08} {self.unknown_0x0C} "\
            f"{self.unknown_0x10} {self.unknown_0x14} {self.unknown_offset_1} {self.unknown_offset_2} "
        
    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.flags        = rw.rw_bytestring(self.flags, 4)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
        self.unknown_0x10 = rw.rw_float32(self.unknown_0x10)
        self.unknown_0x14 = rw.rw_float32(self.unknown_0x14)
        self.unknown_offset_1 = rw.rw_pointer(self.unknown_offset_1)
        self.unknown_offset_2 = rw.rw_pointer(self.unknown_offset_2)
        
class UnknownObject6B(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        self.unknown_offset_1 = None
        self.unknown_offset_2 = None
        
    def __repr__(self):
        return f"[KSPR::UnknownObject6B] "\
            f"{self.unknown_0x00} {self.unknown_0x04} {self.unknown_0x08} {self.unknown_0x0C} {self.unknown_offset_1} {self.unknown_offset_2}"
        
    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        if self.unknown_0x04 > 0:
            self.unknown_offset_1 = rw.rw_pointer(self.unknown_offset_1)
            self.unknown_offset_2 = rw.rw_pointer(self.unknown_offset_2)
        else:
            self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
            self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
            
        if self.unknown_0x00 > 4:
            assert 0, self
                
class UnknownObject6BA(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        
    def __repr__(self):
        return f"[KSPR::UnknownObject6BA] "\
            f"{self.unknown_0x00} {self.unknown_0x04} {self.unknown_0x08} {self.unknown_0x0C}"
        
    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)

class UnknownObject6BB(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        
    def __repr__(self):
        return f"[KSPR::UnknownObject6BB] "\
            f"{self.unknown_0x00} {self.unknown_0x04} {self.unknown_0x08} {self.unknown_0x0C}"
        
    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
             
class UnknownObject7(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.unknown_0x00 = None
        self.unknown_0x04 = None
        self.unknown_0x08 = None
        self.unknown_0x0C = None
        
    def __repr__(self):
        return f"[KSPR::UnknownObject7] "\
            f"{self.unknown_0x00} {self.unknown_0x04} {self.unknown_0x08} {self.unknown_0x0C}"
        
    def read_write(self, rw):
        self.unknown_0x00 = rw.rw_uint32(self.unknown_0x00)
        self.unknown_0x04 = rw.rw_uint32(self.unknown_0x04)
        self.unknown_0x08 = rw.rw_uint32(self.unknown_0x08)
        self.unknown_0x0C = rw.rw_uint32(self.unknown_0x0C)
