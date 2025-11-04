# mylist = [1,2,3,4]
# Itertool = iter(mylist)
# print(Itertool)
# print(next(Itertool))
# print(next(Itertool))
# print(next(Itertool))
# print(next(Itertool))

def calc_sq(a):
    return a*a

import math


def calc_sq(a,b):
    return (a*a) * (b*b)


# print(calc_sq(4))
# print(calc_sq(2,3))

def pm_ar(r):
    pm = math.pi * r * 2
    ar = math.pi * r * r

    return pm,ar

ans = pm_ar(4)

print(ans)


def calc_sq(*args):
    for arg in args:
        yield arg*arg


result = calc_sq(2, 3, 4, 5)

for val in result:
    print(val)
