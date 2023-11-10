class MCls1:
    def __new__(s):
        super(MCls1,s).__new__(s)
        print("new method called object created!")

m1 = MCls1()
m2 = MCls1()