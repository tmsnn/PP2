import os 
path='C:\\Users\\Acer\\PP2\\LAB6\\dir_and_files\\del.txt' 
 
 
print(path) 
 
if os.access(path, os.F_OK): 
 
    os.remove('del.txt') 
    print('File deleted') 
 
else: 
    print('File does not exist')