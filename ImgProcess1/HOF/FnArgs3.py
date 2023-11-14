def fn(*a):
    for e in a:
        print(e)

fn(1,2,3)
print('------------------')
fn('Apple','Pomogranate','Almonds')
print('--------------------')
fn('Hello',10,2.234,True,False)