#python "D:/Python/4_Art.py"
import numpy as np
import random
m = int(input())
n = int(input())
E = [n, m]
A = np.zeros((m, n))

for i in range(m):
    for h in range(n):
        c = random.randint(0, 9)
        A[i][h] = c

print('\n')
print(A)

B = A

C = []
for i in range(n):
	C.append(int(max(A[i])))
print('\n')
print(C)

for i in range(max(E)):
 	c = max(C)
 	for idx, num in enumerate(A[i]):
 		B = A
 		if num == c:
 			for t in range(max(E)):
 				B[t][0], B[t][idx] = B[t][idx], B[t][0] 

print('\n')
print(B)

S = list(B)

for i in range(len(C)):
	if max(C) in B[i]:
		S[0], S[i] = S[i], S[0]

C = np.array(S)

print('\n')
print(C)

'''

'Cause I'm just a man
But as long as I got a mic, I'm godlike
So me and you are not alike
Bitch, I wrote "Stan"

'''
B = {
	('КарГТУ', 'ТехнБ'): [ A[0], A[1], 15 ],

	('КарГТУ', 'Ауэзова'):  [ A[0], A[4], 5 ],

	('КарГТУ', 'СГУ'): [ A[0], A[2], 25 ], 

	('КарГТУ', 'Гоголя'): [ A[0], A[5], 20 ],

	('ТехнБ', 'СГУ'): [ A[1], A[2], 15 ],

	('СГУ', 'Гоголя'): [ A[2], A[5], 15 ],
	
	('СГУ', 'Болашак'): [ A[2], A[6], 15 ],

	('СГУ', 'МГТУ'): [ A[2], A[3], 25 ],

	('СГУ', 'КарГУ'): [ A[2], A[7], 35 ],
	
	('МГТУ', 'КарГУ'): [ A[3], A[7], 20 ],
	
	('КарГУ', 'Болашак'): [ A[7], A[6], 35 ],

	('Болашак', 'Гоголя'): [ A[6], A[5], 15 ],
	
	('Ауэзова', 'Гоголя'): [ A[4], A[6], 25 ]
}


A = ['КарГТУ', 'ТехнБ', 'СГУ', 'МГТУ', 'Ауэзова',
    'Гоголя', 'Болашак', 'КарГУ' ]

B = {
	'КарГТУ, ТехнБ': [ A[0], A[1], 15 ],

	'КарГТУ, Ауэзова':  [ A[0], A[4], 5 ],

	'КарГТУ, СГУ': [ A[0], A[2], 25 ], 

	'КарГТУ, Гоголя': [ A[0], A[5], 20 ],

	'ТехнБ, СГУ': [ A[1], A[2], 15 ],

	'СГУ, Гоголя': [ A[2], A[5], 15 ],
	
	'СГУ, Болашак': [ A[2], A[6], 15 ],

	'СГУ, МГТУ': [ A[2], A[3], 25 ],

	'СГУ, КарГУ': [ A[2], A[7], 35 ],
	
	'МГТУ, КарГУ': [ A[3], A[7], 20 ],
	
	'КарГУ, Болашак': [ A[7], A[6], 35 ],

	'Болашак, Гоголя': [ A[6], A[5], 15 ],
	
	'Ауэзова, Гоголя': [ A[4], A[6], 25 ]
}
print(B[0])

C = {
	'КарГТУ': [ ['ТехнБ', 15], ['Ауэзова', 5], ['СГУ', 25], ['Гоголя', 20] ],
	'ТехнБ': [ ['КарГТУ', 15 ], ['СГУ', 15] ],
	'СГУ': [ ['КарГТУ', 25 ], ['ТехнБ', 15], ['Гоголя', 15],['Болашак', 15], [ 'МГТУ', 25 ], [ 'КарГУ', 25 ] ],
	'МГТУ': [ ['СГУ', 25], ['КарГУ', 20] ],
	'Ауэзова': [ ['КарГТУ', 5], ['Гоголя', 15], ['Болашак', 25] ],
	'Гоголя': [ ['КарГТУ', 20], ['Ауэзова', 15], ['СГУ', 15], ['Болашак', 15] ],
	'Болашак': [ ['КарГУ', 35], ['Ауэзова', 25], ['СГУ', 15], ['Гоголя', 15] ],
	'КарГУ': [ ['МГТУ', 20], ['СГУ', 35], ['Болашак', 35] ]
}
'''n = 0
for g in range(len(A)):
	for i in range(len(C[A[g]])):
		if C[A[g]] in C[A[g+1]]:

		n += C[A[g]][i][1]
		print(C[A[g]][i][1])

print(n)'''
A = [
	['КарГТУ', 'ТехнБ', 15 ],

	['КарГТУ', 'Ауэзова', 5 ],

	['КарГТУ', 'СГУ', 25 ], 

	['КарГТУ', 'Гоголя', 20 ],

	['ТехнБ', 'СГУ', 15 ],

	['СГУ', 'Гоголя', 15 ],
	
	['СГУ', 'Болашак', 15 ],

	['СГУ', 'МГТУ', 25 ],

	['СГУ', 'КарГУ', 35 ],
	
	['МГТУ', 'КарГУ', 20 ],
	
	['КарГУ', 'Болашак', 35 ],

	['Болашак', 'Гоголя', 15 ],
	
	['Ауэзова', 'Гоголя', 15 ],
	
	['Ауэзова', 'Болашак', 25 ]