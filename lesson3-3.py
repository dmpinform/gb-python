def my_func(a=0, b=0, c=0):
    my_list = [a, b, c]
    return sum(my_list) - min(a, b, c)
