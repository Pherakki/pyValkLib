import array

from pyValkLib.serialisation import Serializable
from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH, Header32B


class ENRSReadWriter(ValkSerializable32BH):
    FILETYPE = "ENRS"
    
    __slots__ = ("padding_0x20", "num_groups", "data")
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        self.padding_0x20 = None
        self.num_groups = None
        self.data = []
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x : hex(x))
        
        self.padding_0x20 = rw.rw_uint32(self.padding_0x20, endianness='<')
        self.num_groups   = rw.rw_uint32(self.num_groups, endianness='<')
        rw.align(rw.local_tell(), 0x10)
        rw.assert_equal(self.padding_0x20, 0)
        
        self.data = rw.rw_uint8s(self.data, self.header.data_length - 0x10)


class ENRSHandler(Serializable):
    __slots__ = ("header", "pointer_offsets", "containers", "endianness")
    
    def __init__(self, containers, context):
        super().__init__(context)
        self.header = Header32B(context)
        self.pointer_offsets = []
        self.containers = containers

    def read_write(self, rw):
        if (rw.mode() == "read"):
            self.do_read(rw)
        elif (rw.mode() == "write"):
            self.do_write(rw)
        else:
            raise Exception("Unknown mode!")

    def do_read(self, rw):
        enrs_rw = ENRSReadWriter(self.containers, self.context.endianness)
        rw.rw_obj(enrs_rw)
        self.header = enrs_rw.header
        
        self.pointer_offsets = decompressENRS(enrs_rw.num_groups, enrs_rw.data)

    def do_write(self, rw):
        ENRS_data = compressENRS(self.pointer_offsets)
        
        enrs_rw = ENRSReadWriter(self.containers, self.context.endianness)
        enrs_rw.header = self.header
        enrs_rw.padding_0x20 = 0
        enrs_rw.ptr_count = len(self.pointer_offsets)
        enrs_rw.data = compressENRS(ENRS_data)
        rw.rw_obj(enrs_rw)
        
#################
# DECOMPRESSION #
#################
def pull_bytecode(ENRS_iter, byte_power, bytecode_value):
    for _ in range((1 << byte_power) - 1):
        elem = next(ENRS_iter)
        bytecode_value <<= 8
        bytecode_value |= elem
        
    return bytecode_value

def decompressInt(ENRS_iter):
    elem = next(ENRS_iter)
    byte_power = elem >> 6
    bytecode_value = elem & 0x3F
    
    return pull_bytecode(ENRS_iter, byte_power, bytecode_value)


def decompressSubStencilDef(ENRS_iter):
    elem = next(ENRS_iter)
    byte_power = elem >> 6
    bytecode_value = elem & 0xF
    array_byte_power = elem >> 4 & 3
    
    return pull_bytecode(ENRS_iter, byte_power, bytecode_value), array_byte_power

def pull_bytecode_Bytes(ENRS_iter, byte_power, bytecode_value):
    out = []
    for _ in range((1 << byte_power) - 1):
        out.append(next(ENRS_iter))
        
    return out

def decompressInt_Bytes(ENRS_iter):
    elem = next(ENRS_iter)
    byte_power = elem >> 6
    bytecode_value = elem & 0x3F
    
    return [elem, *pull_bytecode_Bytes(ENRS_iter, byte_power, bytecode_value)]


def decompressSubStencilDef_Bytes(ENRS_iter):
    elem = next(ENRS_iter)
    byte_power = elem >> 6
    bytecode_value = elem & 0xF
    
    return [elem, *pull_bytecode_Bytes(ENRS_iter, byte_power, bytecode_value)]


type_lookup = {2: "H",
               4: "I",
               8: "Q"}

def decompressENRS(num_groups, data):
    offset = 0
    offsets = []
    
    ENRS_iter_data = iter(data)
    for loop in range(num_groups):
        # Decode the ENRS spec
        jump_from_previous_stencil_group = decompressInt(ENRS_iter_data)
        offset += jump_from_previous_stencil_group
        
        num_sub_stencils = decompressInt(ENRS_iter_data)
        stencil_size = decompressInt(ENRS_iter_data)
        stencil_repetitions = decompressInt(ENRS_iter_data)
        working_offset = offset
        sub_stencil_defs = []
        for j in range(num_sub_stencils):    
            sub_stencil_defs.append((*decompressSubStencilDef(ENRS_iter_data), decompressInt(ENRS_iter_data)))
            
        # Generate offsets
        stencil_group = []
        for i in range(stencil_repetitions):
            saved_offset = working_offset + stencil_size
            stencil = []
            for j in range(num_sub_stencils):
                jump_from_previous_substencil, elem_byte_power, elem_count = sub_stencil_defs[j]
                working_offset += jump_from_previous_substencil

                    
                diff = 2 << elem_byte_power
                sub_stencil = []
                for k in range(elem_count):
                    sub_stencil.append(working_offset)
                    working_offset += diff

                sub_stencil = array.array(type_lookup[diff], sub_stencil)
                stencil.append(sub_stencil)
            stencil_group.append(stencil)
            working_offset = saved_offset
        offsets.append(stencil_group)
        
    return offsets

