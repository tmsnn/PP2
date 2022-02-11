low, upper, digit = 0, 0, 0 
n = int(input()) 
sozder = set() 
for i in range(n): 
    s = input() 
    sozder.add(s) 
ll=list() 
for s in sozder: 
    low, upper, digit = 0, 0, 0   
    for i in s: 
        if (i.islower()): 
            low+=1    
        if (i.isupper()): 
            upper+=1    
        if (i.isdigit()): 
            digit+=1    
    if (low >= 1 and upper >= 1 and digit >= 1): 
        ll.append(s) 
print(len(ll)) 
for i in sorted(ll): 
    print(i)
     