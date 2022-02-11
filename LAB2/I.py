n = int(input())
put, take = [], []
for i in range(n):
    shelf = input().split()
    if len(shelf) == 2:
         disks = (shelf[1])
         put.append(disks)
    else:
        take.append(put[0])
        put.pop(0)
print(*take)