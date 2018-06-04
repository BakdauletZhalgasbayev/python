#python "D:/Python/Дискретная лаба 4.py"
import random
def d(X,Y):
    Z = list(range(len(X)))
    for i in range(len(X)):
        if X[i] == 0 and Y[i] == 0:
            Z[i] = 0
        elif X[i] == 1 and Y[i] == 0:
            Z[i] = 1
        elif X[i] == 0 and Y[i] == 1:
            Z[i] = 1
        elif X[i] == 1 and Y[i] == 1:
            Z[i] = 1
    return Z
def k(X,Y):
    Z = list(range(len(X)))
    for i in range(len(X)):
        if X[i] == 0 and Y[i] == 0:
            Z[i] = 0
        elif X[i] == 1 and Y[i] == 0:
            Z[i] = 0
        elif X[i] == 0 and Y[i] == 1:
            Z[i] = 0
        elif X[i] == 1 and Y[i] == 1:
            Z[i] = 1
    return Z
def n(X):
    Z = list(range(len(X)))
    for i in range(len(X)):
        if X[i] == 1:
            Z[i] = 0
        elif X[i] == 0:
            Z[i] = 1
    return Z
def sdnf(X):
    ans = ""
    for i in range(len(X)):
        if X[i] == 1:
            if i != 0:
                ans += "+"
            if A[i] == 1:
                ans += "(A"
            else:
                ans += "((nA)"
            if B[i] == 1:
                ans += "B"
            else:
                ans += "(nB)"
            if C[i] == 1:
                ans += "C"
            else:
                ans += "(nC)"
            if D[i] == 1:
                ans += "D"
            else:
                ans += "(nD)"
            if E[i] == 1:
                ans += "E)"
            else:
                ans += "(nE))"
    return ans
def sknf(X):
    ans = ""
    for i in range(len(X)):
        if X[i] == 0:
            if A[i] == 0:
                ans += "(A+"
            else:
                ans += "((nA)+"
            if B[i] == 0:
                ans += "B+"
            else:
                ans += "(nB)+"
            if C[i] == 0:
                ans += "C+"
            else:
                ans += "(nC)+"
            if D[i] == 0:
                ans += "D+"
            else:
                ans += "(nD)+"
            if E[i] == 0:
                ans += "E)"
            else:
                ans += "(nE))"
    return ans
A = [ i//16%2 for i in range(2**5)]
B = [ i//8%2 for i in range(2**5)]
C = [ i//4%2 for i in range(2**5)]
D = [ i//2%2 for i in range(2**5)]
E = [ i//1%2 for i in range(2**5)]
f1 = d(d(k(A,B),k(C,n(D))),n(E))
f2 = d(k(d(A,B),d(C,n(D))),E)
print("A: " + str(A))
print("B: " + str(B))
print("C: " + str(C))
print("D: " + str(D))
print("E: " + str(E))
print("----------------")
print("f1   : " + str(f1))
print("f2   : " + str(f2))
print("----------------")
if f1 == f2:
    print("true")
else:
    print("false")
print("----------------")
A = [ i//16%2 for i in range(2**5)]
B = [ i//8%2 for i in range(2**5)]
C = [ i//4%2 for i in range(2**5)]
D = [ i//2%2 for i in range(2**5)]
E = [ i//1%2 for i in range(2**5)]
print("A: " + str(A))
print("B: " + str(B))
print("C: " + str(C))
print("D: " + str(D))
print("E: " + str(E))
f3 = d(k(d(A,B),d(C,n(D))),n(E))
print("----------------")
print("f3   : " + str(f3))
print("----------------")
print("sdnf : " + str(sdnf(f3)))
print("----------------")
print("sknf : " + str(sknf(f3)))
print("----------------")