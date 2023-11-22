def f1():
    print("f1 is called/executed...")

def f2():
    print("f2 is called/executed...")

def main():
    x=10
    y=2
    samp = [1,2,x,y,f1,f2]

    for e in samp:
        if callable(e):
            e()

if __name__ == "__main__":
    main()
