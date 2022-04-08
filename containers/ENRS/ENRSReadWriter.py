from pyValkLib.serialisation.ValkyriaBaseRW import ValkyriaBaseRW32BH


class ENRSReadWriter(ValkyriaBaseRW32BH):
    FILETYPE = "ENRS"
    
    __slots__ = ("num_groups", "data")
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)

    
    def read_write_contents(self):
        self.assert_equal("flags", 0x10000000, self.header, lambda x : hex(x))
        
        self.rw_var("padding_0x20", "I", endianness='<')
        self.rw_var("num_groups", "I", endianness='<')
        self.cleanup_ragged_chunk(self.local_tell(), 0x10)
        self.assert_equal("padding_0x20", 0)
        
        self.rw_varlist('data', 'B', self.header.data_length - 0x10)

class ENRSHandler:
    __slots__ = ("pointer_offsets", "containers", "endianness")
    
    def __init__(self, containers, endianness):
        self.pointer_offsets = []
        self.containers = containers
        self.endianness = endianness
        
    def read(self, bytestream):
        enrs_rw = ENRSReadWriter(self.containers, self.endianness)
        enrs_rw.read(bytestream)
        
        self.pointer_offsets = decompressENRS(enrs_rw.num_groups, enrs_rw.data)

    
    def write(self, bytestream):
        ENRS_data = compressENRS(self.pointer_offsets)
        
        enrs_rw = ENRSReadWriter(self.containers, self.endianness)
        enrs_rw.padding_0x20 = 0
        enrs_rw.ptr_count = len(self.pointer_offsets)
        enrs_rw.data = compressENRS(ENRS_data)
        enrs_rw.write(bytestream)
        
#################
# DECOMPRESSION #
#################
def pull_bytecode(ENRS_iter, byte_power, bytecode_value):
    if byte_power == 0:
        return bytecode_value
    if byte_power == 1:
        return (bytecode_value << 8) | next(ENRS_iter)
    elif byte_power == 2:
        return (bytecode_value << 8 | next(ENRS_iter)) << 0x10 | next(ENRS_iter) << 8 | next(ENRS_iter)
    else:
        assert 0

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

class ENRSSubStencil:
    __slots__ = ("data", "dsize")
    def __init__(self, dsize):
        self.data = []
        self.dsize = dsize
    

skip_groups = list(range(0))
print_groups = list(range(0))
def decompressENRS(num_groups, data):
    offset = 0
    offsets = []
    flat_offsets = []
    stencil_sizes = []
    ENRS_iter_data = iter(data)
    print("<<< DECOMPRESS >>>")
    for loop in range(num_groups):
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
            
        if print_groups and not skip_groups:
            print("####")
            print(jump_from_previous_stencil_group)
            print(num_sub_stencils)
            print(stencil_size)
            print(stencil_repetitions)
            
        stencil_group = []
        for i in range(stencil_repetitions):
            saved_offset = working_offset + stencil_size
            stencil = []
            for j in range(num_sub_stencils):
                jump_from_previous_substencil, elem_byte_power, elem_count = sub_stencil_defs[j]
                working_offset += jump_from_previous_substencil

                    
                diff = 2 << elem_byte_power
                sub_stencil = ENRSSubStencil(diff)
                if print_groups and not skip_groups:
                    print(">>>")
                    print(jump_from_previous_substencil, diff)
                    print(elem_count)
                for k in range(elem_count):
                    flat_offsets.append(working_offset)
                    sub_stencil.data.append(working_offset)
                    working_offset += diff

                stencil.append(sub_stencil)
            stencil_group.append(stencil)
            working_offset = saved_offset
        offsets.append(stencil_group)
        
        if print_groups:
            print_groups.pop()
        if skip_groups:
            skip_groups.pop()
        
    return flat_offsets, offsets, stencil_sizes


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

