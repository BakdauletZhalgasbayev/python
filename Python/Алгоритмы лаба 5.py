#python "D:/Python/Алгоритмы лаба 5.py"
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [10, 11, 12, 13, 14, 15, 16, 17, 18]

print('Первый список :')
print(a)

print('Второй список :')
print(b)

print('второй элемент 1 списка :')
print(a[1])

b[-1] = 888
print('Изменение последнего элеммента 2 списка :')
print(b)

c = []
for i in range(len(a)):
	c.append(a[i])
for i in range(len(b)):
	c.append(b[i])

print('Объединение списков :')
print(c)

d = c[5:15]
print('Срез объединения:')
print(d)

d.append(5555)
d.append(7777)
print('Добавление 2 элементов в срез объединения :')
print(d)





'''S = list(A)

S[0], S[1] = S[1], S[0]

C = np.array(S)

print('\n')
print(S)

print('\n')
print(C)'''