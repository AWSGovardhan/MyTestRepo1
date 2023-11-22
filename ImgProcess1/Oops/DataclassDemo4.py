from dataclasses import dataclass,astuple,asdict,field

@dataclass
class MyCls:
    rno:int
    sna:str
    age:int = field(default=21)


a = MyCls(1,'Harry')
b = MyCls(2,'James',23)
print(a)
print(b)
print(astuple(a))
print(astuple(b))
a.rno=201
b.rno=301
print(a)
print(astuple(a))
print(asdict(a))

print(b)
print(astuple(b))
print(asdict(b))

# print(astuple(a))
# print(astuple(b))

# print(asdict(a))
# print(asdict(b))

c = astuple(MyCls(101,'Martin',20))
print(c)
# c.rno=1001 #cannot modify/edit the contents of a tuple object.
print(c)
# print(astuple(c))
# print(asdict(c))