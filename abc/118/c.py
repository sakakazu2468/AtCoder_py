from math import gcd
n = int(input())
a = list(map(int, input().split()))
# print(gcd(*a))
ans = a[0]
for i in range(n-1):
    ans = gcd(ans, a[i+1])
print(ans)
