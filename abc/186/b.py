h, w = map(int, input().split())
a = []
mini = 1000
for i in range(h):
    a_input = list(map(int, input().split()))
    mini = min(min(a_input), mini)
    a.append(a_input)

ans = 0
for i in range(h):
    for j in range(w):
        ans += a[i][j]-mini

print(ans)
