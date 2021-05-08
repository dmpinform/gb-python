def fact(_n):
    f = 1
    for i in range(1, _n + 1):
        f = f*i
        yield f


n = 4
print(f"{n}! =  {max(fact(n))}")

for el in fact(n):
    print(el)
