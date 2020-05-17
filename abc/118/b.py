n, m = map(int, input().split())
kind = [0 for i in range(m)]
for i in range(n):
    a = list(map(int, input().split()))
    k, a = a[0], a[1:]
    for j in range(k):
        kind[a[j]-1] += 1
count = 0
for i in kind:
    if i == n:
        count += 1
print(count)
