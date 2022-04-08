from .CCRS.CCRSReadWriter import CCRSReadWriter
from .MXEN.MXENReadWriter import MXENReadWriter
from .MXEN.MXEC.MXECReadWriter import MXECReadWriter
from .POF0.POF0ReadWriter import POF0Handler
from .ENRS.ENRSReadWriter import ENRSHandler

containers = {
    "CCRS": CCRSReadWriter,
    "ENRS": ENRSHandler,
    "MXEN": MXENReadWriter,
    "MXEC": MXECReadWriter,
    "POF0": POF0Handler
}