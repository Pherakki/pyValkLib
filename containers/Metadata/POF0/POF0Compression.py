from pyValkLib.serialisation.ReadWriter import POF0Builder
from pyValkLib.utils.Compression.Stencilled.validation import Validator

def pull_bytecode(POF0_iter, byte_power, bytecode_value):
    for _ in range((1 << byte_power) - 1):
        elem = next(POF0_iter)
        bytecode_value <<= 8
        bytecode_value |= elem
        
    return bytecode_value

def decompressInt(POF0_iter):
    elem = next(POF0_iter)
    byte_power = elem >> 6
    bytecode_value = elem & 0x3F
    
    return pull_bytecode(POF0_iter, byte_power, bytecode_value)

def decompressPOF0(data):
    offset = 0
    offsets = []  
    data = iter(data)

    for elem in data:
        power_val = elem & 0xC0
        value = elem & 0x3F
        if power_val == 0x40:
            offset += 4*value
            offsets.append(offset)
        elif power_val == 0x80:
            offset_incr = 4*(value << 8 | next(data))
            offset += offset_incr
            offsets.append(offset)
        elif power_val == 0xC0:
            offset_incr = 4*(value << 0x18 | next(data) << 0x10 | next(data) << 0x08 | next(data))
            offset += offset_incr
            offsets.append(offset)
        else:
            continue
    return offsets

def decompressPOF0_alt_alt(data):
    offset = 0
    offsets = []  
    data = iter(data)

    for elem in data:
        bit_power = (elem & 0xC0) >> 6
        if bit_power == 0:
            continue
        bitwidth = 1 << (bit_power - 1)
        value = elem & 0x3F
        for _ in range(bitwidth - 1):
            value << 8
            value |= next(data)
            
        offset = 4*value
        offsets.append(offset)

    return offsets

def compressPOF0(offsets):
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


##############
# VALIDATION #
##############

def buildPOF0(ctr):
    pb = POF0Builder()
    pb.virtual_offset = ctr.header.header_length
    ctr.read_write_contents(pb)
    
    return pb.pointers

def comparePOF0(ctr_1, ctr_2, print_errs=True):
    pof0_1 = decompressPOF0(ctr_1.POF0.data)
    pof0_2 = buildPOF0(ctr_2)
    
    if pof0_1 != pof0_2:
        for i, (c1, c2) in enumerate(zip(pof0_1, pof0_2)):
            if print_errs:
                print("> POF0 COMPARISON", i, c1, "---", c2)
            
            if c1 != c2:
                print(f"POF0 DID NOT MATCH: {i} {c1} --- {c2}")
                raise Exception()
        if len(pof0_1) > len(pof0_2):
            print("Input POF0 HAS ADDITIONAL POINTERS:", pof0_1[len(pof0_2):])
            raise Exception()
        if len(pof0_2) > len(pof0_1):
            print("Output POF0 HAS ADDITIONAL POINTERS:", pof0_2[len(pof0_1):])
            raise Exception()

class POF0Validator(Validator):
    FILETYPE="POF0VALIDATOR"
    
    def __init__(self, ctr, print_errs=True):
        super().__init__(lambda: comparePOF0(ctr, ctr, print_errs))
    