n, k = map(int, input().split())
c = list(map(int, input().split()))
pool = dict()
count = 0
for i in range(k):
    if pool.get(c[i], 0) == 0:
        pool[c[i]] = 1
        count += 1
    else:
        pool[c[i]] += 1

ans = -1
ans = max(ans, count)
for i in range(n-k):
    if pool.get(c[i+k], 0) == 0:
        pool[c[i+k]] = 1
        count += 1
    else:
        pool[c[i+k]] += 1
    if pool.get(c[i], 0) == 1:
        pool[c[i]] = 0
        count -= 1
    else:
        pool[c[i]] -= 1
    ans = max(count, ans) 
print(ans)   