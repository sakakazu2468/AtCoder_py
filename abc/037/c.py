n, k = map(int, input().split())
a = list(map(int, input().split()))
s = [0]
for i in range(n):
    s.append(s[-1]+a[i])

ans = 0
for i in range(n-k+1):
    ans += s[i+k] - s[i]

print(ans)