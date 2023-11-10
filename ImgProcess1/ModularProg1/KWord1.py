class MyClass:
    def __new__(cls):
        instance = super(MyClass, cls).__new__(cls)
        instance.custom_attribute = "Custom Value"
        return instance

my_instance = MyClass()
m2 = MyClass()