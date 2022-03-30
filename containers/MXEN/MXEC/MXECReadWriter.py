from pyValkLib.serialisation.ValkyriaBaseRW import ValkyriaBaseRW32BH
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
        
        self.asset_table = AssetTable(self.endianness)          # Asset table

        self.texmerge_ptr = None
        
        self.component_table_strings = []
        self.entity_table_strings = []
        self.batch_render_strings = []
        self.asset_table_strings = {}

        #self.POF0 = containers["POF0"](containers, endianness)
        #self.ENRS = containers["ENRS"](containers, endianness)
        #self.CCRS = containers["CCRS"](containers, endianness)
        #self.EOFC = containers["EOFC"](containers, endianness)
    
    def read_write_contents(self):
        self.assert_equal("flags", 0x18000000, self.header, lambda x: hex(x))
        self.rw_fileinfo()
        
    def rw_fileinfo(self):
        self.rw_var("content_flags", 'I')
        self.rw_var("component_table_ptr", 'I')    # Entries 1 ptr
        self.rw_var("entity_table_ptr", 'I')       # Entries 2 ptr
        self.rw_var("batch_render_table_ptr", 'I') # Table ptr

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
        print(cflags)
        cflags -= texmerge_enabled * 0x00000100
        cflags -= unknown_enabled * 0x00000400
        cflags -= pvs_enabled * 0x00001800
        cflags -= mergefile_enabled * 0x01000000
        assert cflags == 0, f"Some MXEC flags uncaught! 0x{cflags:0>8x}"
        
        self.rw_var("unknown_0x30", 'I', endianness='>')
        self.rw_var("entry_table_3_ptr", 'I', endianness='>')
        self.rw_var("texmerge_count", 'I', endianness='>')
        self.rw_var("texmerge_ptrs_ptr", 'I', endianness='>')
        
        self.assert_equal("unknown_0x30", 1)
        
        
