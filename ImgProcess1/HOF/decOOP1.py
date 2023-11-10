class COne:
    def __init__(self):
        print('cons called object created!')

    def MyDeco1(fn):
        def inFn():
            print('inFn called/executed')
            fn()
        return inFn
    
    @MyDeco1
    def myFn(self):
        print("myFn called/executed")
    
a = COne()
a.myFn()