#python "D:/Programm2.py"
A = set()
import random
for i in range(13):
	a = random.randint(0, 14)
	A.add(a)
print(A)

B = set()
import random
for i in range(13):
	a = random.randint(0, 14)
	B.add(a)
print(B)
C = A.intersection(B)

print('Множество А : ' + str(A))
print('Множество B : ' + str(B))
print('Условия подмножеств :')
print (A.issubset(B))
print (B.issubset(A))
print('Условиe равенства :')
print(A == B)
print('Пересечение : ')
print(A.intersection(B))
if not C == set(): 
	print('Пересечение А и В не пустое')