n = int(input())
a = list(map(int, input().split()))

table = [0 for i in range(10**6+1)]
ans = 0
a.sort()
a.append(10**7)
for i in range(n):
    el = a[i]
    if table[el] != 0:
        continue
    else:
        if el != a[i+1]:
            ans += 1
    idx = el
    while idx <= 10**6:
        table[idx] += 1
        idx += el

print(ans)
