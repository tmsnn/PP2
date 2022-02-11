d = {'ONE':'1','TWO':'2','THR':'3','FOU':'4','FIV':'5','SIX':'6','SEV':'7','EIG':'8','NIN':'9',
'ZER':'0'}
s = input()
t = ''
for i in range(len(s)):
    if s[i:i + 3] in d.keys():
        t += d[s[i:i + 3]]
    elif s[i] == '+':
        t += '+'
num = str(sum(list(map(int, t.split('+')))))
reverse = {k:v for v,k in d.items()}
print(''.join(reverse[i] for i in num))