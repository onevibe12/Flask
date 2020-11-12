''' set 의 특징
중복을 허용하지 않는다
순서가 없다(Unordered)
'''
s1 = set([1,2,3,4,5,6,7])
print(s1)

s2 = set('hello')
print(s2)

ll = list(s2)
print(ll)

print('--------------------------------------------')
# 교집합 합집합 차집합 구하기 

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)		# 교집합
print(s1 | s2)		# 합집합
print(s1 - s2)		# 차집합
print(s2 - s1)		# 차집합

print('-------------------함수 ------------------------')
#  add() 값 추가하기 
s1 = set([1,2,3]) 
s1.add(4)
print(s1)

# update 값 여러개 추가하기
s1.update([5,6,7])
print(s1)

# remove() 특정 값 제거하기 
s1 = set([1,2,3])
s1.remove(2)
print(s1)





