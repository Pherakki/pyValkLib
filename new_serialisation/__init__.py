if (__name__ == "__main__"):
    from ReadWriter import Reader, Writer
    from Serialisable import Serialisable
else:
    from .ReadWriter import Reader, Writer
    from .Serialisable import Serialisable
