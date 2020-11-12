class Calculator:
	def __init__(self):
		self.result = 0

	def add(self, num):
		self.result += num
		return self.result

	def sub(self, num1, num2):
		self.result = num1 - num2
		return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(5))
print(cal1.add(5))
a = cal1.add(10)
print(cal2.sub(a, 5))

