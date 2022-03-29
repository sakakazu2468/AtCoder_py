n, w = map(int, input().split())
cheese = []
for i in range(n):
    a, b = map(int, input().split())
    cheese.append((a, b))

cheese.sort(reverse=True)

ans = 0
for i in range(len(cheese)):
    ans += cheese[i][0] * min(cheese[i][1], w)
    w -= min(cheese[i][1], w)
print(ans)
