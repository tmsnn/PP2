n = int(input())
z = input()
if(z == "b"):
    print(n * 1024)
else:
    c = int(input())
    itog = "{:." + str(c) + "f}"
    print(itog.format(n / 1024))
        