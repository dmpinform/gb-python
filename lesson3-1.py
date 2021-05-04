def my_div(a, b):
    res = 0
    try:
        res = a/b
    except ZeroDivisionError as e:
        print(e)
    finally:
        return res


print(my_div(2, 2))
