import os 
 
WORKING_DIR = os.getcwd() 
 
for item in os.listdir(WORKING_DIR):  
  joined = os.path.join(WORKING_DIR, item) 
 
  print('Exist:', os.access(joined, os.F_OK)) 
  print('Readable:', os.access(joined, os.R_OK))  
  print('Writable:', os.access(joined, os.W_OK)) 
  print('Executable:', os.access(joined, os.X_OK))