import os 
 
WORKING_DIR = os.getcwd() 
 
print("DIRS:") 
for item in os.listdir(WORKING_DIR):  
  joined = os.path.join(WORKING_DIR, item) 
   
  if os.path.isdir(joined): 
    print(f'DIR: {item}') 
 
print("ALL DIRS AND FILES:") 
for item in os.listdir(WORKING_DIR):  
  joined = os.path.join(WORKING_DIR, item) 
   
  if os.path.isdir(joined): 
    print(f'DIR: {item}') 
 
  if os.path.isfile(joined): 
    print(f'FILE: {item}') 
 
print("FILES:") 
for item in os.listdir(WORKING_DIR):  
  joined = os.path.join(WORKING_DIR, item) 
  if os.path.isfile(joined): 
    print(f'FILE: {item}')