mylist = []
while True:
    il = input("Введите значение списка, для выхода нажмите 'Q': ")
    if il == 'Q':
        break
    mylist.append(il)

for i in range(0, len(mylist)-1, 2):
    mylist[i+1], mylist[i] = mylist[i], mylist[i+1]

print(mylist)
