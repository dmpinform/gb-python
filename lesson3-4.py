def my_power(x, y):
    res = x
    for p in range(y - 1):
        res = res * x

    if y == 0:
        return 1
    return res


print(my_power(2, 3))
