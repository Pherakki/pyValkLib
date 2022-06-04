if (__name__ == "__main__"):
    from ReadWriter import Reader, Writer, Context
else:
    from .ReadWriter import Reader, Writer, Context


class Serializable:
    """
    Provides an interface for symmetrically reading or writing binary data.
    To use, inherit from Serializable, and define a "read_write" method.
    Calling "read" or "write" on the object will then excute this method,
    with either a Reader or a Writer as the operating object.
    """
    __slots__ = ("context",)
    
    def __init__(self):
        self.context = Context()
    
    def read(self, filepath):
        with Reader(filepath) as rw:
            self.read_write(rw)
            
    def write(self, filepath):
        with Writer(filepath) as rw:
            self.read_write(rw)
            
    def read_write(self, rw):
        raise NotImplementedError

