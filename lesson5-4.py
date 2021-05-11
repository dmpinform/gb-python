file = open("text_4.txt", "r", encoding="UTF-8")
dict_tre = {"One": "Один", "Two": "Два", "Three":"Три", "Four": "Четыре"}
list_new_text = []

with file as f_obj:
    for line in f_obj:
        words = line.split(" ")
        newline = " ".join(dict_tre.get(trl) if dict_tre.get(trl) is not None else
                           trl for trl in words)
        list_new_text.append(newline)

file = open("text_4_translate.txt", "w", encoding="UTF-8")
with file as f_obj:
    f_obj.writelines(list_new_text)
