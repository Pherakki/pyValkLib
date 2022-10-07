from .CCOL.CCOLReadWriter import CCOLReadWriter
from .HMDL.HMDLReadWriter import HMDLReadWriter
from .HMOT.HMOTReadWriter import HMOTReadWriter
from .HTEX.HTEXReadWriter import HTEXReadWriter
# from .IZCA.HSHP.HSHPReadWriter import HSHPReadWriter
from .IZCA.HSPR.HSPRReadWriter import HSPRReadWriter
from .IZCA.MLX0.MLX0ReadWriter import MLX0ReadWriter
# from .IZCA.PJNT.PJNTReadWriter import PJNTReadWriter
# from .IZCA.PACT.PACTReadWriter import PACTReadWriter
from .IZCA.MXTL.MXTLReadWriter import MXTLReadWriter

containers = {
    "CCOL": CCOLReadWriter,
    "HMDL": HMDLReadWriter,
    "HMOT": HMOTReadWriter,
    # "HSHP": HSHPReadWriter,
    "HSPR": HSPRReadWriter,
    "HTEX": HTEXReadWriter,
    "MLX0": MLX0ReadWriter,
    # "PACT": PACTReadWriter,
    # "PJNT": PJNTReadWriter,
    "MXTL": MXTLReadWriter,
}