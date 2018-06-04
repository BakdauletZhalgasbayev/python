#python "D:/Python/1.py"
def fac(b):
    if b == 1:
        return 1
    else:
        return b*fac(b-1)
print(str(int(fac(9)/(fac(5)*fac(9-5)))))
print("способов покрасить 5 шаров в черный цвет")
#Визуализация:
'''import copy
balls = [0,0,0,0,0,0,0,0,0]
def check(b):
    c = 0
    for i in range(len(b)):
        if b[i] == 1:
            c += 1
    return c
def nextt(b,a):
    if b[len(b)-a] == 0:
        b[len(b)-a] = 1
        return b
    else:
        b[len(b)-a] = 0
        nextt(b,a+1)
        return b
def show(b):
    s = ""
    for i in range(len(b)):
        s = str(s) + str(b[i])
    return s
answer = []
for i in range(2**9):
    if check(balls) == 5:
        answer.append(copy.copy(balls))
    balls = nextt(balls,1)
print(str(len(answer)) + str(" - способов покрасить 5 шаров в черный цвет"))
print()
for i in range(len(answer)//4):
    print("{}   {}   {}   {}".format(show(answer[i*4]),show(answer[i*4+1]),show(answer[i*4+2]),show(answer[i*4+3])))
s = ""
for i in range(len(answer)%4):
    s = str(s) + str(show(answer[(len(answer)//4)*4 + i])) + "   "
print(s)'''