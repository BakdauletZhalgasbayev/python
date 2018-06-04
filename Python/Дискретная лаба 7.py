#python "D:/Python/Дискретная лаба 7.py"
a = [1, 2, 3]
b = [[1,  1,  0],
     [1,  0,  1], 
     [0,  1,  1]]
print('Матрица смежности первого графа:')
print('   {}  {}  {}  \n'.format(a[0], a[1], a[2]))

for i in range(len(a)):
	print('{}  {}  {}  {}\n'.format(a[i], b[i][0], b[i][1],
	                                        b[i][2]))


print('Количество ребер данного графа: 6')

c = []
for i in range(4):
	c.append(i+1)

d = [ [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0] ]
for i in range(len(b)):
	for h in range(len(b[i])):
		if b[i][h] == 1 and b[h][i] == 1:
			
			d[0][0] = 1
			
			d[0][1] = 1
			d[1][1] = 1

			d[1][2] = 1
			d[2][2] = 1

			d[2][3] = 1


print('\n')
print('Матрица инцидентности первого графа:')
print('\n')
print('По горизонтали(1-4) - номер ребра, По вертикали(1-3) - номер вершины:')
print('\n')
print('   {}  {}  {}  {}\n'.format(c[0],c[1], c[2], c[3]))

for i in range(len(a)):
	print('{}  {}  {}  {}  {}\n'.format(a[i], d[i][0], d[i][1], d[i][2], d[i][3]))

print('\n')
a = [1, 2, 3, 4, 5]