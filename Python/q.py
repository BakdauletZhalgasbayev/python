import random
alphabet = ['а', 'б', 'в', 'г','д','е','ё','ж','з','и',
            'к','л','м','н','о','п','р','с','т','у','ф',
            'х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
numbers = [2, 4, 6, 8]
string = None
for i in range(10):
    n = random.randint(0, 31)
    m = random.randint(0, 3)
    if string == None and i%2 == 0:
        string = alphabet[n]
    elif i%2 == 0:
        string = string + alphabet[n]
    elif i%2 != 0:
        string = string + str(numbers[m])
print(string)