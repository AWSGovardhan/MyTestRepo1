def Deco1(fn):
    def inFn1():
        print("Inner fn1 called")
        fn()

    return inFn1

def Deco2(fn):
    def inFn2():
        fn()
        print('Inner fn2 called')
        fn()
    return inFn2

@Deco1
def fn1():
    print("fn1 executed...")

@Deco2
def fn2():
    print("fn2 executed")

fn1()
print('---------------------')
fn2()