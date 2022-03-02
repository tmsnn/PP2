import math
from math import cos, sin
n = int(input('Input number of sides: '))
a = int(input('Input the length of a side: '))
print('The area of the polygon is: ', end = '')
print(int(n * pow(a, 2) * cos(math.pi / n)/(sin(math.pi / n)) / 4))