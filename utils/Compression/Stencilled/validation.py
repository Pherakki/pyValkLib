from pyValkLib.serialisation.Serializable import Context, Serializable

def flattenStencil(arr):
    return [elem for mainarr in arr for stencil in mainarr for substencil in stencil for elem in substencil]

def compareStencil(ctr_1, ctr_2, accessor, decompress, compress, build, to_packed_rep, print_errs=True):
    stencil_ctr = accessor(ctr_1)
    stencil_type = stencil_ctr.FILETYPE
    
    ptrs_1 = decompress(stencil_ctr.num_groups, stencil_ctr.data)
    ptrs_1 = ptrs_1.typed_flatten()
    ptrs_2 = to_packed_rep(build(ctr_2)).typed_flatten()
    
    if ptrs_1 != ptrs_2:
        for i, (c1, c2) in enumerate(zip(ptrs_1, ptrs_2)):
            if print_errs:
                print(f"> {stencil_type} COMPARISON", i, c1, "---", c2)
            
            if c1 != c2:
                print(f"{stencil_type} DID NOT MATCH: {i} {c1} --- {c2}")
                raise Exception()
        if len(ptrs_1) > len(ptrs_2):
            print("Input {stencil_type} HAS ADDITIONAL POINTERS:", ptrs_1[len(ptrs_2):])
            raise Exception()
        if len(ptrs_2) > len(ptrs_1):
            print("Output {stencil_type} HAS ADDITIONAL POINTERS:", ptrs_2[len(ptrs_1):])
            raise Exception()            

def validateStencil(pointers, nm, packed_rep_op, compress_op, decompress_op, print_errs=False):
    reference_ptrs = flattenStencil(pointers)
           
    for op_idx, op in enumerate([lambda x: x, 
                                 lambda x: x.to_abs_rep().to_unpacked_rep(),
                                 lambda x: x.to_abs_rep().to_rel_rep().to_abs_rep().to_unpacked_rep(),
                                 lambda x: decompress_op(len(pointers), compress_op(x))]):
        # Test if moving to structure works
        test_data = packed_rep_op(pointers)
        test_data = op(test_data)
        test_data = test_data.flatten()
        if test_data != reference_ptrs:
            for i, (c1, c2) in enumerate(zip(reference_ptrs, test_data)):
                if print_errs:
                    print("> {nm} TEST {op_idx+1}", i, c1, "---", c2)
                
                if c1 != c2:
                    print(f"{i} {c1} --- {c2}")
                    raise Exception()

class Validator(Serializable):
    def __init__(self, op):
        super().__init__(Context())
        self.op = op
        
    def read_write(self, rw):
        self.op()
