words = input().replace('?','').replace(',','').replace('.','').replace('!','').split()
s = set()
for word in words:
    s.add(word)
print(len(s))
print(*sorted(s),sep='\n')