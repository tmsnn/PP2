zhaqsha = input()
l = []
for i in range(len(zhaqsha)):
    if zhaqsha[i] == '[' or zhaqsha[i] == '(' or  zhaqsha[i] == '{':
        l.append(zhaqsha[i])
    elif zhaqsha[i] == ']'or zhaqsha[i] == ')'or zhaqsha[i] == "}":
        if (len(l) > 0):
            if (l[-1] == '[' and zhaqsha[i] == ']') or (l[-1] == '(' and zhaqsha[i] == ')') or (l[-1] == '{' and zhaqsha[i] == '}'):
                l.pop(-1)
            else:
                l.append(zhaqsha[i])
if len(l) > 0:
    print('No')
else:
    print('Yes')

