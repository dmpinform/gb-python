file = open("text_2.txt", "r")
line_count = 0
res = {}
with file as f_obj:
    for line_count, line in enumerate(f_obj):
        res[line_count] = len(line.split(" "))

print("Count all lines = %s" % (line_count+1),
      list(f"line №{i+1} - {c} words" for i, c in res.items()))
