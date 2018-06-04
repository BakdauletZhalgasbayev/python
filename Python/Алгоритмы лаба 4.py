#python "D:/Python/Алгоритмы лаба 4.py"
import numpy as np
import random 
print('Введите N:')
n = int(input())
print('Введите M:')
m = int(input())

A = np.zeros((n, m))

for i in range(n):
	for h in range(m):
		c = random.randint(0, 9)
		A[i][h] = c

print(A)
print('\n')
print('вычитание последней строки из всех строк:')
print('\n')
v = int(n/n)
for i in range(n-1):
	A[v - 1] = A[v - 1] - A[n-1]
	v += 1
print(A)