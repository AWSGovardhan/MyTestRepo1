from dataclasses import dataclass

@dataclass #provides constructor and repr methods
class Person:
    pid : int
    name : str
    age : int

    def __gt__(self,other):
        if self.pid>other.pid:
            return True
        else:
            return False

p1 = Person(1001,'Peter',21)

p2 = Person(1002,'James',20) 

print(p1)
print(p2)
print(p1>p2)

print(p1==p2)
print(p1!=p2)