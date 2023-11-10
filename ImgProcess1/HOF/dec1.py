def myDecoFn(fn):
    def innerFn():
        print('Before actual fn')
        fn()
        print("After actual fn")
    return innerFn

@myDecoFn
def myFn1():
    print("Executing simple functionality")

myFn1()

# if __name__ == '__main__':
#     myFn1()
