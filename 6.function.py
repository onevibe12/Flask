def avg(*args):
	result = 0
	for i in args:
		result = result + i
	else:
		avg = result/4
		print(result)
		print(avg)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
avg(a,b,c,d)

print('--------------------------------------------------------------')

def say_myself(name, old, man=True): 
	print("나의 이름은 %s 입니다." % name) 
	print("나이는 %d살입니다." % old) 
	if man: 
		print("남자입니다.")
	else: 
		print("여자입니다.")

say_myself('Lee', 26, False)
