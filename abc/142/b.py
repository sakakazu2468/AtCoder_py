n, k = map(int, input().split())
h = list(map(int, input().split()))
ok = 0
for i in range(n):
    if h[i] >= k:
        ok += 1
print(ok)