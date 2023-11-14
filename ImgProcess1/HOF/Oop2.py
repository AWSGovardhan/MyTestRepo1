class BCls1:
    def __new__(cls):
        obj = super().__new__(cls)
        print("Obj created!")

class BCls2(BCls1):
    def __init__(self):
        super(BCls2,self).__init__()
        print("Object created is initailized!")


def main():
    a = BCls1()
    b = BCls2()

if __name__ == "__main__":
    main()