#python "D:/Python/Test python.py" 
import random
print('Вариант 14 (0100)') 

x = input()
D = list(x)
B = [int(D[0]), int(D[1]), int(D[2]), int(D[3]) ]

c0 = ( B[0] + B[2] + B[3] )%2

c1 = ( B[0] + B[1] + B[3] )%2

c2 = ( B[1] + B[2] + B[3] )%2

C = [ c0, c1, c2 ]

print('Ваше сообщение :')
print(B)

print('Дополнительные биты для Вашего сообщения')
print(C)

print('Код Хемминга :')
BC = [ B[0], B[1], B[2], B[3], C[0], C[1], C[2] ]

print(BC)

###############################################################
print('-----------------------------')
A = B

####################Ошибка################

n = random.randint(0, (len(A) - 1) )

if A[n] == 0:
	A[n] = 1
else:
	A[n] = 0
print('Ваше сообщение с ошибкой :')
print(A)


d0 = ( A[0] + A[2] + A[3] )%2

d1 = ( A[0] + A[1] + A[3] )%2

d2 = ( A[1] + A[2] + A[3] )%2



print('Дополнительные биты с ошибкой :')

D = [ d0, d1, d2 ]
print(D)

print('Код Хемминга с ошибкой :')
AD = [ A[0], A[1], A[2], A[3], D[0], D[1], D[2] ]
print(AD)

print('Исправление :')

def chng():
	if D[0] != C[0] and D[1] != C[1]:
		if A[0] == 0 :
			A[0] = 1
		else:
			A[0] = 0
	
	if D[1] != C[1] and D[2] != C[2]:
		if A[1] == 0 :
			A[1] = 1
		else:
			A[1] = 0
	
	if D[0] != C[0] and D[2] != C[2]:
		if A[2] == 0 :
			A[2] = 1
		else:
			A[2] = 0
	
	
def chng3():
	if D[0] != C[0] and D[1] != C[1] and D[2] != C[2]:
		if A[3] == 0 :
			A[3] = 1
		else:
			A[3] = 0



if A[3] != B[3]:
	chng3()
else:
	chng()

print(A)