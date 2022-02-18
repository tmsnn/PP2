from cmath import pi


def get_volume(r):
    # r = int(input())
    v = (4 / 3) * pi * (r**3)
    print(v)
r = int(input())
get_volume(r)