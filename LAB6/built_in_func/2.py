# Write a Python program with builtin function that accepts a string and calculate 
# the number of upper case letters and lower case letters
s = input() 
cnt_upper,cnt_lower = 0,0 
 
for i in s: 
    if (i.islower()): 
        cnt_upper=cnt_upper+1                  
    elif (i.isupper()): 
        cnt_lower = cnt_lower +1    
           
print('Lower case letters: ', cnt_upper) 
print('Upper case letters: ', cnt_lower)


