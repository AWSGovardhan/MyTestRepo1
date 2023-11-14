class Connection:
    __instance = None

    def __new__(cls,*args, **kwargs):
        if cls.__instance is None:
            print("Connecting...")
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            print("WARNING : There\'s an instance of the connection already created!")
            return cls.__instance
        
    def __init__(self):
        print("Connection established!")

a = Connection()
b = Connection()

print(a)
print(b)


print(a==b)