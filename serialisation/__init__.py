if (__name__ == "__main__"):
    from ReadWriter import Reader, Writer
    from Serializable import Serialisable
else:
    from .ReadWriter import Reader, Writer
    from .Serializable import Serialisable
