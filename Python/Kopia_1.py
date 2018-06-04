#python "D:/Python/Kopia_1.py"
A = [3,5,7,8]
R = [ [A[i//len(A)], A[i%len(A)]] for i in range(len(A)*len(A))
      if A[i//len(A)] < A[i%len(A)]]
M = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(A)*len(A)):
    if [A[i//len(A)], A[i%len(A)]] in R:
        M[i//len(A)][i%len(A)] = 1
    else:
        M[i//len(A)][i%len(A)] = 0

print("  y {} {} {} {}\nx".format(A[0], A[1], A[2], A[3]))
for i in range(len(A)):
    print("{}   {} {} {} {}".format(A[i],
                                    M[i][0], M[i][1], M[i][2], M[i][3]))
print("\n" + str(R))

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






