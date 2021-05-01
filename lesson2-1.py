mylist = [1, "one", {1, 2, 3}, {"1": "one", "2": "two"}, (1, 2), [1, 2]]
for i in mylist:
	t = type(i)
	if t == int:
		print("int")
	elif t == str:
		print("str")
	elif t == set:
		print("set")
	elif t == dict:
		print("dict")
	elif t == tuple:
		print("tuple")
	elif t == list:
		print("list")
