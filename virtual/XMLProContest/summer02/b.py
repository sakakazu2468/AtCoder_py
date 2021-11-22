n = int(input())
a = list(map(int, input().split()))
s = a[-1]
ans = 0
for i in range(n-1):
    ans += s*a[-1*(i+2)]
    ans %= 10**9+7
    s = (s+a[-1*(i+2)])%(10**9+7)
print(ans)
