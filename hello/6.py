n = int(input())
spisok = []
for i in range(n):
    b = int(input())
    spisok.append(b)
for i in spisok:
    if(i <= 10):
        print('Go to work!')
    elif(i > 10 and i <= 25):
        print('You are weak')
    elif(i > 25 and i <= 45):
        print('Okay, fine')
    elif(i > 45):
        print('Burn! Burn! Burn Young!')
