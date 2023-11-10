class NameCls:
    def __init__(self,fna,lna):
        self.fname = fna
        self.lname = lna

    def getName(self):
        return self.fna+' '+self.lna
    

class Impl1:
    def __init__(self,fna,lna):
        self.StudName = NameCls(fna,lna)
        
    def dispStud(self):
        self.StudName.getName()

obj = Impl1('James','Bond')
obj.dispStud()