def mdeco1(fn):
    def inFn1():
        print('inFn1 execution starts ... ')
        res = fn()
        print('In First Deco',res)
        print('inFn1 execution ends...')
    return inFn1

def mdeco2(fn):
    def inFn2():
        print('inFn2 execution begins!')
        res = fn()
        print('In Second Deco',res)
        print("inFn2 execution ends!")
    return inFn2

# @mdeco1
# @mdeco2
# def fn1():
#     print("apples are red!")

# fn1()

# @mdeco1
# @mdeco2
# def fn1():
#     return "apples are red!";

# # print(fn1())
# fn1()

@mdeco2
@mdeco1
def fn2():
    return 'Grapes are not always green!!'

print(fn2())