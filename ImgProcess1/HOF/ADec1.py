def mdec1(fn):
    def inner1():
        print("mdec1 inner1 fn execution starts...")
        a = fn()
        # print(a*2)
        return  a*2
        print("mdec1 inner1 fn execution ends")

    return inner1

def mdec2(fn):
    def inner2():
        print("mdec2 inner2 fn execution starts")
        a = fn()
        # print(a+2)
        return a+2
        print("mdec2 inner2 fn execution ends")
    return inner2


#Chaining of decorators
@mdec1
@mdec2
def myFn1():
    return 5

print(myFn1())

#Chaining of decorators
@mdec2
@mdec1
def myFn2():
    return 9

print(myFn2())