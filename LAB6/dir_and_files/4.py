file = open('C:/Users/Acer/PP2/LAB6/dir_and_files/line.txt',"r")  
cnt  = 0 
text = file.read()  
list = text.split("\n")  
 
for x in list:  
    if x:  
        cnt += 1 
   
print("lines in txt file:", cnt )