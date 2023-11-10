def Deco1(fn):
    def inFn():
        print('Inner execution starts')
        print("Innter execution ends")

    return inFn

@Deco1
def myFn():
    print("Actual Fn Executes...")


myFn()