n, a, x, y = map(int, input().split())
ans = 0
for i in range(n):
    if i+1 <= a:
        ans += x
    else:
        ans += y
print(ans)