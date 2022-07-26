class CCRSTemplateComponent:
    def __init__(self, stride, count, type_):
        self.type = type_
        self.count = count
        self.stride = stride
        
    def __repr__(self):
        return f"<CCRS GenComp> Type: {self.type} Stride: {self.stride} Count: {self.count}</CCRS GenComp>"

    def unpack(self):
        if self.type == 0:
            return [self.stride + i*0x10 for i in range(self.count)]
        elif self.type == 1:
            return [self.stride + i*0x04 for i in range(self.count)]
        elif 1 < self.type <= 5:
            return [self.stride + i*0x02 for i in range(self.count)]
        else:
            raise ValueError(f"Invalid type: {self.type}")
            