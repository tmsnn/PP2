import random
def Guess_the_number():
    name = input('Hello! What is your name?: ')
    print(f'Well, {name}, I am thinking of a number between 1 and 20.', sep = '\n')
   #  print('Take a guess', sep = '\n')
   #  n = int(input())
    cnt = 0
    m = random.randint(1,20)
   #  print(m)
    while cnt < 20:
         cnt += 1
         n = int(input('Take a guess: '))
         if n == m:
            print (f'Good job, {name}! You guessed my number in {cnt} guesses!')
            break
         elif m != n:
            print('Your guess is too low.', sep = '\n')
            # print('Take a guess' , sep = '\n')
(Guess_the_number())


