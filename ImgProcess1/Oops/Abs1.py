from abc import ABC, abstractmethod

class MCls1(ABC):

    @abstractmethod
    def m1(self):
        pass

class MCls2(MCls1):
    def m1(self):
        print("Implemented in MCls2")

def main():
    a = MCls2()
    a.m1()
    # MCls2.m1()

if __name__ == "__main__":
    main()