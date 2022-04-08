from .CCRS.CCRSReadWriter import CCRSReadWriter
from .ENRS.ENRSReadWriter import ENRSHandler
from .EOFC.EOFCReadWriter import EOFCReadWriter
from .MXEN.MXENReadWriter import MXENReadWriter
from .MXEN.MXEC.MXECReadWriter import MXECReadWriter
from .POF0.POF0ReadWriter import POF0Handler

containers = {
    "CCRS": CCRSReadWriter,
    "ENRS": ENRSHandler,
    "EOFC": EOFCReadWriter,
    "MXEN": MXENReadWriter,
    "MXEC": MXECReadWriter,
    "POF0": POF0Handler
}