from pyValkLib.serialisation.Serializable import Context, Serializable

class SceneNodeBinary(Serializable):
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
        self.bone_type                 = None
        self.object_offset_1           = None
        
        self.object_offset_2           = None
        self.object_offset_3           = None
        self.skeletons_offset          = None
        self.bone_data_offset          = None
        
        self.unknown_0x40              = 0
        self.unknown_0x44              = None
        self.unknown_0x48              = 0
        self.unknown_0x4C              = 0x20
        self.unknown_0x4D              = 0x20
        self.unknown_0x4E              = 0x20
        self.unknown_0x4F              = 0x20
        
        self.unknown_0x50              = None
    
    def __repr__(self):
        flags = hex(self.flags) if self.flags is not None else self.flags
        return f"[KFMS::SceneNode] {flags} {self.ID} {self.parent_ID} {self.unknown_0x08} {self.unknown_0x0C} " \
            f"{self.parent_offset} {self.first_child_offset} {self.next_sibling_offset} {self.bounding_box_offset} " \
            f"{self.bounding_box_vertex_count} {self.object_count_1} {self.object_count_2} {self.object_count_3} " \
            f"{self.skeleton_count} {self.bone_type} {self.object_offset_1} {self.object_offset_2} {self.object_offset_3} " \
            f"{self.skeletons_offset} {self.bone_data_offset} {self.unknown_0x44} {self.unknown_0x50}"
    
    def __eq__(self, other):
        return \
            self.flags                     == other.flags                     and \
            self.ID                        == other.ID                        and \
            self.parent_ID                 == other.parent_ID                 and \
            self.unknown_0x08              == other.unknown_0x08              and \
            self.unknown_0x0C              == other.unknown_0x0C              and \
            \
            self.parent_offset             == other.parent_offset             and \
            self.first_child_offset        == other.first_child_offset        and \
            self.next_sibling_offset       == other.next_sibling_offset       and \
            self.bounding_box_offset       == other.bounding_box_offset       and \
            \
            self.bounding_box_vertex_count == other.bounding_box_vertex_count and \
            self.object_count_1            == other.object_count_1            and \
            self.object_count_2            == other.object_count_2            and \
            self.object_count_3            == other.object_count_3            and \
            self.skeleton_count            == other.skeleton_count            and \
            self.bone_type                 == other.bone_type                   and \
            self.object_offset_1           == other.object_offset_1           and \
            \
            self.object_offset_2           == other.object_offset_2           and \
            self.object_offset_3           == other.object_offset_3           and \
            self.skeletons_offset          == other.skeletons_offset          and \
            self.bone_data_offset          == other.bone_data_offset          and \
            \
            self.unknown_0x40              == other.unknown_0x40              and \
            self.unknown_0x44              == other.unknown_0x44              and \
            self.unknown_0x48              == other.unknown_0x48              and \
            self.unknown_0x4C              == other.unknown_0x4C              and \
            self.unknown_0x4D              == other.unknown_0x4D              and \
            self.unknown_0x4E              == other.unknown_0x4E              and \
            self.unknown_0x4F              == other.unknown_0x4F              and \
            \
            self.unknown_0x50              == other.unknown_0x50 
            
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
        self.bone_type                 = rw.rw_uint16(self.bone_type)
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
