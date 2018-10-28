def gen(x):
    n=10
    for y in range(n):
        if y%x==0:
            pass
        else:
            yield y
g=gen(2)
for i in g:
    print i
