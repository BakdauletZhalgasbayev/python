#python "D:/Python/Алгоритмы лаба 6.py"
import random

a = int(input('Введите начало диапазона :'))
b = int(input('Введите конец диапазона :'))
c = []
f = b - a
def massive(x, y):
	for i in range(f):
		v = random.randint(x, y)
		c.append(v)
		x += 1
massive(a, b)
print(c)