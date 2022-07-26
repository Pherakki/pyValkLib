from .Representations import CCRSRelRep, CCRSRelativeTemplateGenerator, CCRSTemplateComponent

from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH


class CCRSReadWriter(ValkSerializable32BH):
    FILETYPE = "CCRS"
    
    __slots__ = ("padding_0x20", "num_groups", "data")
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        
        # Data holders
        self.padding_0x20 = 0
        self.num_groups = None
        self.data = None
        
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x10000000, lambda x: hex(x))
        self.padding_0x20 = rw.rw_uint32(self.padding_0x20)
        self.num_groups   = rw.rw_uint32(self.num_groups)
        rw.align(rw.local_tell(), 0x10)
        
        rw.assert_is_zero(self.padding_0x20)
        self.data = rw.rw_uint8s(self.data, self.header.data_length - 0x10, endianness='<')
        
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


def decompressCCRS(num_groups, data):
    offset = 0
    offsets = []
    
    CCRS_iter_data = iter(data)
    for loop in range(num_groups):
        # Decode the CCRS spec
        jump_from_previous_stencil_group = decompressInt(CCRS_iter_data)
        offset += jump_from_previous_stencil_group
        
        num_sub_stencils = decompressInt(CCRS_iter_data)
        stencil_size = decompressInt(CCRS_iter_data)
        stencil_repetitions = decompressInt(CCRS_iter_data)
        working_offset = offset
        sub_stencil_defs = []
        for j in range(num_sub_stencils):
            sub_stencil_defs.append([decompressInt(CCRS_iter_data), 
                                     decompressInt(CCRS_iter_data), 
                                     decompressInt(CCRS_iter_data)])
        # Generate Offsets
        working_offset = offset
        stencil_group = []
        for i in range(stencil_repetitions):
            saved_offset = working_offset + stencil_size
            stencil = []
            for j in range(num_sub_stencils):
                array_loop_skip, array_count, bytecode = sub_stencil_defs[j]
                working_offset += array_loop_skip
                
                
                sub_stencil = []
                if bytecode == 0:
                    for k in range(array_count):
                        sub_stencil.append((working_offset, 0))
                        working_offset += 0x10
                elif bytecode == 1:
                    for k in range(array_count):
                        sub_stencil.append((working_offset, 1))
                        working_offset += 4
                elif bytecode == 2:
                    for k in range(array_count):
                        sub_stencil.append((working_offset, 2))
                        working_offset += 2
                elif bytecode == 3:
                    for k in range(array_count):
                        sub_stencil.append((working_offset, 3))
                        working_offset += 2
                elif bytecode == 4:
                    for k in range(array_count):
                        sub_stencil.append((working_offset, 4))
                        working_offset += 2
                elif bytecode == 5:
                    for k in range(array_count):
                        sub_stencil.append((working_offset, 5))
                        working_offset += 2
                elif bytecode > 5:
                    assert 0, f"Bytecode > 5, {array_count}"
                    
                stencil.append(sub_stencil)
                
            working_offset = saved_offset
            stencil_group.append(stencil)
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

# Refactor with classes to make it more obvious what's going on
# Need to find a consistent nomenclature first...
def compressCCRS(pointer_offsets):
    data = []
    prev_main_array_offset = 0
    for idx, main_array in enumerate(pointer_offsets):
        stencil = main_array[0]
        
        first_offset = main_array[0][0][0][0]
        num_array_member_copies = len(main_array)
        num_sub_stencils = len(main_array[0])
        
        # Calculate the jump between stencils
        if idx+1 == len(pointer_offsets):
            if len(stencil) > 2:
                stencil_size = stencil[1][0][0] - stencil[0][0][0]
            else:
                stencil_size = 1
        else:
            offset_to_next_stencil_group = pointer_offsets[idx+1][0][0][0][0] - stencil[0][0][0]
            stencil_size = offset_to_next_stencil_group // len(main_array)
        
        data.extend(compressInt(first_offset - prev_main_array_offset))
        data.extend(compressInt(num_sub_stencils))
        data.extend(compressInt(stencil_size))
        data.extend(compressInt(num_array_member_copies))
        
        prev_main_array_offset = first_offset
        
        previous_substencil_offset = stencil[0][0][0]
        for j, sub_stencil in enumerate(stencil):
            starting_offset = sub_stencil[0][0] - previous_substencil_offset
            
            sub_stencil_count = len(sub_stencil)
            
            data.extend(compressInt(starting_offset - previous_substencil_offset))
            data.extend(compressInt(sub_stencil_count))
            data.extend(compressInt(sub_stencil[0][1]))
            
            previous_substencil_offset = sub_stencil[0][0]

    return data
