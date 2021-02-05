from math import gcd

t = int(input())
for i in range(t):
    n, s, k = map(int, input().split())
    if s%gcd(n, k) == 0:
        count = 0
        pass
    else:
        print(-1)
