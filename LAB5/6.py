# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re 
text = input() 
print(re.sub("[ ,.]", ":", text))