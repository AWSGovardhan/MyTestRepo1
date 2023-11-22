def f1():
    print('hello')

def f2():
    pass

x=10
y=20

for e in [f1,x,y,f2]:
    print(callable(e))