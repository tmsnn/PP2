l = list(map(int, input().split())) 
position = len(l)-1 
for i in range(len(l)-2, -1, -1): 
    if i + l[i] >= position: 
        position = i 
if position != 0: 
    print('0') 
else: 
    print('1')