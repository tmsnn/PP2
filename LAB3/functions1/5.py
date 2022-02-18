import itertools
def permut(s):
    ans = itertools.permutations(s)
    for i in ans:
        print(*i, end = '')
        print()

s = input()
permut(s)