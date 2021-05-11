file = open("text_5.txt", "w", encoding="UTF-8")
my_str = "1 2 3 4 11 9"
with file as f_obj:
    f_obj.writelines(my_str.strip())

file = open("text_5.txt", "r", encoding="UTF-8")
with file as f_obj:
    sum_in_file = sum(map(int, f_obj.readline().split(" ")))

print(sum_in_file)
