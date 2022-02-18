def checkpal(s):
    if(s == s[::-1]):
        return True
    else:
        return False

s = input()
if checkpal(s) == True:
    print(f'string "{s}" is palindrom')
else:
    print(f'string "{s}" is not palindrom')
