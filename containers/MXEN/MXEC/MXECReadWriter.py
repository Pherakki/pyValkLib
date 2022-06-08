from pyValkLib.serialisation.Serializable import Context
from pyValkLib.serialisation.ValkSerializable import ValkSerializable32BH
from pyValkLib.serialisation.PointerIndexableArray import PointerIndexableArray, PointerIndexableArrayCStr, PointerIndexableArrayUint64
from pyValkLib.containers.MXEN.MXEC.EntryTable import EntryTable 
from pyValkLib.containers.MXEN.MXEC.ECSComponentEntry import ComponentEntry
from pyValkLib.containers.MXEN.MXEC.ECSEntityEntry import EntityEntry
from pyValkLib.containers.MXEN.MXEC.BatchRenderEntry import BatchRenderEntry
from pyValkLib.containers.MXEN.MXEC.AssetTable import AssetTable
import struct


class MXECReadWriter(ValkSerializable32BH):
    FILETYPE = "MXEC"
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        
        self.content_flags          = None
        self.component_table_ptr    = None
        self.entity_table_ptr       = None
        self.asset_table_ptr        = None
        
        self.unknown_0x30           = None
        self.batch_render_table_ptr = None
        self.texmerge_count         = None
        self.texmerge_ptrs_ptr      = None
        
        self.pvs_record_ptr         = None
        self.mergefile_record_ptr   = None
        self.padding_0x48           = 0
        self.padding_0x4C           = 0
        
        self.padding_0x50           = 0
        self.padding_0x54           = 0
        self.padding_0x58           = 0
        self.padding_0x5C           = 0
        
        self.component_table    = EntryTable(ComponentEntry, self.context)    # Component table
        self.entity_table       = EntryTable(EntityEntry, self.context)       # Entity table
        self.batch_render_table = EntryTable(BatchRenderEntry, self.context)  # Batch render table?
        # "Batch Render" role is not confirmed; just a guess for now
        
        self.asset_table = AssetTable(self.context)          # Asset table

        self.texmerge_ptr = None
        self.strings = PointerIndexableArrayCStr(self.context, "cp932")
        self.unknowns = PointerIndexableArrayUint64(self.context)

        subcontainer_context = Context()
        subcontainer_context.endianness = '<'
        self.POF0 = containers["POF0"](containers, subcontainer_context)
        self.ENRS = containers["ENRS"](containers, subcontainer_context)
        self.CCRS = containers["CCRS"](containers, '<')
        self.EOFC = containers["EOFC"](containers, '<')

        self.subcontainers.extend([self.POF0, self.ENRS, self.CCRS, self.EOFC])
            
    def __repr__(self):
        return f"MXEC Object [{self.header.depth}] [0x{self.header.flags:0>8x}]:\n" \
               f"[{len(self.component_table.entries.data)}] Components.\n"\
               f"[{len(self.entity_table.entries.data)}] Entities.\n"\
               f"[{len(self.batch_render_table.entries.data)}] Batch Render Entries.\n"\
               f"[{len(self.asset_table.entries.data)}] Asset References.\n"\
               f"[{len(self.asset_table.asset_slot_offsets)}] Asset Pointers.\n"\
               f"Contains POF0, ENRS, CCRS, and EOFC."
    
    def read_write_contents(self, rw):
        rw.assert_equal(self.header.flags, 0x18000000, lambda x: hex(x))
        self.rw_fileinfo(rw)
        self.rw_components_table(rw)
        self.rw_entities_table(rw)
        self.rw_batch_render_table(rw)
        self.rw_asset_table(rw)
        self.rw_strings(rw)
        self.rw_unknowns(rw)
        
    def rw_fileinfo(self, rw):
        # Read/write

        self.content_flags       = rw.rw_uint32(self.content_flags)
        self.component_table_ptr = rw.rw_pointer(self.component_table_ptr)
        self.entity_table_ptr    = rw.rw_pointer(self.entity_table_ptr)
        self.asset_table_ptr     = rw.rw_pointer(self.asset_table_ptr)

        self.unknown_0x30           = rw.rw_uint32(self.unknown_0x30)
        self.batch_render_table_ptr = rw.rw_pointer(self.batch_render_table_ptr)
        self.texmerge_count         = rw.rw_uint32(self.texmerge_count)
        self.texmerge_ptrs_ptr      = rw.rw_pointer(self.texmerge_ptrs_ptr)
        
        self.pvs_record_ptr       = rw.rw_pointer(self.pvs_record_ptr)
        self.mergefile_record_ptr = rw.rw_pointer(self.mergefile_record_ptr)
        self.padding_0x48         = rw.rw_pad32(self.padding_0x48)
        self.padding_0x4C         = rw.rw_pad32(self.padding_0x4C)
        
        self.padding_0x50 = rw.rw_pad32(self.padding_0x50)
        self.padding_0x54 = rw.rw_pad32(self.padding_0x54)
        self.padding_0x58 = rw.rw_pad32(self.padding_0x58)
        self.padding_0x5C = rw.rw_pad32(self.padding_0x5C)
        
        # VALIDATION
        
        # 0x00000100 -> texmerge count + ptrs_ptr enabled
        # 0x00000400 -> texmerge count + ptrs_ptr enabled
        # 0x00001800 -> pvs enabled
        # 0x01000000 -> mergefile enabled
        texmerge_enabled  = (self.content_flags & 0x00000100) == 0x00000100
        unknown_enabled   = (self.content_flags & 0x00000400) == 0x00000400
        pvs_enabled       = (self.content_flags & 0x00001800) == 0x00001800
        mergefile_enabled = (self.content_flags & 0x01000000) == 0x01000000
        
        # Check we've got all the flags
        cflags = self.content_flags
        cflags -=  texmerge_enabled * 0x00000100
        cflags -=   unknown_enabled * 0x00000400
        cflags -=       pvs_enabled * 0x00001800
        cflags -= mergefile_enabled * 0x01000000
        assert cflags == 0, f"Some MXEC flags uncaught! 0x{cflags:0>8x}"
        
        rw.assert_equal(self.unknown_0x30, 1)
        #rw.assert_equal((self.texmerge_count > 0), texmerge_enabled)
        #rw.assert_equal((self.texmerge_ptrs_ptr > 0), texmerge_enabled)
        
        rw.assert_equal(self.padding_0x48, 0)
        rw.assert_equal(self.padding_0x4C, 0)
        rw.assert_equal((self.pvs_record_ptr > 0), pvs_enabled)
        rw.assert_equal((self.mergefile_record_ptr > 0), mergefile_enabled)

        rw.assert_equal(self.padding_0x50, 0)
        rw.assert_equal(self.padding_0x54, 0)
        rw.assert_equal(self.padding_0x58, 0)
        rw.assert_equal(self.padding_0x5C, 0)
        
    def rw_components_table(self, rw):
        if self.component_table_ptr != 0:
            rw.assert_local_file_pointer_now_at("Component Table", self.component_table_ptr)
            rw.rw_obj_method(self.component_table, self.component_table.rw_fileinfo)
            rw.assert_local_file_pointer_now_at("Component Table Entry Headers", self.component_table.entry_ptr)
            rw.rw_obj_method(self.component_table, self.component_table.rw_entry_headers)
            rw.rw_obj_method(self.component_table, self.component_table.rw_entries)

    def rw_entities_table(self, rw):
        if self.entity_table_ptr != 0:
            rw.assert_local_file_pointer_now_at("Entity Table", self.entity_table_ptr)
            rw.rw_obj_method(self.entity_table, self.entity_table.rw_fileinfo)
            rw.assert_local_file_pointer_now_at("Entity Table Entry Headers", self.entity_table.entry_ptr)
            rw.rw_obj_method(self.entity_table, self.entity_table.rw_entry_headers)
            rw.rw_obj_method(self.entity_table, self.entity_table.rw_entries)

            rw.align(rw.local_tell(), 0x10)
            
    def rw_batch_render_table(self, rw):
        if self.batch_render_table_ptr != 0:
            rw.assert_local_file_pointer_now_at("Batch Render Table", self.batch_render_table_ptr)
            rw.rw_obj_method(self.batch_render_table, self.batch_render_table.rw_fileinfo_brt)
            rw.assert_local_file_pointer_now_at("Batch Render Table Entry Headers", self.batch_render_table.entry_ptr)
            rw.rw_obj_method(self.batch_render_table, self.batch_render_table.rw_entry_headers)
            for entry in self.batch_render_table.entries:
                rw.rw_obj_method(entry, entry.rw_data)

    def rw_asset_table(self, rw):
        if self.asset_table_ptr != 0:
            rw.assert_local_file_pointer_now_at("Asset Table", self.asset_table_ptr)
            rw.rw_obj_method(self.asset_table, self.asset_table.rw_fileinfo)
            
            rw.assert_local_file_pointer_now_at("Asset Table Entry Headers", self.asset_table.asset_references_offset)
            rw.rw_obj_method(self.asset_table, self.asset_table.rw_entry_headers)

                
            rw.assert_local_file_pointer_now_at("Asset Table Entries", self.asset_table.asset_use_offset)
            rw.rw_obj_method(self.asset_table, self.asset_table.rw_asset_slot_offsets)
    
            if self.texmerge_ptrs_ptr != 0:
                rw.assert_local_file_pointer_now_at("Texmerge pointers", self.texmerge_ptrs_ptr)
                self.texmerge_ptr = rw.rw_pointers(self.texmerge_ptr, self.texmerge_count)
            rw.align(rw.local_tell(), 0x10)
        
    def rw_strings(self, rw):
        # This needs sorting out - clearly the full string structure isn't completely understood yet
        if (rw.mode() == "read"):
            self.read_strings(rw)
        elif (rw.mode() == "write"):
            self.write_strings(rw)
        #else:
        #    raise Exception("Unknown mode!")
            
        rw.align(rw.local_tell(), 0x10)
        
    def read_strings(self, rw):
        curpos = rw.local_tell()
        start_pos = rw.local_tell()

        # Get the start of the unknown data
        entity_data_offsets = [elem.unknown_data_ptr for elem in self.entity_table.entries.data if elem.unknown_data_ptr > 0]
        end_point = min(entity_data_offsets) if len(entity_data_offsets) else self.header.header_length + self.header.data_length

        # Get the start of the component strings
        component_string_offsets = [getattr(elem.data, "get_string_ptrs", lambda:[])() for elem in self.component_table.entries]
        component_string_offsets = [subitem for item in component_string_offsets for subitem in item]
        start_of_component_strings = min(component_string_offsets) if len(component_string_offsets) else end_point

        main_string_blob      = memoryview(rw.bytestream.read(start_of_component_strings - rw.local_tell()))
        if len(main_string_blob):
            if main_string_blob[0] == 0:
                curpos += 1
        n_entries = 0
        while curpos < start_of_component_strings:
            strn, size = parse_null_terminated_string(main_string_blob[curpos-start_pos:])
            if strn == b"":
                curpos += 1  # Looks like we read a null-terminator, must be at alignment
                break

            self.strings.data.append(strn)
            self.strings.ptr_to_idx[curpos] = n_entries
            self.strings.idx_to_ptr[n_entries] = curpos
            n_entries += 1
            curpos += size

        remaining_stuff = main_string_blob[curpos-start_pos:].tobytes()
        if remaining_stuff != (b'\x00'*len(remaining_stuff)):
            raise Exception(f"End of main string bank not reached!\n{remaining_stuff}")
        rw.align(rw.local_tell(), 0x10) # <- Alignment not done for VlMxGeneralCharInfo??!!? Are some strings shared between components and main on game_info_sys_param?!
        curpos = rw.local_tell()

        rw.assert_local_file_pointer_now_at("Start of Component Strings Table", start_of_component_strings)
        component_string_blob = memoryview(rw.bytestream.read(end_point - start_of_component_strings))
        if len(component_string_blob):
            if component_string_blob[0] == 0:
                curpos += 1
        while curpos < end_point:
            strn, size = parse_null_terminated_string(component_string_blob[curpos-start_of_component_strings:])
            if strn == b"":
                break

            self.strings.data.append(strn)
            self.strings.ptr_to_idx[curpos] = n_entries
            self.strings.idx_to_ptr[n_entries] = curpos
            n_entries += 1
            curpos += size

        remaining_stuff = component_string_blob[curpos-start_of_component_strings:].tobytes()
        if remaining_stuff != (b'\x00'*len(remaining_stuff)):
            print(remaining_stuff)
            raise Exception("End of component string bank not reached!")
        rw.align(rw.local_tell(), 0x10)
        rw.assert_local_file_pointer_now_at("End of Component Strings Table", end_point)
        
    def write_strings(self, rw):
        for string in self.strings.data:
            rw.bytestream.write(string.encode("cp932"))
            rw.bytestream.write(b"\x00")
        
    def read_unknowns(self, rw):
        entity_data_offsets = sorted(set([elem.unknown_data_ptr for elem in self.entity_table.entries.data if elem.unknown_data_ptr > 0]))
        for offset in entity_data_offsets:
            rw.assert_local_file_pointer_now_at("Unknowns Offset", offset)
            idx =  len(self.unknowns.idx_to_ptr)
            self.unknowns.ptr_to_idx[offset] = len(self.unknowns.idx_to_ptr)
            self.unknowns.idx_to_ptr[idx] = offset
            self.unknowns.data.append((struct.unpack('Q', rw.bytestream.read(8))[0]))

    def write_unknowns(self, rw):
        for data in self.unknowns.data:
            rw.bytestream.write(struct.pack('Q', *data))

    def rw_unknowns(self, rw):
        if (rw.mode() == "read"):
            self.read_unknowns(rw)
        elif (rw.mode() == "write"):
            self.write_unknowns(rw)
        #else:
        #    raise Exception("Unknown mode!")
        rw.align(rw.local_tell(), 0x10)
        

def parse_null_terminated_string(data):
    size = 0
    while data[size] != 0:
        size += 1

    string = data[0:size].tobytes()#.decode('cp932') # Asset table strings are UTF8, all others are SHIFT-JIS... delay decode for the particular table

    return string, size+1
