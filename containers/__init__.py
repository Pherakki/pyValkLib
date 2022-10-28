from .CCOL.CCOLReadWriter import CCOLReadWriter
from .HCMT.HCMTReadWriter import HCMTReadWriter
from .HMDL.HMDLReadWriter import HMDLReadWriter
from .HMMT.HMMTReadWriter import HMMTReadWriter
from .HMOT.HMOTReadWriter import HMOTReadWriter
from .HMRP.HMRPReadWriter import HMRPReadWriter
from .HSCM.HSCMReadWriter import HSCMReadWriter
from .HSPR.HSPRReadWriter import HSPRSkipper
from .HTEX.HTEXReadWriter import HTEXReadWriter
from .HTEX.HTSF.HTSFReadWriter import InlineHTSFReadWriter
from .IZCA.CLDC.CLDCReadWriter import CLDCReadWriter
from .IZCA.HSHP.HSHPReadWriter import HSHPReadWriter
from .IZCA.MLX0.MLX0ReadWriter import MLX0ReadWriter
# from .IZCA.PJNT.PJNTReadWriter import PJNTReadWriter
# from .IZCA.PACT.PACTReadWriter import PACTReadWriter
from .IZCA.MXTF.MXTFReadWriter import MXTFReadWriter
from .IZCA.MXTL.MXTLReadWriter import MXTLReadWriter

containers = {
    "CCOL": CCOLReadWriter,
    "CLDC": CLDCReadWriter,
    "HCMT": HCMTReadWriter,
    "HMDL": HMDLReadWriter,
    "HMOT": HMOTReadWriter,
    "HMMT": HMMTReadWriter,
    "HMRP": HMRPReadWriter,
    "HSCM": HSCMReadWriter,
    "HSHP": HSHPReadWriter,
    "HSPR": HSPRSkipper,
    "HTEX": HTEXReadWriter,
    "HTSF": InlineHTSFReadWriter,
    "MLX0": MLX0ReadWriter,
    # "PACT": PACTReadWriter,
    # "PJNT": PJNTReadWriter,
    "MXTF": MXTFReadWriter,
    "MXTL": MXTLReadWriter,
}