class Vehicle:
    def __new__(cls, wheels:int):
        if wheels == 2 :
            return Bike()
        elif wheels == 4 : 
            return Car()
        else:
            return super().__new__(cls)
        
    def __init__(self,wheels: int):
        self.wheels = wheels
        print(f"Initializing vehicle with {wheels} wheels")

class Bike:
    def __init__(self):
        print("Initializing the Bike")

class Car:
    def __init__(self):
        print("Initializing the Car")

obj1 = Vehicle(2)
obj2 = Vehicle(4)
obj3 = Vehicle(6)