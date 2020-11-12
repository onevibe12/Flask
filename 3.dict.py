# 쌍 추가하기 
a = {1: 'a'}	# 방법 1
a[2] = 'b'		# 방법 2 
print(a)

print('='* 50)

# del 딕셔너리 요소 삭제하기 

del a[1]
print(a)


'''
딕셔너리 주의 사항
Key 는 고유한 값이다 
Key 에서는 list 값을 쓸수 없다. 
하지만 tuple 은 Key로 사용가능하다

'''

print('===========================함수 알아보기===================')
# keys() 키 찾기
a = {1: 'a', 2: 'b'}
print(a.keys())


for k in a.keys():
	print(k)

# items() Key, Value 쌍 얻기
print(a.items()) 

# values() 값 찾기
print(a.values())

for k in a.values():
	print(k)

# 내용 비우기 모두 지우기 
a.clear()
print(a)

# get() Key 로 value 얻기
a = {1: 'a.value', 2: 'b.value'}
print(a.get(1))
print(a.get('foo','bar'))






