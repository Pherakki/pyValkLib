# from .IZCA.IZCAReadWriter import IZCAReadWriter
# from .IZCA.CCOL.CCOLReadWriter import CCOLReadWriter
# from .IZCA.HMDL.HMDLReadWriter import HMDLReadWriter
from .HMOT.HMOTReadWriter import HMOTReadWriter
from .HTEX.HTEXReadWriter import HTEXReadWriter
# from .IZCA.HSHP.HSHPReadWriter import HSHPReadWriter
from .IZCA.MLX0.MLX0ReadWriter import MLX0ReadWriter
# from .IZCA.PJNT.PJNTReadWriter import PJNTReadWriter
# from .IZCA.PACT.PACTReadWriter import PACTReadWriter

containers = {
    # "CCOL": CCOLReadWriter,
    "HMDL": HMDLReadWriter,
    "HMOT": HMOTReadWriter,
    # "HSHP": HSHPReadWriter,
    "HTEX": HTEXReadWriter,
    "MLX0": MLX0ReadWriter,
    # "PACT": PACTReadWriter,
    # "PJNT": PJNTReadWriter,
}