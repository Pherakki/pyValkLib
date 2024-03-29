import copy

from pyValkLib.serialisation.Serializable import Serializable
from pyValkLib.serialisation.ReadWriter import OffsetTracker


class PointerIndexableArray(Serializable):
    def __init__(self, context):
        super().__init__(context)
        #self.context.anchor_pos = context.anchor_pos
        #self.context.endianness = context.endianness
        
        self.data = []
        self.ptr_to_idx = {}
        self.idx_to_ptr = {}
        
    @classmethod
    def from_data(cls, context, data, offset, element_size=None):
        instance = cls(context)
        instance.data = copy.deepcopy(data)
        instance.ptr_to_idx = {offset + element_size*i : i for i in range(len(data))}
        instance.idx_to_ptr = {i : offset + element_size*i for i in range(len(data))}
        return instance
                
    @classmethod
    def from_placeholder_data(cls, context, ctor, count, offset, element_size=None):
        instance = cls(context)
        instance.data = [ctor() for _ in range(count)]
        instance.ptr_to_idx = {offset + element_size*i : i for i in range(count)}
        instance.idx_to_ptr = {i : offset + element_size*i for i in range(count)}
        return instance
    
    @classmethod
    def from_ragged_data(cls, context, data, offset, *args, **kwargs):
        instance = cls(context)
        instance.data = copy.deepcopy(data)
        ot = OffsetTracker()
        for i, d in enumerate(instance.data):
            new_offset = offset + ot.local_tell()
            instance.ptr_to_idx[new_offset] = i
            instance.idx_to_ptr[i] = new_offset
            ot.rw_obj(d, *args, **kwargs)
        return instance
    
    def at_ptr(self, ptr):
        return self.data[self.ptr_to_idx[ptr]]
    
    def at_idx(self, idx):
        return self.data[idx]

    def __getitem__(self, idx):
        return self.data[idx]

    def __iter__(self):
        for elem in self.data:
            yield elem
    
    def read_write(self, rw, *args, **kwargs):
        rw.mark_new_contents_array()
        for i, elem in enumerate(self.data):
            rw.mark_new_contents_array_member()
            if i in self.idx_to_ptr:
                rw.assert_local_file_pointer_now_at("Start of Array Entry", self.idx_to_ptr[i])
            curpos = rw.local_tell()
            self.ptr_to_idx[curpos] = i
            self.idx_to_ptr[i] = curpos

            self.rw_element(rw, i, *args, **kwargs)
            

    def rw_element(self, rw, idx, *args, **kwargs):
        rw.rw_obj(self.data[idx], *args, **kwargs)
        
    def rw_element_method(self, rw, func, idx):
        rw.rw_obj_method(self.data[idx], getattr(self.data[idx], func.__name__))
        
    def __len__(self):
        return len(self.data)
    
    def __repr__(self):
        return f"[Pointer Indexable Array]: {self.data}"
    
class PointerIndexableArrayInt8(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_int8(self.data[idx])
    
class PointerIndexableArrayUint8(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_uint8(self.data[idx])
    
class PointerIndexableArrayInt16(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_int16(self.data[idx])
    
class PointerIndexableArrayUint16(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_uint16(self.data[idx])
    
class PointerIndexableArrayInt32(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_int32(self.data[idx])
    
class PointerIndexableArrayUint32(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_uint32(self.data[idx])
    
class PointerIndexableArrayInt64(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_int64(self.data[idx])
    
class PointerIndexableArrayUint64(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_uint64(self.data[idx])
    
class PointerIndexableArrayFloat16(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_float16(self.data[idx])
    
class PointerIndexableArrayFloat32(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_float32(self.data[idx])
    
class PointerIndexableArrayFloat64(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_float64(self.data[idx])
    
class PointerIndexableArrayPointer(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_pointer(self.data[idx])
    
class PointerIndexableArrayMatrix4x4(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_matrix4x4(self.data[idx])
    
class PointerIndexableArrayVec32(PointerIndexableArray):
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_vec32(self.data[idx])
    
class PointerIndexableArrayCStr(PointerIndexableArray):
    def __init__(self, context, encoding='ascii'):
        super().__init__(context)
        self.encoding = encoding
        
    def rw_element(self, rw, idx): self.data[idx] = rw.rw_cstr(self.data[idx], encoding=self.encoding)
