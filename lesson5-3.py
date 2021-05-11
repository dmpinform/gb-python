def wln(empl):
    return f"{empl['sn']}\t{empl['sal']}"


file = open("text_3.txt", "r", encoding="UTF-8")
sum_sal, empl_min_sal, cl = 0, [], 0
with file as f_obj:
    for line in f_obj:
        cl += 1
        name, sal = line.split(" ")
        sum_sal += float(sal)
        if float(sal) < 20000:
            empl_min_sal.append(name)

print("Salary < 20 000 : ", ",".join(empl_min_sal))
print("Salary AVG = ", sum_sal/cl)
