def BintoDec(s):
    if len(s) == 1:
        return int(s)
    else:
        return BintoDec(s[-1]) + 2*BintoDec(s[:-1])
s = str(input())
print(BintoDec(s))