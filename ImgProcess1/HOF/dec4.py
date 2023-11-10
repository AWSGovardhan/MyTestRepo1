def myDeco1(fn):
    def inFn():
        print("Deco-Fn-1 starts")
        fn()
        print("Deco-Fn-1 ends")
    return inFn

@myDeco1
def fn1():
    print("Actual Fn Exec...")


def myDeco2(fn):
    def inFn():
        print("Deco-fn2 starts")
        fn()
        print('Deco-fn2 ends')
    return inFn


@myDeco2
def fn2():
    print("Next Actual Fn Executes")

fn1()
fn2()