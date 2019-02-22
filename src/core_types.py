class Header:
    def __init__(self, obj):
        self.magic = self._set_magic(obj)
        self.cputype = None
        self.cpusubtype = None 
        self.filetype = None 
        self.ncmds = None 
        self.sizeofcmds = None 
        self.flags = None 

    def _set_magic(self, obj):
        content = obj[0].hex()
        return "".join((content[i*2: i*2+2] for i in range(3, -1, -1) ))

    #def __
        
class Segment:
    def __init__(self):
        pass

class Section:
    def __init__(self):
        pass
