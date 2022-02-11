n = int(input()) 
for row in range(n): 
    for col in range(n): 
        if row == 0: 
            print(col, end=" ") 
        elif col == 0: 
            print(row, end=" ")    
        elif row == col: 
            print(row * col, end= " ") 
        else: 
            print(0, end=" ")              
    print()