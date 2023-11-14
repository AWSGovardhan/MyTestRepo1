class ACls1:
    def __init__(self,acno,btype,actype="Free"):
        self.acno = acno
        self.actype = actype
        self.btype = btype

class GenPmpt:


class GenFnt:


class GenClr:


class GenImg:


class GenCls:
    def __init__(self,acobj):
        self.acinfo = acobj

    def dispGenDtls(self):
        print('Account Number is ',self.acinfo.acno)
        print("Account Type is ",self.acinfo.actype)

    