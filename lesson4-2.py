my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [val for i, val in enumerate(my_list[1:]) if val > my_list[i]]
print(new_list)
