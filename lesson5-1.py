file = open("text_1.txt", "w")
text = "-"
with file as f_obj:
    while text != "":
        text = input("Enter string ")
        print(text, file=f_obj)
