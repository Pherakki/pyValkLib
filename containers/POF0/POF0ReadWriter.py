from pyValkLib.serialisation.ValkyriaBaseRW import ValkyriaBaseRW32BH


class POF0ReadWriter(ValkyriaBaseRW32BH):
    FILETYPE = "POF0"
    
    __slots__ = ("data_size", "data")
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        
        # Data holders
        self.data_size = None
        self.data = None
        
    def read_write_contents(self):
        self.assert_equal("flags", 0x10000000)
        self.rw_var("data_size", 'I', endianness='<')
        self.rw_vararray("data", 'B', (self.data_size - 4))
        self.cleanup_ragged_chunk(self.local_tell(), 16)

class POF0Handler:
    """
    The POF0 stores offsets of pointers within the container it is attached to.
    Specifically, each entry stores the number of bytes you need to skip to 
    find the next pointer.
    
    Consider a byte: 01000011
    The first two bits say how many bits the jump is encoded in:
    01 : 6 bits
    10 : 14 bits
    11 : 30 bits
    To get the offset:
    - Read that many more bits
    - Pad with two more bits on the left to make it a whole integer
    - Multiply by 4
    
    The minimum jump that can be stored is 4. The maximum is 2**32.
    This is fine, because VC file pointers are uint32, so they never are never
    located at an offset that is not a multiple of 4. Moreover, since the
    offsets can only store a maximum of 2**32 due to being uint32, the VC
    containers can never be more than 2**32 bytes long, and therefore the
    offsets themselves will never have a value more than 2**32 bytes. This
    compression scheme therefore completely matches the range of the pointers.
    
    Example 1. 01000011 -> +68
    Example 2. Conside a POF0 with three bytes: 01000001, 01000001, 01000010 
    These decode to the jumps (+4, +4, +8)
    This means that the data at 0x04, 0x08, and 0x10 within the container
    the POF0 is attached to are pointers.
    """
    __slots__ = ("pointer_offsets", "containers", "endianness")
    
    def __init__(self, containers, endianness):
        self.pointer_offsets = []
        self.containers = containers
        self.endianness = endianness
        
    def read(self, bytestream):
        pof0_rw = POF0ReadWriter(self.containers, self.endianness)
        pof0_rw.read(self.bytestream)
        
        num_bytes = pof0_rw.data_size - 4
        POF0_data = pof0_rw.data
        
        self.pointer_offsets = decode_POF0(POF0_data, num_bytes)

    
    def write(self, bytestream):
        POF0_data = encode_POF0(self.pointer_offsets)
        
        pof0_rw = POF0ReadWriter(self.containers, self.endianness)
        pof0_rw.data = POF0_data
        pof0_rw.data_size = len(POF0_data) + 4
        pof0_rw.write()
        
def decode_POF0(POF0_data, num_offsets):
    offset = 0
    offsets = []  
    data = iter(POF0_data)

    bytes_to_parse = iter(range(num_offsets))
    for loop in bytes_to_parse:
        elem = next(data)
        power_val = elem & 0xC0
        value = elem & 0x3F
        if power_val == 0x40:
            offset += 4*value
            offsets.append(offset)
        elif power_val == 0x80:
            offset_incr = 4*(value << 8 | next(data))
            offset += offset_incr
            next(bytes_to_parse)
            offsets.append(offset)
        elif power_val == 0xC0:
            offset_incr = 4*(value << 0x18 | next(data) << 0x10 | next(data) << 0x08 | next(data))
            offset += offset_incr
            offsets.append(offset)
            next(bytes_to_parse)
            next(bytes_to_parse)
            next(bytes_to_parse)
        else:
            continue
    return offsets
        
def encode_POF0(offsets):
    data = []
    previous_offset = 0
    for offset in offsets:
        diff = offset - previous_offset
        assert offset & 0x03 == 0, f"Offset is not a multiple of 4! {offset}"
        if diff < 2**8:
            power_val = 0x40
            byte_1 = diff >> 2
            
            data.append(power_val | byte_1)
        elif diff < 2**16:
            power_val = 0x80
            element_data = diff >> 2
            
            byte_1 = (element_data & 0xFF00) >> 0x08
            byte_2 = (element_data & 0x00FF) >> 0x00
            data.append(power_val | byte_1)
            data.append(byte_2)
        elif diff < 2**32:
            power_val = 0xC0
            element_data = diff >> 2
            
            byte_1 = (element_data & 0xFF000000) >> 0x18
            byte_2 = (element_data & 0x00FF0000) >> 0x10
            byte_3 = (element_data & 0x0000FF00) >> 0x08
            byte_4 = (element_data & 0x000000FF) >> 0x00
            data.append(power_val | byte_1)
            data.append(byte_2)
            data.append(byte_3)
            data.append(byte_4)
        
        else:
            raise ValueError(f"Offset differences can be no larger than 2**32: {previous_offset} {offset} {diff}.")
        previous_offset = offset
    return data
