"""
Problem C: 187587. To Lowercase.
Given a string s. Create a function toLowercase that will replace every uppercase in s with the same lowercase letter and return the lowercase string.

Input format
String s.

Output format
Print the string that you will get as a result of the toLowercase function.
"""
string = input()
def toLowercase():
    t = ""
    for i in string:
        if(i >= 'A' and i <= 'Z'):
            i = chr(ord(i) + 32)
        t += i
    print(t)
toLowercase()
