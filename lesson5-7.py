import json

file = open("text_7.txt", "r", encoding="UTF-8")
profit = {}
analytic_list = []
list_profit = []

with file as f_obj:
    for line in f_obj:
        name, typ, income, costs = line.split(" ")
        profit[name] = float(income) - float(costs)
        if profit[name] > 0:
            list_profit.append(profit[name])

analytic_list.append(profit)
analytic_list.append({"average_profit":
                          sum(list_profit) / len(list_profit)
                      })

file = open("text_777.json", "w", encoding="UTF-8")
with file as outfile:
    outfile.write(json.dumps(analytic_list, indent=2, ensure_ascii=False))
