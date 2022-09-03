from pyValkLib.serialisation.Serializable import Serializable

class StructureNodeFCurves(Serializable):
    def __init__(self, context, flags):
        super().__init__(context)
        
        self.flags = flags
        
        self.pos_x_offset   = 0
        self.pos_y_offset   = 0
        self.pos_z_offset   = 0
        self.pos_w_offset   = 0
        
        self.rot_x_offset   = 0
        self.rot_y_offset   = 0
        self.rot_z_offset   = 0
        self.rot_w_offset   = 0
        
        self.scale_x_offset = 0
        self.scale_y_offset = 0
        self.scale_z_offset = 0
        self.scale_w_offset = 0
        
    def read_write(self, rw):
        rw.mark_new_contents_array()
        flags = self.flags
        if (flags & 0x8000000000000000) == 0x8000000000000000:
            self.pos_x_offset = rw.rw_pointer(self.pos_x_offset)
        if (flags & 0x4000000000000000) == 0x4000000000000000:
            self.pos_y_offset = rw.rw_pointer(self.pos_y_offset)
        if (flags & 0x2000000000000000) == 0x2000000000000000:
            self.pos_z_offset = rw.rw_pointer(self.pos_z_offset)
        if (flags & 0x1000000000000000) == 0x1000000000000000:
            self.pos_w_offset = rw.rw_pointer(self.pos_w_offset)
            
        if (flags & 0x0800000000000000) == 0x0800000000000000:
            self.rot_x_offset = rw.rw_pointer(self.rot_x_offset)
        if (flags & 0x0400000000000000) == 0x0400000000000000:
            self.rot_y_offset = rw.rw_pointer(self.rot_y_offset)
        if (flags & 0x0200000000000000) == 0x0200000000000000:
            self.rot_z_offset = rw.rw_pointer(self.rot_z_offset)
        if (flags & 0x0100000000000000) == 0x0100000000000000:
            self.rot_w_offset = rw.rw_pointer(self.rot_w_offset)
    
        if (flags & 0x0080000000000000) == 0x0080000000000000:
            self.scale_x_offset = rw.rw_pointer(self.scale_x_offset)
        if (flags & 0x0040000000000000) == 0x0040000000000000:
            self.scale_y_offset = rw.rw_pointer(self.scale_y_offset)
        if (flags & 0x0020000000000000) == 0x0020000000000000:
            self.scale_z_offset = rw.rw_pointer(self.scale_z_offset)
        if (flags & 0x0010000000000000) == 0x0010000000000000:
            self.scale_w_offset = rw.rw_pointer(self.scale_w_offset)
            