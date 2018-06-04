#python "D:/Python/Дискретная лаба 6(2).py"
from copy import *
A = [1,2,4,7,14,36,36]
M = []
for i in range(sum(A)):
	M.append(i)
B = 0
C = 0
D = 0
E = 0
F = 0
H = 0
K = 0
S1 = []
def summa(a, b, c, d, e, f, k):
	for i in range(len(A)):
		b = copy(a)
		b[i] = 0
		s1 = sum(b)
		S1.append(s1)
		for i in range(len(A)):
			c = copy(b)
			c[i] = 0
			s2 = sum(c)
			S1.append(s2)
			for i in range(len(A)):
				d = copy(c)
				d[i] = 0
				s3 = sum(d)
				S1.append(s3)
				for i in range(len(A)):
					e = copy(d)
					e[i] = 0
					s4 = sum(e)
					S1.append(s4)
					for i in range(len(A)):
						f = copy(e)
						f[i] = 0
						s5 = sum(f)
						S1.append(s5)
						for i in range(len(A)):
							h = copy(f)
							h[i] = 0
							s6 = sum(h)
							S1.append(s6)
							for i in range(len(A)):
								k = copy(h)
								k[i] = 0
								s7 = sum(k)
								S1.append(s7)
	return list(set(S1))	
for i in range(len(A)):
	A = [1,2,4,7,14,36,36]
	A[i] = 0
	summa(A, B, C, D, E, F, K)
N = list(set(S1))
for i in range(len(N)):
	if N[i] != M[i]:
		print('Дан массив ' + str(A))
		print('из данных чисел не возможна сумма ' + str(M[i]))
		break
