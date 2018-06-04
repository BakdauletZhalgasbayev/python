def ob(line):
    N = []
    i = 0
    s = ""
    c = 1
    for i in range(len(line)):
        if line[i] == ",":
            if c%2 == 0:
                N.append(float(s))
            c += 1
        elif line[i] == " ":
            s = ""
        else:
            s = str(s) + str(line[i])
    return N


M = [0.1, 5.6, 0.8, 2.4, 7.3, 6.8, 0.5, 2.3]
f = open("X.txt","w")
for i in range(len(M)):
    f.write(str(M[i])+", ")
f.close()

N = []
f = open("X.txt","r")
for line in f:
    s = str(line)
    N = N + ob(line)
f.close()

f = open("Y.txt","w")
for i in range(len(N)):
    f.write(str(N[i])+", ")
f.close()


print("X: "+str(M))
print("Y: "+str(N))
