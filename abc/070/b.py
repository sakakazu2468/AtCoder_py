a, b, c, d = map(int, input().split())
ans = 0
start = True
for i in range(101):
    if a <= i <= b and c <= i <= d:
        if start:
            start = False
            continue
        ans += 1
print(ans)
