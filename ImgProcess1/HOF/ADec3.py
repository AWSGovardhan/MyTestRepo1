def mdeco1(fn):
    def inFn1():
        print('inner fn exec starts...')
        print(fn())
        print('inner fn exec ends...')
    return inFn1


@mdeco1
def fn1():
    return 'Actual Fn execution!!!'

fn1()