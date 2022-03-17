# mylist = tuple(input('input your tuple: ').split())
# x = all(mylist)
# print(x)
t = input()
a = tuple(int(x) for x in t.split())
#view this tuple
print(all(a))
