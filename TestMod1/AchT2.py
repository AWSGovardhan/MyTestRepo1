class FullName:
    def __init__(self,fname,mname,lname):
        self.fna = fname
        self.mna = mname
        self.lna = lname

    def __str__(self):
        return self.fna+' '+self.mna+' '+self.lna
    
class Stud:
    def __init__(self,obj,age):
        self.name = obj
        self.age = age

    def dispStud(self):
        print(self.name)
        print(self.age)

class Prod:
    def __init__(self,obj,price):
        self.prod = obj
        self.price = price
    def dispProd(self):
        print(self.prod)
        print(self.price)

name = FullName('Sachin','Ramesh','Tendulkar')
s1 = Stud(name,50)
s1.dispStud()

print('======================')
obj = FullName('Maggie','Veg','Soft Noodles')
p1 = Prod(obj,15)
p1.dispProd()
obj = FullName('Maggie','Chicken','Soft Noodles')
p2 = Prod(obj,25)
p2.dispProd()

samp = 