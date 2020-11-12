languages = ['python', 'perl', 'c', 'java']

for lang in languages:
	if lang in ['python', 'perl']:
		print("%6s need interpreter" % lang)
	elif lang in ['c', 'java']:
		print("%6s need compiler" % lang)
	else:
		print("should not reach here")

print('----------------------문자열-----------------------------')

food = "Python's favorite food is perl"
print(food)

print('----------------------쿼우팅----------------------------')

multiline="""
Life is too short
You need python
"""
print(multiline)

print('-----------------------format-----------------------------')

num = 3
string = 'apples'
print ('I eat %d bannaa' % num)
print ('I eat 3 %s' %string )
print ('I eat %d %s' %(num,string))
print ('I eat {num} {str}'.format(num=3, str='tt'))
	   
print('-------------------------list---------------------------')

a = [1,2,3]
b = [4,5,6]
c = []
c = a+b
print(a)
print(b)
print(c)

# 값 수정 가능
a[2] = 'b'
print(a)

print('---------------------------list function---------------------')
# del 함수 리스트 요소 삭제
a = [1,2,3]
del a[1]   # 2 삭제
print(a)

a = [1,2,3,4,5,6,7,8,9,10]
del a[2:]
print(a)

# 요소 추가 append
a = [1,2,3]
a.append(1)
print(a)
a.append('string')
print(a)

# sort 정렬 Tip! string 과 int 자료형이 같이 있으면 안된다.
a = [3,1,2]
b = ['c','a','b']
#c = [3,1,'a',2]   # error 출력
a.sort()
b.sort()
c.sort()
print(a)
print(b)
print(c)

# reverse 뒤집기 Note. 단순히 현재 상태를 뒤집을 분 정렬이 아니다
a = [3,1,2]
b = ['c','a','b']
a.reverse()
b.reverse()
print(a)   
print(b)
a.sort(reverse=True)  # Tip. 정렬은 이렇게 사용가능하다
b.sort(reverse=True)
print(a)
print(b)

# index 위치반환 Note. 해당 위치에x의 값이 있으면 위치값을 돌려줌
a = [1,2,3]
print(a.index(3))
b = ['a','b','c']
print(b.index('b'))


# insert 요소 삽입 
a = [1,2,3,4,5]
a.insert(1, 't')
print(a)

# remove 요소 제거
a = [1,2,3,4,'t',5]
a.remove('t')
print(a)

a = [1,2,3,4,'t',5]
a.pop(3)
print(a)

a = [1,2,3]
x = ['a','b','c']
a.extend(x)   # Note. (x)의 위치에는 list형식만 올 수 있다
print(a)
a.extend('t')
