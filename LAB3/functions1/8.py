def spy_game(): 
    l = list(map(int, input().split())) 
    s = '' 
    for i in l: 
        if (i == 0 or i == 7): 
            s += str(i) 

    for i in range(len(s) - 2):
        return True if(s[i] == '0' and s[i + 1] == '0' and s[i + 2] == '7') else False
        
print(spy_game())
    