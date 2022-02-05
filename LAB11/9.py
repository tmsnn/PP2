"""
Problem I: 189327. Dimash that's too bad.
Dimash hacked the database and he got all the email addresses to send out spam. But Dimash’s program works differently.
The program should only receive logins from @gmail.com
Help the young hacker get the logins. Help him do it!!!
"""
n = int(input())
for i in range(n):
    s = str(input())
    if "@gmail.com" in s:
        print(s.replace("@gmail.com", ""))