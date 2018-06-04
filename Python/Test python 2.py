#python "D:/Python/Test python 2.py" Алгоритмы лаба 4.py
import random
print('Вариант 14 (0100)') 

x = input()
D = list(x)
B = [int(D[0]), int(D[1]), int(D[2]), int(D[3]) ]

c0 = ( B[0] + B[1] + B[3] )%2

c1 = ( B[0] + B[2] + B[3] )%2

c2 = ( B[1] + B[2] + B[3] )%2

C = [ c0, c1, c2 ]

print('Ваше сообщение :')
print(B)

print('Дополнительные биты для Вашего сообщения')
print(C)

print('Код Хемминга :')
BC = [ C[0], C[1], B[0], C[2], B[1], B[2], B[3] ]

print(BC)
###############################################################
print('-----------------------------')
####################Ошибка################
n = random.randint(0, (len(BC) - 1) )
if BC[n] == 0:
	BC[n] = 1
else:
	BC[n] = 0

print("Код с ошибкой\n" + str(BC))

print('Исправление :')
	
def chng3(AD):
	A = [AD[2], AD[4], AD[5], AD[6]] 
	D = [AD[0], AD[1], AD[3]]

	c0 = ( A[0] + A[1] + A[3] )%2

	c1 = ( A[0] + A[2] + A[3] )%2

	c2 = ( A[1] + A[2] + A[3] )%2

	C = [c0,c1,c2]

	error = 0
	for i in range(3):
		if D[i] != C[i]:
			error += 1

	print(A,D,C)

	if error == 3:
		if A[3] == 0 :
			A[3] = 1
		else:
			A[3] = 0

	if error == 2:
		if D[0] != C[0] and D[1] != C[1]:
			if A[0] == 0 :
				A[0] = 1
			else:
				A[0] = 0


		if D[1] != C[1] and D[2] != C[2]:
			if A[2] == 0 :
				A[2] = 1
			else:
				A[2] = 0


		if D[0] != C[0] and D[2] != C[2]:
			if A[1] == 0 :
				A[1] = 1
			else:
				A[1] = 0
	
	if error == 1:
		if D[0] != C[0]:
			if D[0] == 0 :
				D[0] = 1
			else:
				D[0] = 0

		if D[1] != C[1] :
			if D[1] == 0 :
				D[1] = 1
			else:
				D[1] = 0


		if D[2] != C[2]:
			if D[2] == 0 :
				D[2] = 1
			else:
				D[2] = 0
	newAD = [ D[0], D[1], A[0], D[2], A[1], A[2], A[3] ]
	return newAD
print(str(chng3(BC)))