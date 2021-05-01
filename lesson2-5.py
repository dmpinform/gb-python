mylist = [9, 7, 5, 3, 3, 2]

new_elem = int(input("Enter new elem: "))
mylist.sort()

if int(new_elem) in mylist:
    index = mylist.index(new_elem)
    mylist.insert(index, new_elem)
else:
    mylist.append(int(new_elem))

mylist.sort(reverse=True)
print(mylist)


