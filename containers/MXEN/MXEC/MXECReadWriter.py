from pyValkLib.serialisation.ValkyriaBaseRW import ValkyriaBaseRW32BH, PointerIndexableArray
from pyValkLib.containers.MXEN.MXEC.EntryTable import EntryTable 
from pyValkLib.containers.MXEN.MXEC.ECSComponentEntry import ComponentEntry
from pyValkLib.containers.MXEN.MXEC.ECSEntityEntry import EntityEntry
from pyValkLib.containers.MXEN.MXEC.BatchRenderEntry import BatchRenderEntry
from pyValkLib.containers.MXEN.MXEC.AssetTable import AssetTable

class MXECReadWriter(ValkyriaBaseRW32BH):
    FILETYPE = "MXEC"
    
    def __init__(self, containers, endianness=None):
        super().__init__(containers, endianness)
        
        self.content_flags = None
        self.component_table_ptr = None
        self.entity_table_ptr = None
        self.batch_render_table_ptr = None
        
        self.component_table    = EntryTable(ComponentEntry, self.endianness)    # Component table
        self.entity_table       = EntryTable(EntityEntry, self.endianness)       # Entity table
        self.batch_render_table = EntryTable(BatchRenderEntry, self.endianness)  # Batch render table?
        # "Batch Render" role is not confirmed; just a guess for now
        
        self.asset_table = AssetTable(self.endianness)          # Asset table

        self.texmerge_ptr = None
        self.strings = PointerIndexableArray()

        self.POF0 = containers["POF0"](containers, '<')
        self.ENRS = containers["ENRS"](containers, '<')
        self.CCRS = containers["CCRS"](containers, endianness)
        #self.EOFC = containers["EOFC"](containers, endianness)
        
        self.subcontainers.extend([self.POF0, self.ENRS, self.CCRS])
            
    def check_string(self, offset, prnt=False):
        curr_offset = self.local_tell()
        self.local_seek(offset)
        lookup_type = read_null_terminated_string(self.bytestream)
        self.local_seek(curr_offset)
        return lookup_type
    
    def check_struct_type(self, offset, prnt=False):
        curr_offset = self.local_tell()
        self.local_seek(offset)
        lookup_type = read_struct_type_string(self.bytestream)
        self.local_seek(curr_offset)
        return lookup_type
    
    def read_write_contents(self):
        self.assert_equal("flags", 0x18000000, self.header, lambda x: hex(x))
        self.rw_fileinfo()
        self.rw_components_table()
        self.rw_entities_table()
        self.rw_batch_render_table()
        self.rw_asset_table()
        self.rw_strings()
        
    def rw_fileinfo(self):
        self.rw_var("content_flags", 'I')
        self.rw_var("component_table_ptr", 'I')
        self.rw_var("entity_table_ptr", 'I')
        self.rw_var("asset_table_ptr", 'I')

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
        
        self.rw_var("unknown_0x30", 'I')
        self.rw_var("batch_render_table_ptr", 'I')
        self.rw_var("texmerge_count", 'I')
        self.rw_var("texmerge_ptrs_ptr", 'I')
        
        self.assert_equal("unknown_0x30", 1)
        
        
        self.rw_var("pvs_record_ptr", 'I')
        self.rw_var("mergefile_record_ptr", "I")
        self.rw_var("unknown_0x48", 'I')
        self.rw_var("unknown_0x4C", 'I')
        
        self.assert_equal("unknown_0x48", 0)
        self.assert_equal("unknown_0x4C", 0)

        
        self.rw_var("unknown_0x50", 'I')
        self.rw_var("unknown_0x54", 'I')
        self.rw_var("unknown_0x58", 'I')
        self.rw_var("unknown_0x5C", 'I')
        
        self.assert_equal("unknown_0x50", 0)
        self.assert_equal("unknown_0x54", 0)
        self.assert_equal("unknown_0x58", 0)
        self.assert_equal("unknown_0x5C", 0)
        
    def rw_components_table(self):
        if self.component_table_ptr != 0:
            self.assert_local_file_pointer_now_at(self.component_table_ptr)
            self.rw_readwriter(self.component_table)
            
            self.assert_local_file_pointer_now_at(self.component_table.entry_ptr)
            self.run_rw_method(self.component_table.rw_entry_headers, self.global_tell(), self.local_tell())
            
            for entry in sorted([entry for entry in self.component_table.entries.data], key=lambda x: x.data_offset):
                component_type = self.check_struct_type(entry.name_offset)
                if entry.data_offset:
                    self.assert_local_file_pointer_now_at(entry.data_offset)
                    self.run_rw_method(entry.rw_data, component_type)
                    self.cleanup_ragged_chunk(self.local_tell(), 0x10)
            
            
    def rw_entities_table(self):
        if self.entity_table_ptr != 0:
            self.assert_local_file_pointer_now_at(self.entity_table_ptr)
            self.rw_readwriter(self.entity_table)
            
            self.assert_local_file_pointer_now_at(self.entity_table.entry_ptr)
            self.run_rw_method(self.entity_table.rw_entry_headers, self.global_tell(), self.local_tell())
            
            for entry in sorted([entry for entry in self.entity_table.entries.data], key=lambda x: x.data_offset):
                self.assert_local_file_pointer_now_at(entry.data_offset)
                self.run_rw_method(entry.rw_data, self.local_tell())

            self.cleanup_ragged_chunk(self.local_tell(), 0x10)
            
    def rw_batch_render_table(self):
        if self.batch_render_table_ptr != 0:
            self.assert_local_file_pointer_now_at(self.batch_render_table_ptr)
            self.rw_readwriter(self.batch_render_table)
            
            self.run_rw_method(self.batch_render_table.rw_entry_headers, self.global_tell(), self.local_tell())

            for entry in self.batch_render_table.entries.data:                
                if entry.t1_offset:
                    self.assert_local_file_pointer_now_at(entry.t1_offset)
                    self.run_rw_method(entry.rw_t1_data)

                if entry.t2_offset:
                    self.assert_local_file_pointer_now_at(entry.t2_offset)
                    self.run_rw_method(entry.rw_2_data)
                
                for t1 in entry.t1_data:
                    if t1.offset_1:
                        self.assert_local_file_pointer_now_at(t1.offset_1)
                        self.run_rw_method(t1.rw_data_1)
                    if t1.offset_2:
                        self.assert_local_file_pointer_now_at(t1.offset_2)
                        self.run_rw_method(t1.rw_data_2)
                
                for t2 in entry.t2_data:
                    if t2.offset:
                        self.assert_local_file_pointer_now_at(t2.offset)
                        self.run_rw_method(t2.rw_data)
                    
                self.cleanup_ragged_chunk_read(self.local_tell(), 0x10)
                
                if entry.t3_offset:
                    self.assert_local_file_pointer_now_at(entry.t3_offset)
                    self.run_rw_method(entry.rw_t3_data)
                    
                    for t3 in entry.t3_data:
                        if t3.offset_1:
                            self.assert_local_file_pointer_now_at(t3.offset_1)
                            self.run_rw_method(t3.rw_data_1)
                        if t3.offset_2:
                            self.assert_local_file_pointer_now_at(t3.offset_2)
                            self.run_rw_method(t3.rw_data_2)
                        if t3.offset_3:
                            self.assert_local_file_pointer_now_at(t3.offset_3)
                            self.run_rw_method(t3.rw_data_3)
                        if t3.offset_4:
                            self.assert_local_file_pointer_now_at(t3.offset_4)
                            self.run_rw_method(t3.rw_data_4)
                
                if entry.t4_offset:
                    self.assert_local_file_pointer_now_at(entry.t4_offset)
                    self.run_rw_method(entry.rw_t4_data)

                self.cleanup_ragged_chunk_read(self.local_tell(), 0x10)
                  
      
            
    def rw_asset_table(self):
        if self.asset_table_ptr != 0:
            self.assert_local_file_pointer_now_at(self.asset_table_ptr)
            self.rw_readwriter(self.asset_table)
        
            self.assert_local_file_pointer_now_at(self.asset_table.offset_1)
            for elem in self.asset_table.elements_1:
                self.rw_readwriter(elem)
                
            self.assert_local_file_pointer_now_at(self.asset_table.offset_2)
            self.run_rw_method(self.asset_table.rw_unknown_offsets)
    
            if self.texmerge_ptrs_ptr != 0:
                self.assert_local_file_pointer_now_at(self.texmerge_ptrs_ptr)
                self.rw_varlist("texmerge_ptr", 'I', self.texmerge_count)
            self.cleanup_ragged_chunk(self.local_tell(), 0x10)
        
    def rw_strings(self):
        strn = None
        string_blob = iter(self.bytestream.read(self.header.header_length + self.header.data_length - self.local_tell()))

        n_entries = 0
        while not (strn == "\x00" or strn == ""):
            curpos = self.local_tell()
            self.strings.ptr_to_idx[curpos] = n_entries
            
            try:
                strn = parse_null_terminated_string(string_blob)
                if strn == "\x00" or strn == "":
                    break
            except StopIteration:
                break
            
            self.strings.data.append(strn)
            self.strings.idx_to_ptr.append(curpos)
            n_entries += 1
            
        self.cleanup_ragged_chunk(self.local_tell(), 0x10)

def read_null_terminated_string(bytestream):
    string = b''
    char = bytestream.read(1)
    while char != b'\x00':
        string += char
        char = bytestream.read(1)
    string = string.decode('cp932', errors="ignore")  
    return string   

def parse_null_terminated_string(data):
    string = b''
    char = next(data).to_bytes(1, 'big')
    while char != b'\x00':
        string += char
        char = next(data).to_bytes(1, 'big')
    string = string.decode('cp932', errors="ignore")  
    return string  

def read_struct_type_string(bytestream):
    string = b''
    char = bytestream.read(1)
    while char != b':':
        string += char
        char = bytestream.read(1)
    string = string.decode('cp932', errors="ignore")  
    return string.lstrip("+").split("@")[-1]