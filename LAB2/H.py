def dis(x,y,x2,y2):
    return (x-x2)*(x-x2)+(y-y2)*(y-y2)
dict = {}
x,y = map(int,input().split())
n = int(input())
for i in range(n):
    m,l = map(int,input().split())
    d = dis(x,y,m,l)
    if d not in dict:
        dict[d] = [m,l]
    else:
        dict[d].append(m)
        dict[d].append(l)
for k in sorted(dict.keys()):
      c = dict[k]
      if len(c)>2:
          for i in range(0,len(c),2):
              print(c[i],c[i+1])
      else:
          print(*dict[k])