def getNums(n):
    for x in range(1,n+1):
        yield x

res = getNums(5)

print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
# print(next(res))