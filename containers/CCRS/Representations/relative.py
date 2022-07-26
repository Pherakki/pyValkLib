class CCRSRelativeTemplateGenerator:
    def __init__(self, jump, stride, count, subs):
        self.jump = jump
        self.stride = stride
        self.count = count
        self.subs = subs
        
    def __getitem__(self, idx):
        return self.subs[idx]
    
    def __repr__(self):
        out = ""
        for sub in self.subs:
            out += f"\n\t{sub}"
        return f"<CCRS RelGen> Jump: {self.jump} Stride: {self.stride} Count: {self.count}{out}\n</CCRS RelGen>"
