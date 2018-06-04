#python "D:/Python/4.py"
import numpy as np
A = np.zeros((101))
c = -50
for i in range(101):
    A[i] = c
    c += 1 
print(A)
print('\n')
for i in range(101):
    if A[i] < 0:
        A[i] = abs(A[i])
print(A)