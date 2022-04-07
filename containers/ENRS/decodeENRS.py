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
    

def decode_ENRS(num_groups, data):
    offset = 0
    offsets = []
    flat_offsets = []
    ENRS_iter_data = iter(data)
    for loop in range(num_groups):
        jump_from_previous_stencil_group = decompressInt(ENRS_iter_data)
        offset += jump_from_previous_stencil_group
        
        num_sub_stencils = decompressInt(ENRS_iter_data)
        stencil_size = decompressInt(ENRS_iter_data)
        stencil_repetitions = decompressInt(ENRS_iter_data)
        
        working_offset = offset
        sub_stencil_defs = []
        for j in range(num_sub_stencils):    
            sub_stencil_defs.append((*decompressSubStencilDef(ENRS_iter_data), decompressInt(ENRS_iter_data)))
            
        stencil_group = []
        for i in range(stencil_repetitions):
            saved_offset = working_offset + stencil_size
            stencil = []
            for j in range(num_sub_stencils):
                jump_from_previous_substencil, elem_byte_power, elem_count = sub_stencil_defs[j]
                working_offset += jump_from_previous_substencil

                    
                diff = 2 << elem_byte_power
                sub_stencil = ENRSSubStencil(diff)
                for k in range(elem_count):
                    flat_offsets.append(working_offset)
                    sub_stencil.data.append(working_offset)
                    working_offset += diff

                stencil.append(sub_stencil)
            stencil_group.append(stencil)
            working_offset = saved_offset
        offsets.append(stencil_group)
    return flat_offsets, offsets
