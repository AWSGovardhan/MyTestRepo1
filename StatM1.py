
class MyCls1:
    @staticmethod
    def f1(myname:str):
        print("Given name is :: ",myname)

    def f2(k):
        print("instance m called")


MyCls1.f1("Samp1")
MyCls1.f1("Samp2")
name = 'Samp3'
MyCls1.f1(name)

obj = MyCls1()
obj.f2()
