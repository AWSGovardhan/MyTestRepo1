def fn(**a):
    for k in a.items():
        print(k)
        for e in k:
            print(e)

fn(name="Apple",Color='red')