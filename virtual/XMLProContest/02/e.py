n, m = map(int, input().split())
balls = [[1, 0] for i in range(n)]
balls[0][1] = 1

for i in range(m):
    x, y = map(int, input().split())
    balls[x-1][0] -= 1
    balls[y-1][0] += 1
    if balls[x-1][1] == 1:
        balls[y-1][1] = 1
    if balls[x-1][0] == 0:
        balls[x-1][1] = 0

ans = 0
for i in balls:
    ans += i[1]

print(ans)
