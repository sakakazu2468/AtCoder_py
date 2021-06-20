h, w = map(int, input().split())
a = []
m = 10**10
for i in range(h):
    ipt = list(map(int, input().split()))
    m = min(min(ipt), m)
    a.append(ipt)

ans = 0
for i in range(h):
    for j in range(w):
        ans += a[i][j]-m
print(ans)


