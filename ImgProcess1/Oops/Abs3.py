from abc import ABC, abstractmethod

class MCls1(ABC):
    @abstractmethod
    def m1(self):
        pass

class MCls2(MCls1):
    @abstractmethod
    def m2(self):
        pass

class MCls3(MCls2):
    def m1(self):
        print("MCls1 m1 implemented here")

    def m2(self):
        print("MCls2 m2 implemented here")

def main():
    a = MCls3()
    a.m1()
    a.m2()

if __name__ == "__main__":
    main()