from math import sqrt
def check(n):
    if n == 0 or n == 1: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n, f = map(int, input().split())
if n <= 500 and check(n) and f % 2 == 0:
    print('Good job!')
else:
    print('Try next time!')
