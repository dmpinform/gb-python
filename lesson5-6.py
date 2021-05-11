file = open("text_6.txt", "r", encoding="UTF-8")
res = {}


def dig(str):
    num = ''.join(i for i in str if i.isdigit())
    return int(num) if len(num) > 0 else 0


with file as f_obj:
    for line in f_obj:
        subj, text = line.split(":")
        res[subj] = sum(map(dig, text.split("(")))

print(res)


