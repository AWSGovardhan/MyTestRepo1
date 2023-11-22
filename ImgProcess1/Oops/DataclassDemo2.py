from dataclasses import dataclass

@dataclass
class GenCls:
    id : int
    name : str

@dataclass
class Emp(GenCls):
    sal : float

@dataclass
class Prod(GenCls):
    price : float
    qty : int

g1 = GenCls(101,'Kiran')

e1 = Emp(1001,'Harry',25678.45)

p1 = Prod(201,'Pencil',2.45,5)

print(g1)

print(e1)

print(g1)