def divideENRSBytes(num_groups, data):
    bytes_out = []
    
    ENRS_iter_data = iter(data)
    for loop in range(num_groups):
        hdr = []
        # Decode the ENRS spec
        hdr.extend(decompressInt_Bytes(ENRS_iter_data))
        
        num_sub_stencils_bytes = decompressInt_Bytes(ENRS_iter_data)
        num_sub_stencils = decompressInt(iter(num_sub_stencils_bytes))
        hdr.extend(num_sub_stencils_bytes)
        hdr.extend(decompressInt_Bytes(ENRS_iter_data))
        hdr.extend(decompressInt_Bytes(ENRS_iter_data))

        subs = []
        for j in range(num_sub_stencils):    
            subs.append([*decompressSubStencilDef_Bytes(ENRS_iter_data), decompressInt_Bytes(ENRS_iter_data)])

        bytes_out.append([hdr, subs])

    return bytes_out


def compressInt(integer):
    data = []
    if integer < 2**6:
        power_val = 0x00
        
        byte_1 = (integer & 0x3F) >> 0x00
        
        data.append(power_val | byte_1)
    elif integer < 2**14:
        power_val = 0x40
        
        byte_1 = (integer & 0x3F00) >> 0x08
        byte_2 = (integer & 0x00FF) >> 0x00
        
        data.append(power_val | byte_1)
        data.append(byte_2)
    elif integer < 2**30:
        power_val = 0x80
        
        byte_1 = (integer & 0x3F000000) >> 0x18
        byte_2 = (integer & 0x00FF0000) >> 0x10
        byte_3 = (integer & 0x0000FF00) >> 0x08
        byte_4 = (integer & 0x000000FF) >> 0x00
        
        data.append(power_val | byte_1)
        data.append(byte_2)
        data.append(byte_3)
        data.append(byte_4)
    else:
        raise ValueError(f"Int can be no larger than 2**30: {integer}.")
    return data

def compressSubStencil(starting_offset, diff):
    data = []
    elem_byte_power = diff << 2
    if starting_offset < 2**4:
        power_val = 0x00
        
        byte_1 = (starting_offset & 0x0F) >> 0x00
        
        data.append(power_val | elem_byte_power | byte_1)
    elif starting_offset < 2**12:
        power_val = 0x40
        
        byte_1 = (starting_offset & 0x0F00) >> 0x08
        byte_2 = (starting_offset & 0x00FF) >> 0x00
        
        data.append(power_val | elem_byte_power | byte_1)
        data.append(byte_2)
    elif starting_offset < 2**28:
        power_val = 0x80
        
        byte_1 = (starting_offset & 0x0F000000) >> 0x18
        byte_2 = (starting_offset & 0x00FF0000) >> 0x10
        byte_3 = (starting_offset & 0x0000FF00) >> 0x08
        byte_4 = (starting_offset & 0x000000FF) >> 0x00
        
        data.append(power_val | elem_byte_power | byte_1)
        data.append(byte_2)
        data.append(byte_3)
        data.append(byte_4)
    else:
        raise ValueError(f"Offset can be no larger than 2**28: {diff}.")
    return data


###############
# COMPRESSION #
###############    
def compressENRS(pointer_offsets):
    data = []
    prev_main_array_offset = 0
    for idx, main_array in enumerate(pointer_offsets):
        stencil = main_array[0]
        
        first_offset = main_array[0][0][0]
        num_array_member_copies = len(main_array)
        num_sub_stencils = len(main_array[0])
        
        # Calculate the jump between stencils
        # Surely this can be simplified?
        if idx+1 == len(pointer_offsets):
            if len(main_array) == 1 and len(main_array[0]) == 1 and len(main_array[0][0]) == 1:
                 stencil_size = 1
            elif len(stencil) > 2:
                stencil_size = stencil[1][0] - stencil[0][0]
            else:
                stencil_size = stencil[0].itemsize
        else:
            print(idx)
            print(len(main_array))
            print(len(main_array[0]))
            print(len(main_array[0][0]))
            is_contiguous = pointer_offsets[idx+1][0][0][0] == (main_array[-1][-1][-1] + main_array[-1][-1].itemsize)
            if len(main_array) == 1 and len(main_array[0]) == 1 and is_contiguous:
                 stencil_size = 1
            else:
                offset_to_next_stencil_group = pointer_offsets[idx+1][0][0][0] - stencil[0][0]
                stencil_size = offset_to_next_stencil_group // len(main_array)
            print("Stencil size:", stencil_size)
        
        data.extend(compressInt(first_offset - prev_main_array_offset))
        data.extend(compressInt(num_sub_stencils))
        data.extend(compressInt(stencil_size))
        data.extend(compressInt(num_array_member_copies))
        
        prev_main_array_offset = first_offset
        
        previous_substencil_offset = stencil[0][0]
        for j, sub_stencil in enumerate(stencil):
            starting_offset = sub_stencil[0] - previous_substencil_offset
            diff = sub_stencil.itemsize
            
            sub_stencil_count = len(sub_stencil)
            
            data.extend(compressSubStencil(starting_offset, diff))
            data.extend(compressInt(sub_stencil_count))
            
            previous_substencil_offset = sub_stencil[0]

    return data
