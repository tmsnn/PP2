n = int(input()) 
for i in range(n): 
    for j in range(n):
        if (n % 2 == 0):
            if i >= j:
                print('#', end = '')
            else:
                print('.', end = '')
        elif n % 2 != 0:
            if (i + j == n - 1):
                print('#', end = '')
            elif i + j < n - 1:
                print('.', end = '')
            else:
                print('#', end = '')
    print()
