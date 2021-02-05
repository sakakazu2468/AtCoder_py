import math

n, m, t = map(int, input().split())
init_n = n
tmp = 0
for i in range(m):
    a, b = map(int, input().split())
    n -= math.floor((a-tmp)+0.5)
    if n <= 0:
        print("No")
        break
    n += math.floor((b-a)+0.5)
    if init_n < n:
        n = init_n
    tmp = b
else:
    if n-math.floor((t-tmp)+0.5) > 0:
        print("Yes")
    else:
        print("No")
