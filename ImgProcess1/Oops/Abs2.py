from abc import ABC, abstractmethod

class MCls1(ABC):
    @abstractmethod
    def m1():
        pass

class MCls2(MCls1):
    @abstractmethod
    def m2():
        pass

class MCls3(MCls2):
    def m1():
        print("MCls1 m1 implemented")

    def m2():
        print("MCls2 m2 implemented")

def main():
    MCls3.m1()
    MCls3.m2()

if __name__ == "__main__":
    main()