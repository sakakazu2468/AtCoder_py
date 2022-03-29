from math import gcd


n = int(input())
a = list(map(int, input().split()))
ans = gcd(a[0], a[1])
for i in range(n-2):
    ans = gcd(ans, a[i+2])
print(ans)
