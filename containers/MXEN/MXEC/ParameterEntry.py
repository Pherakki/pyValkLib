import json
import os
from pyValkLib.serialisation.Serializable import Serializable
from pyValkLib.containers.MXEN.MXEC.StructureList import data_types


param_structs = {}
struct_path = os.path.abspath("pyValkLib/configuration/MXE/Parameters")
for file in os.listdir(struct_path):
    filename, fileext = os.path.splitext(file)
    if fileext == ".json":
        filepath = os.path.join(struct_path, file)
        with open(filepath, 'r') as F:
            param_structs[filename] = json.load(F)      

def handle_pad(rw, x, func):
    val = func(x)
    rw.assert_is_zero(val)
    return val

func_lookup = {
    "int8"       : lambda rw, x, en: rw.rw_int8(x, endianness=en),
    "int16"      : lambda rw, x, en: rw.rw_int16(x, endianness=en),
    "int32"      : lambda rw, x, en: rw.rw_int32(x, endianness=en),
    "int64"      : lambda rw, x, en: rw.rw_int64(x, endianness=en),  
    "uint8"      : lambda rw, x, en: rw.rw_uint8(x, endianness=en),
    "uint16"     : lambda rw, x, en: rw.rw_uint16(x, endianness=en),
    "uint32"     : lambda rw, x, en: rw.rw_uint32(x, endianness=en),
    "uint64"     : lambda rw, x, en: rw.rw_uint64(x, endianness=en),
    "float16"    : lambda rw, x, en: rw.rw_float16(x, endianness=en),
    "float32"    : lambda rw, x, en: rw.rw_float32(x, endianness=en),
    "float64"    : lambda rw, x, en: rw.rw_float64(x, endianness=en),
    "pad32"      : lambda rw, x, en: handle_pad(rw, x, rw.rw_pad32),
    "pad64"      : lambda rw, x, en: handle_pad(rw, x, rw.rw_pad64),
    "asset"      : lambda rw, x, en: rw.rw_int64(x, endianness=en),
    "pointer32"  : lambda rw, x, en: rw.rw_uint32(x, endianness=en),
    "utf8_string": lambda rw, x, en: rw.rw_uint32(x, endianness=en),
    "sjis_string": lambda rw, x, en: rw.rw_uint32(x, endianness=en)
}

class ParameterSet(Serializable):
    def __init__(self, context, struct_type):
        super().__init__(context)
        self.struct_type = struct_type
        self.data = {}
        self.datatypes = []
        self.sjis_vars = []
        self.utf8_vars = []
        self.asset_vars = []
        
        for k, v in param_structs[struct_type].items():
            self.data[k] = None
            self.datatypes.append(v)
            
            if type(v) is str:
                if v[1:] == "utf8_string":
                    self.utf8_vars.append(k)
                elif v[1:] == "sjis_string":
                    self.sjis_vars.append(k)
                elif v[1:] == "asset":
                    self.asset_vars.append(k)
        
    def read_write(self, rw):
        for k, ktype in zip(self.data, self.datatypes):
            # Handle a regular type
            if type(ktype) is str:
                try:
                    self.data[k] = func_lookup[ktype[1:]](rw, self.data[k], ktype[0])
                except Exception as e:
                    print("Failed to handle", k, "for", self.struct_type)
                    raise e
            # Handle subparameters
            elif type(ktype) is dict:
                count = self.data[ktype["count"]]
                ptr = self.data[ktype["pointer"]]
                if rw.mode() == "read":
                    self.data[k] = [ParameterSet(self.context, ktype["type"]) for _ in range(count)]
                    
                rw.assert_local_file_pointer_now_at(f"{ktype['type']} Member {k}", ptr)
                for param in self.data[k]:
                    rw.rw_obj(param)
                

    def asset_table_offsets(self):
        return [self.data[k] for k in self.asset_vars]
    
    def get_string_ptrs(self):
        return [self.data[k] for k in self.utf8_vars]
    
    def get_shiftjis_string_ptrs(self):
        return [self.data[k] for k in self.sjis_vars]

class ParameterEntry(Serializable):
    __slots__ = ("name", "ID", "name_offset", "data_size", "data_offset", "parameter_type", "data")

    def __init__(self, context):
        super().__init__(context)
        self.ID = 0
        self.name_offset = 0
        self.data_size = 0
        self.data_offset = 0
        
        self.parameter_type = None
        
        self.data = None
        
    def read_write(self, rw):
        self.ID          = rw.rw_uint32(self.ID)
        self.name_offset = rw.rw_pointer(self.name_offset)
        self.data_size   = rw.rw_uint32(self.data_size)
        self.data_offset = rw.rw_pointer(self.data_offset)
        
    def rw_data(self, rw, lookup_name):
        if rw.mode() == "read":
            self.data = ParameterSet(self.context, lookup_name)
        rw.rw_obj(self.data)
        rw.align(rw.local_tell(), 0x10)
