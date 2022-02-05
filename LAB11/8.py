s = input()
ch = input()
a = -1
b = -1
for i in range(len(s)):
    if (s[i] == ch):
       a = i
       break
i = len(s)-1
while i != 0:
    if(s[i] == ch and i != a):
        b = i
        break
    i -= 1
if(a != -1 and b != -1):
    print(a, b)
elif(a != -1 and b == -1):
    print(a)