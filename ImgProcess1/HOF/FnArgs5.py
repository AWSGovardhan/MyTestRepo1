# def fn(**kargs):
#     for k in kargs:
#         print(k,',',kargs[k])


def fn(**kargs):
    for k in kargs.items():
        # print(k)
        for e in k:
            print(e)

fn(rno=1,name='Allen',age=21,gen='F')
print("=========================")
fn(pid=101,pname='Pen',price=12,qty=5)
print("=========================")
fn(eid=1001,ena='James',age=30,gen='Male')