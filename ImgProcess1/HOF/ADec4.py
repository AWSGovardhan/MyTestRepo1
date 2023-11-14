def mdec1(fn):
    def inFn1():
        print("inFn1 execution starts!")
        fn()
        print('inFn1 execution completes!')
    return inFn1

def mdec2(fn):
    def inFn2():
        print('inFn2 execution starts!!')
        fn()
        print('inFn2 execution ends!!')
    return inFn2

def mdec3(fn):
    def inFn3():
        print("inFn3 execution start!!!")
        fn()
        print('inFn3 execution completes!!!')

    return inFn3

# @mdec1
# @mdec2
# @mdec3
# def fn1():
#     print('Act-fn-1 called')


# @mdec3
# @mdec2
# @mdec1
# def fn1():
#     print('Act-fn-1 called')


# @mdec1
# @mdec1
# @mdec1
# def fn1():
#     print('Act-fn-1 called')


@mdec1
@mdec2
@mdec1
@mdec2
@mdec3
def fn1():
    print('Act-fn-1 called')


fn1()