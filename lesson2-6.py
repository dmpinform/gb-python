prod_list = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

newdict = {}

for item in [k[1] for k in prod_list]:
    for k, v in item.items():
        if newdict.get(k) is None:
            newdict[k] = {v}
        else:
            newdict[k].add(v)

newdict = {k: list(v) for k, v in newdict.items()}

print(newdict)
