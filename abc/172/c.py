n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
max_ans = 0
time = 0
ac = 0
bc = 0
for i in range(n):
    if time + a[i] <= k:
        ans += 1
        time += a[i]
        ac += 1
    else:
        break
for i in range(m):
    if time + b[i] <= k:
        ans += 1
        time += b[i]
        bc += 1
    else:
        break
max_ans = ans
while (bc!=m) and (ac!=0):
    time -= a[ac-1]
    ac -= 1
    ans -= 1
    while time + b[bc] <= k:
        ans += 1
        time += b[bc]
        bc += 1
        max_ans = max(ans, max_ans)
        if bc == m:
            break
print(max_ans)
