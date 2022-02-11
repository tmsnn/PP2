l = list()
while True:
    data = input()
    if data == '0':
        break
    else:
        a = data.split()
        l.append(a[2] + ' ' + a[1] + ' ' + a[0])
for data in sorted(l):
    data = data.split()
    print(f'{data[2]} {data[1]} {data[0]}')