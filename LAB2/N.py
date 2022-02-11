l = list() 
l1 = list() 
while True: 
    n = int(input()) 
    if n == 0: 
        break 
    else: 
        l.append(n) 
for i in range((len(l) // 2)): 
    if i == len(l) - i: 
        print(l[i], end =' ') 
    else: 
        print(l[i] + l[len(l)-1 - i], end = ' ') 
if len(l) % 2 == 0: 
    pass 
else: 
    l1.append(l[len(l)//2]) 
print(*l1)
   

