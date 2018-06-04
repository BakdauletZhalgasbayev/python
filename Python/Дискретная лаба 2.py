#python "D:/Python/Дискретная лаба 2.py"
import random
A = [ random.randint(1,9) for i in range(7)]

print("\n" + 'Множество А(строка) : ' + "\n" )
print(list(A) )

B = [ random.randint(1,9) for i in range(6)]

print("\n" + 'Множество B(строка) : ' + "\n" )
print(list(B) )

r = [ [ A[i//len(A)], B[i%len(B) ] ] for i in range(len(A)*len(B)) ]
print("\n" + 'Отношение R(из списков) :' + "\n" )
print(r)

print("\n" + 'Множество А(не повторяющиеся элементы) : ' + "\n" )
print(set(list(A)) )

print("\n" + 'Множество В(не повторяющиеся элементы) : ' + "\n" )
print(set(list(B)) )

rr = [ r[i] for i in range(len(r)) if r.index(r[i]) >=i ]
print("\n" + 'Декартово произведение ' + "\n" )
print(rr)

R = [ rr[i] for i in range(len(rr)) if rr[i][0]%rr[i][1] == 0]
print("\n" + 'Отношение R (делиться без остатака) :' + "\n" )
print(R)

R2 = [ R[i][2] for i in range(len(R))]
print("\n" + 'Исключение 2-ой позиции :')
print(R2) 

R1 = [ [R[i][0], [ R[i][1], [ R[i][0] ] ] ] for i in range(len(R))] 
print("\n" + 'Удвоение 1-ой позиции :')
print(R1)