t1 = ()
t2 = (1,)		# 1개의 원소일경우 ',' 를 꼭 붙여야 한다
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a', 'b', ('ab', 'cd'))
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

print('='*50)

# ----------------------------튜플 값 지우기----------------
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2
print(t3)
