from pyValkLib.serialisation.BufferViewArray import View

class StructureNodeTransform(View):
    element_size = 4
    @staticmethod
    def rw_op(rw, val, size):
        return rw.rw_float32s(val, size)
    
    def __init__(self, buffer, flags):
        
        self.pxo_idx = -1
        self.pyo_idx = -1
        self.pzo_idx = -1
        self.pwo_idx = -1
        self.rxo_idx = -1
        self.ryo_idx = -1
        self.rzo_idx = -1
        self.rwo_idx = -1
        self.sxo_idx = -1
        self.syo_idx = -1
        self.szo_idx = -1
        self.swo_idx = -1
        
        count = 0
        if (flags & 0x8000000000000000) == 0x8000000000000000:
            self.pxo_idx = count; count += 1
        if (flags & 0x4000000000000000) == 0x4000000000000000:
            self.pyo_idx = count; count += 1
        if (flags & 0x2000000000000000) == 0x2000000000000000:
            self.pzo_idx = count; count += 1
        if (flags & 0x1000000000000000) == 0x1000000000000000:
            self.pwo_idx = count; count += 1
            
        if (flags & 0x0800000000000000) == 0x0800000000000000:
            self.rxo_idx = count; count += 1
        if (flags & 0x0400000000000000) == 0x0400000000000000:
            self.ryo_idx = count; count += 1
        if (flags & 0x0200000000000000) == 0x0200000000000000:
            self.rzo_idx = count; count += 1
        if (flags & 0x0100000000000000) == 0x0100000000000000:
            self.rwo_idx = count; count += 1
    
        if (flags & 0x0080000000000000) == 0x0080000000000000:
            self.sxo_idx = count; count += 1
        if (flags & 0x0040000000000000) == 0x0040000000000000:
            self.syo_idx = count; count += 1
        if (flags & 0x0020000000000000) == 0x0020000000000000:
            self.szo_idx = count; count += 1
        if (flags & 0x0010000000000000) == 0x0010000000000000:
            self.swo_idx = count; count += 1

        self.offsets = buffer[:count]
        
    def __get_offset(self, member):
        return self.offsets[member] if member > -1 else 0 

    @property
    def pos_x(self):
        return self.__get_offset(self.pxo_idx)
        
    @property
    def pos_y(self):
        return self.__get_offset(self.pyo_idx)
        
    @property
    def pos_z(self):
        return self.__get_offset(self.pzo_idx)
        
    @property
    def pos_w(self):
        return self.__get_offset(self.pwo_idx)
        
    @property
    def rot_x(self):
        return self.__get_offset(self.rxo_idx)
        
    @property
    def rot_y(self):
        return self.__get_offset(self.ryo_idx)
    
    @property
    def rot_z(self):
        return self.__get_offset(self.rzo_idx)
    
    @property
    def rot_w(self):
        return self.__get_offset(self.rwo_idx)
    
    @property
    def scale_x(self):
        return self.__get_offset(self.sxo_idx)
    
    @property
    def scale_y(self):
        return self.__get_offset(self.syo_idx)
    
    @property
    def scale_z(self):
        return self.__get_offset(self.szo_idx)
    
    @property
    def scale_w(self):
        return self.__get_offset(self.swo_idx)
