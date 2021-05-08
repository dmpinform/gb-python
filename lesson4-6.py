import itertools

start = 3
for i in itertools.count(start):
    print(i)
    if i == 10:
        break


my_list = "you can't easily get a fish out of the ..."
for i in itertools.cycle(my_list.split(" ")):
    print(i)
    if i == "...":
        break
