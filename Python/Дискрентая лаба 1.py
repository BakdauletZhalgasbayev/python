#python "D:/Док.py"
A = set('Онищук')
B = set('Михаил')
C = set('Андреевич')
#объединение
D = A.union(B)
E = A.union(C)
F = B.union(C)

print("Объединение А и В :")
print(D)
print("Объединение А и С :")
print(E)
print("Объединение В и С :")
print(F)

#пересечение
Q = A.intersection(B)
W = A.intersection(C)
R = B.intersection(C)
print("Пересечение А и В :")
print(Q)
print("Пересечение А и С :")
print(W)
print("Пересечение В и С :")
print(R)

#Raznost' A\B
T = A.difference(B)
print("Разность А и В :")
print(T)

#Raznost' B\A
Y = B.difference(A)
print("Разность B и A :")
print(Y)
# Simmetrich raznost'
U = A.symmetric_difference(B)
print("Симметрическая разность А и В :")
print(U)
