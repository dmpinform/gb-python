res = 0
i = ""
while i != "Q":
    mys = input("Enter numbers separated by a space (Q - exit): ")
    for i in mys.split(" "):
        if i.isdigit():
            res += int(i)
        if i == "Q":
            break
    print(res)
