#python "D:/Python/nik.py" 
rang = int(input('enter x: '))

def enter(rang):
    try:
        for i in range(rang+1):
            print(i)
    except:
        print('Out of range')

enter(rang)