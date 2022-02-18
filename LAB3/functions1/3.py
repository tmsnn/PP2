def solve(numheads , numlegs):
   for x in range(numheads):
       for y in range(numlegs):
           if x + y == numheads and 2*x + 4*y == 94:
            print('number of chickens:')
            print(x)
            print('number of rabbits:')
            print(y)
solve(35, 94)