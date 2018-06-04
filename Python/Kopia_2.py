#python "D:/Python/Kopia_2.py"
import random
A = [random.randint(1,9) for i in range(10)]
B = [random.randint(1,9) for i in range(10)]
a = [A[i] for i in range(len(A)) if A.index(A[i]) >= i]
b = [B[i] for i in range(len(B)) if B.index(B[i]) >= i]
aRb = [[a[i//len(b)], b[i%len(b)]] for i in range(len(a)*len(b))]
R = [ aRb[i] for i in range(len(aRb)) if aRb[i][0]%7 == aRb[i][1]%7]
m = [ [] for i in range(len(R))]
M = [ [] for i in range(len(R))]
for i in range(len(R)):
    M[i] = list(m)

for i in range(len(R)*len(R)):
    if R[i//len(R)] in R:
        M[i//len(R)][i%len(R)] = 1
    else:
        M[i//len(R)][i%len(R)] = 0
    
for i in range(len(R)):
    print(M[i])
    print("")

def ref(M):
    f = 0
    for i in range(len(M)):
        if M[i][i] == 0:
            f += 1
    if f == 0:
        print("Рефлексивно")

    f = 0
    for i in range(len(M)):
        if M[i][i] == 1:
            f += 1
    if f == 0:
        print("Антирефлексивно")

def sim(M):
    f = 0
    for i in range(len(M)*len(M)):
        if M[i//len(M)][i%len(M)] == 1:
            if M[i%len(M)][i//len(M)] != 1:
                f += 1
    if f == 0:
        print("Симметрично")


    f = 0
    t = 0
    for i in range(len(M)*len(M)):
        if M[i//len(M)][i%len(M)] == 1:
            if M[i%len(M)][i//len(M)] == 1:
                if i%len(M) == i//len(M):
                    e = 1
                else:
                    f += 1
    for i in range(len(M[0])):
        if M[i][i] == 1:
            t += 1
    if t != len(M[0]):
        f = 1
    if f == 0:
        print("Антисимметрично")


def trn(M):
    f = 0
    for i in range((len(M)-1)*(len(M)-1)):
        if i//(len(M)-1) != i%(len(M)-1):
            if M[i//(len(M)-1)][i%(len(M)-1)] == M[i//len(M)][i%len(M)] == 1:
                if M[i//(len(M)-1)][i%(len(M)-1)] != 1:
                    f += 1
    if f == 0:
        print("Транзитивно")
    else:
        f = 0
        for i in range((len(M)-1)*(len(M)-1)):
            if i//(len(M)-1) != i%(len(M)-1):
                if M[i//len(M)][i%len(M)] == M[i//(len(M)-1)][i%(len(M)-1)] == 1:
                    if M[i//len(M)][i%(len(M)-1)] != 1:
                        f += 1
        if f == 0:
            print("Транзитивно")
                

ref(M)
sim(M)
trn(M)
print(R)
