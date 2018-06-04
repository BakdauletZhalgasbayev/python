#python "D:/Python/2.py"
import copy
A = [1,2,7,14,36,36]
payment = []
answer = []
def plus(b,c):
    if c == 1:
        return b[0]
    else:
        return str(plus(b,c-1)) + "+" + str(b[c-1])
def pls(b,c):
    if c == 1:
        return b[0]
    else:
        return pls(b,c-1) + b[c-1]
def chose(b,p):
    if pls(b,len(b)) == p:
        if str(plus(b,len(b))) not in payment:
            payment.append(str(plus(b,len(b))))
    else:
        for i in range(len(b)):
            bb = copy.copy(b)
            del bb[i]
            if len(bb) != 0:
                chose(bb,p)
s = ""
for i in range(len(A)):
    if i+1 == len(A):
        s = str(s)+str(A[i])
    else:
        s = str(s)+str(A[i])+" <= "
print("Для массива: "+str(s)+" ;")
c = 0
for i in range(sum(A)-1):
    chose(A,i+1)
    if len(payment) < i+1-c:
        answer.append(int(i+1))
        c += 1
print("Первое число, непредставимое суммой никаких элементов массива: " + str(answer[0]))