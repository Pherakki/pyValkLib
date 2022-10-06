from pyValkLib.serialisation.Serializable import Context, Serializable

class SceneNode(Serializable):
    def __init__(self, context=None):
        if context is None:
            self.context = Context()
        super().__init__(context)
        
        self.flags                     = None
        self.ID                        = None
        self.parent_ID                 = None
        self.unknown_0x08              = None
        self.unknown_0x0C              = None
        
        self.parent_offset             = None
        self.first_child_offset        = None
        self.next_sibling_offset       = None
        self.bounding_box_offset       = None
        
        self.bounding_box_vertex_count = None
        self.object_count_1            = None
        self.object_count_2            = None
        self.object_count_3            = None
        self.skeleton_count            = None
        self.is_bone                   = None
        self.object_offset_1           = None
        
        self.object_offset_2           = None
        self.object_offset_3           = None
        self.skeletons_offset          = None
        self.bone_data_offset          = None
        
        self.unknown_0x40              = None
        self.unknown_0x44              = None
        self.unknown_0x48              = None
        self.unknown_0x4C              = None
        self.unknown_0x4D              = None
        self.unknown_0x4E              = None
        self.unknown_0x4F              = None
        
        self.unknown_0x50              = None
    
    
    def read_write(self, rw):
        self.flags                     = rw.rw_uint32(self.flags)
        self.ID                        = rw.rw_uint16(self.ID)
        self.parent_ID                 = rw.rw_uint16(self.parent_ID)
        self.unknown_0x08              = rw.rw_float32(self.unknown_0x08)
        self.unknown_0x0C              = rw.rw_float32(self.unknown_0x0C)
        
        self.parent_offset             = rw.rw_pointer(self.parent_offset)
        self.first_child_offset        = rw.rw_pointer(self.first_child_offset)
        self.next_sibling_offset       = rw.rw_pointer(self.next_sibling_offset)
        self.bounding_box_offset       = rw.rw_pointer(self.bounding_box_offset)
        
        self.bounding_box_vertex_count = rw.rw_uint16(self.bounding_box_vertex_count)
        self.object_count_1            = rw.rw_uint16(self.object_count_1)
        self.object_count_2            = rw.rw_uint16(self.object_count_2)
        self.object_count_3            = rw.rw_uint16(self.object_count_3)
        self.skeleton_count            = rw.rw_uint16(self.skeleton_count)
        self.is_bone                   = rw.rw_uint16(self.is_bone)
        self.object_offset_1           = rw.rw_pointer(self.object_offset_1)
        
        self.object_offset_2           = rw.rw_pointer(self.object_offset_2)
        self.object_offset_3           = rw.rw_pointer(self.object_offset_3)
        self.skeletons_offset          = rw.rw_pointer(self.skeletons_offset)
        self.bone_data_offset          = rw.rw_pointer(self.bone_data_offset)
        
        self.unknown_0x40              = rw.rw_uint32(self.unknown_0x40)
        self.unknown_0x44              = rw.rw_uint32(self.unknown_0x44)
        self.unknown_0x48              = rw.rw_uint32(self.unknown_0x48)
        self.unknown_0x4C              = rw.rw_uint8(self.unknown_0x4C)
        self.unknown_0x4D              = rw.rw_uint8(self.unknown_0x4D)
        self.unknown_0x4E              = rw.rw_uint8(self.unknown_0x4E)
        self.unknown_0x4F              = rw.rw_uint8(self.unknown_0x4F)
        
        self.unknown_0x50 = rw.rw_uint32(self.unknown_0x50) # This one sometimes has no ENRS
        rw.align(rw.local_tell(), 0x10)
        
        rw.assert_is_zero(self.unknown_0x40)
        rw.assert_is_zero(self.unknown_0x48)
        rw.assert_equal(self.unknown_0x4C, 0x20)
        rw.assert_equal(self.unknown_0x4D, 0x20)
        rw.assert_equal(self.unknown_0x4E, 0x20)
        rw.assert_equal(self.unknown_0x4F, 0x20)
