from sys import argv


def salary(*args):
    if len(*args) == 3:
        t, mt, bonus = map(float, *args)
        m = t * mt + bonus
        return m
    else:
        return 0


if __name__ == "__main__":
    print(salary(argv[1:]))
