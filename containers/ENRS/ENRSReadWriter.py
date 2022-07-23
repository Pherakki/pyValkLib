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

type_lookup = {2: "H",
               4: "I",
               8: "Q"}

def decompressENRS(num_groups, data):
    offset = 0
    offsets = []
    stencil_sizes = []
    
    ENRS_iter_data = iter(data)
    for loop in range(num_groups):
        # Decode the ENRS spec
        jump_from_previous_stencil_group = decompressInt(ENRS_iter_data)
        offset += jump_from_previous_stencil_group
        
        num_sub_stencils = decompressInt(ENRS_iter_data)
        stencil_size = decompressInt(ENRS_iter_data)
        stencil_repetitions = decompressInt(ENRS_iter_data)
        stencil_sizes.append(stencil_size)
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
    print("<<< COMPRESS >>>")
    data = []
    prev_offset = 0
    prev_first_stencil_start = 0
    for i, stencil_group in enumerate(pointer_offsets):
        stencil_repetitions = len(stencil_group)
        stencil = stencil_group[0]

        if print_groups and not skip_groups:
            print("####")
            print("IDX", i)
            print("OFFSET COMP", i+1, len(pointer_offsets))
            
        jump_from_previous_stencil_group = stencil[0].data[0] - prev_first_stencil_start
        num_sub_stencils = len(stencil)
        
        if i+1 == len(pointer_offsets):
            if len(stencil) > 2:
                stencil_size = stencil[1].data[0] - stencil[0].data[0]
            else:
                stencil_size = stencil[0].dsize
        else:
            jump_to_next_group = pointer_offsets[i+1][0][0].data[0] - stencil_group[-1][-1].data[-1]
            if print_groups and not skip_groups:
                print("THIS STENCIL GROUP", [[substencil.data for substencil in stencil] for stencil in stencil_group])
                print("NEXT STENCIL GROUP", [[substencil.data for substencil in stencil] for stencil in pointer_offsets[i+1]])
                print("OFFSET TO NEXT GROUP", jump_to_next_group)
                print("STENCIL REPETITIONS", stencil_repetitions)
                print("NUM DATA ELEMENTS", len(stencil[0].data))
                print(">>COMP", pointer_offsets[i+1][0][0].data[0], stencil[-1].data[-1], jump_to_next_group, stencil[0].dsize)
            if len(stencil_group) == 1 and  jump_to_next_group == stencil[0].dsize:
                stencil_size = 1
            else:
                offset_to_next_stencil_group = pointer_offsets[i+1][0][0].data[0] - stencil[0].data[0]
                stencil_size = offset_to_next_stencil_group // len(stencil_group)
        
        data.extend(compressInt(jump_from_previous_stencil_group))
        data.extend(compressInt(num_sub_stencils))
        data.extend(compressInt(stencil_size))
        data.extend(compressInt(stencil_repetitions))
        
        if print_groups and not skip_groups:
            print(jump_from_previous_stencil_group, compressInt(jump_from_previous_stencil_group))
            print(num_sub_stencils, compressInt(num_sub_stencils))
            print(stencil_size, compressInt(stencil_size))
            print(stencil_repetitions, compressInt(stencil_repetitions))

        
        previous_substencil_offset = stencil[0].data[0]
        for j, sub_stencil in enumerate(stencil):
            starting_offset = sub_stencil.data[0] - previous_substencil_offset
            diff = sub_stencil.dsize
            
            sub_stencil_count = len(sub_stencil.data)
            
            data.extend(compressSubStencil(starting_offset, diff))
            data.extend(compressInt(sub_stencil_count))
            
            previous_substencil_offset = sub_stencil.data[0]
            
            if print_groups and not skip_groups:
                print(">>>")
                print(starting_offset, diff, compressSubStencil(starting_offset, diff))
                print(sub_stencil_count, compressInt(sub_stencil_count))
                print(len(data))
            
        prev_first_stencil_start = stencil[0].data[0]
        
        if print_groups:
            print_groups.pop()
        if skip_groups:
            skip_groups.pop()
        
    return data

