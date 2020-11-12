a =  "Life is too short, you need python"
if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# ---------------------------------------------------
num = 1
sum = 0
while num <= 1000:
	if num % 3 == 0:
		sum += num
	num += 1
else:
	print(sum)
# -------------------------------------------------

i = 0
while i <= 5:
	i += 1
	print('*' * i)

# --------------------------------------------------


numbers = [1,2,3,4,5]
result = [i*2 for i in numbers if i % 2 == 1]
print(result)

# -------------------------------------------------

a = [70,60,55,75,95,90,80,80,85,100]
result = 0
for i in a:
	result += i
else:
	avg = result / len(a)
	print('%0.1f'%avg)
