#python "D:/Python/Алгоритмы лаба 7.py"
file = open('D:/Python/Laba.txt', 'w')
s = int(input('Количество студентов:'))
fio = 'ФИО'
tec = 'Текущие баллы:'
ball = 'Средний балл:'
file.write(fio + ' '*(30 - len(tec)) + tec + ' '*(10 - len(fio)) + ball + '\n' + '\n')
for i in range(s):
	c = []
	z = str()
	file = open('D:/Python/Laba.txt', 'a')
	a = input('Введите ФИО:')	
	print('Количество оценок:')
	d = input()
	print('Введите баллы:')
	for i in range(int(d)):
		b = int(input())
		c.append(b)			
		z += (str(c[i]) + ' ')
	file.write(str(a) + ' '*(20 - len(a)) + z + ' '*(25 - len(z))
		 + str(round(sum(c)/len(c))) + 
		'\n' + '\n')
file.close()



''''Cause I'm just a man
But as long as I got a mic, I'm godlike
So me and you are not alike
Bitch, I wrote "Stan"'''