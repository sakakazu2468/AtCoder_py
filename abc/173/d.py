n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
ans = a[0]
a_other = a[1:]
for i in range(n-2):
    idx = i//2
    ans += a_other[idx]
print(ans)
