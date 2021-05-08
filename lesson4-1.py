from sys import argv


t, mt, bonus = map(float, argv[1:])
m = t * mt + bonus
print(m)
