
''' 1.1 '''
name = "lesson"
num = 1
print("lesson ",num)

''' 1.2'''

times = 3910 # input("Enter times")
hh,ss= divmod(times,3600)
mm,ss=divmod(ss,60) 
print(f"time = {hh}:{mm}:{ss}")

''' 1.3'''

n = 3 # input("Enter n")
n=str(n)
summ = int(n) + int(n*2) + int(n*3)
print(summ)

''' 1.4'''

n = "12394569"# input("Enter n")
i=0
while i < 10:
	if str(i) in n:
		m=i
	i+=1
print(m)

''' 1.5'''

add =40 	 # input("Enter add")
minus = 20   # input("Enter minus")
employes =10 # input("Enter minus")

if add > minus:
	rent_sum = add / minus
	rent_emp= rent_sum / employes
	print(f'Profit rent_sum = {rent_sum} rent_emp = {round(rent_emp,3)}')
else:
	print('Loss')

''' 1.6'''

current= 2
target = 3
day = 0
while current <= target:
	day += 1
	current = current if day == 1 else current * 1.1

print(f"Target = {target}(km) Day = {day}")