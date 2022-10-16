from pyValkLib.serialisation.ValkSerializable import Serializable, ValkSerializable32BH
from pyValkLib.containers.Metadata.ENRS.ENRSReadWriter import ENRSReadWriter
from pyValkLib.containers.Metadata.EOFC.EOFCReadWriter import EOFCReadWriter

class KFSGReadWriter(ValkSerializable32BH):
    FILETYPE = "KFSG"
    
    def __init__(self, KFSS_ref, endianness=None):
        super().__init__({}, endianness)
        self.header.flags = 0x18000000
        
        self.vertices = []
        self.KFSS_ref = KFSS_ref
        
        self.ENRS = ENRSReadWriter("<")
        self.EOFC = EOFCReadWriter("<")

    def get_subcontainers(self):
        return [self.ENRS, self.EOFC]
    
    def __repr__(self):
        return f"KFSG Object [{self.header.depth}] [0x{self.header.flags:0>8x}]. Contains ENRS."    
        
    def read_write_contents(self, rw):
        rw.mark_new_contents_array()
        rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))
        
        mesh_def = self.KFSS_ref.mesh_defs[0]
        vsize    = mesh_def.vertex_size
        vcount   = mesh_def.vertex_count
        
        if vsize == 0x14:
            vformat = Vertex0x14
        elif vsize == 0x0C:
            vformat = Vertex0x0C
        else:
            raise NotImplementedError(f"Vertex Size {vsize} not implemented.")
            
        self.vertices = rw.rw_obj_array(self.vertices, lambda: vformat(self.context), vcount)
        rw.mark_new_contents_array()
        rw.align(rw.local_tell(), 0x10)
    
class Vertex0x0C(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.position_shift = []
        
    def __repr__(self):
        return f"[KFSG::Vertex0x0C] {self.position_shift}"
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        self.position_shift = rw.rw_float32s(self.position_shift, 3)
        
class Vertex0x14(Serializable):
    def __init__(self, context):
        super().__init__(context)
        
        self.position_shift = []
        self.normal_shift = []
        
    def __repr__(self):
        return f"[KFSG::Vertex0x14] {self.position_shift} {self.normal_shift}"
        
    def read_write(self, rw):
        rw.mark_new_contents_array_member()
        self.position_shift = rw.rw_float32s(self.position_shift, 3)
        self.normal_shift = rw.rw_float16s(self.normal_shift, 4)
