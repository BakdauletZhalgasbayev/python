#python "D:/Python/Дискретная лаба 6(1).py"
from math import *
n = int(input())
m = int(input())
a = factorial(n)
b = factorial(n - m)
print(a)
print(b)
A = ( a ) / ( b )
print(int(A))