n, s, t = map(int, input().split())
w = []
for i in range(n):
    if i == 0:
        w.append(int(input()))
    else:
        w.append(w[i-1]+int(input()))

ans = 0
for i in w:
    if s <= i <= t:
        ans += 1
print(ans)
