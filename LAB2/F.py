n = int(input())
d = {}
for i in range(n):
    name, val = input().split()
    val = int(val)
    d[name] = d.get(name, 0) + val
mx = max(d.values())
for name, val in sorted(d.items()):
    if mx - d[name] == 0:
        print(f"{name} is lucky!")
    else:
        print(f"{name} has to receive {mx - d[name]} tenge" )

