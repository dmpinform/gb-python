s = input("Write words separated by space: ")
for i, val in enumerate(s.split(" ")):
    print(f"{i} {val}", end="\n")
