fruits = ['apple', 'banana', 'mandarin', 'watermelon', 'pear'] 
 
# open file in write mode 
with open(r'C:/Users/Acer/PP2/LAB6/dir_and_files/tasks.txt', 'w') as fp: 
    for item in fruits: 
        # write each item on a new line 
        fp.write(f'{item} \n') 
    print('Done, krasavchik!')