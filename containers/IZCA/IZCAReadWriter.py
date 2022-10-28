from pyValkLib.serialisation.ValkSerializable import Serializable, ValkSerializable16BH
from pyValkLib.containers import containers

class IZCAReadWriter(ValkSerializable16BH):
    FILETYPE = "IZCA"
    
    def __init__(self, endianness, container_endianness):
        super().__init__({}, endianness)
        self.container_endianness = container_endianness
        
        # IZCA Data
        self.section_count = 0
        self.sections = []

    ##############
    # IO METHODS #
    ##############
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x00000000, lambda x: hex(x))

        self.rw_sections(rw)
        rw.align(rw.local_tell(), 0x10)
        
        # Read each section...
                

    ######################
    # SECTION IO METHODS #
    ######################
    def rw_sections(self, rw):
        self.section_count = rw.rw_uint32(self.section_count)
        rw.align(rw.local_tell(), 0x08)
        if rw.mode() == "read":
            self.sections = [IZCASection(self.context) for _ in range(self.section_count)]

        for section in self.sections:
            rw.rw_obj_method(section, section.read_write_def)
        for section in self.sections:
            rw.rw_obj_method(section, section.read_write_offsets)
        rw.align(rw.local_tell(), 0x10)
        
        # First section is always MLX0 only, and it's little-endian
        section = self.sections[0]
        rw.rw_obj_method(section, section.read_write_containers, self.context.endianness)
        for section in self.sections[1:]:
            rw.rw_obj_method(section, section.read_write_containers, self.container_endianness)
        rw.align(rw.local_tell(), 0x10)
            
        
class IZCASection(Serializable):
    __slots__ = ("section_pointers_offset", "section_pointers_count", "section_pointers", "containers")
    
    def __init__(self, context):
        super().__init__(context)
        self.section_pointers_offset = None
        self.section_pointers_count  = None
        self.section_pointers = []
        self.containers       = []
        
    def read_write_def(self, rw):
        self.section_pointers_offset = rw.rw_uint32(self.section_pointers_offset)
        self.section_pointers_count  = rw.rw_uint32(self.section_pointers_count)
        
    def read_write_offsets(self, rw):
        rw.assert_local_file_pointer_now_at("Section pointers", self.section_pointers_offset)
        self.section_pointers = rw.rw_pointers(self.section_pointers, self.section_pointers_count)

    def read_write_containers(self, rw, endianness):
        for i, offset in enumerate(self.section_pointers):
            rw.assert_local_file_pointer_now_at(f"Container {i} Pointer", offset)
            if rw.mode() == "read":
                magic_value = rw.peek_bytestring(4).decode('ascii')
                ctr = containers[magic_value](endianness)
                self.containers.append(ctr)
            rw.rw_obj(self.containers[i])
            rw.align(rw.local_tell(), 0x10)
            