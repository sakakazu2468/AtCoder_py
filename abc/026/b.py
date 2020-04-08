import math


n = int(input())
r = []
for i in range(n):
    r.append(int(input()))
r = sorted(r, reverse=True)
ri = 0
for i in range(n):
    if i%2 == 0:
        ri += r[i]**2
    else:
        ri -= r[i]**2
print(math.pi*ri)
