#python "D:/Python/Алгоритмы лаба 3.py"
from random import *
A = []
for i in range(20):
	a = randint(1, 21)
	A.append(a)
B = set(A)
print(A)
print(B)
C = list(B)
print(C)