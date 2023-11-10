def myImpl(fn):
    def inFn():
        print('Inner Execution Begins...')
        fn()
        print('Inner Execution Ends...')
    return inFn

@myImpl
def myFn():
    print('Hello... Welcome to Deco impl')   
    
myFn()