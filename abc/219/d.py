n = int(input())
x, y = map(int, input().split())
bento = []
for i in range(n):
    bento.append(list(map(int, input().split())))

dp = [[[1000 for i in range(y+10)] for j in range(x+10)] for k in range(n+10)]
dp[0][0][0] = 0

for i in range(n):
    for j in range(x+1):
        for k in range(y+1):
            if dp[i][j][k] != 1000:
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                dp[i+1][min(x, j+bento[i][0])][min(y, k+bento[i][1])] = min(dp[i+1][min(x, j+bento[i][0])][min(y, k+bento[i][1])], dp[i][j][k]+1)

ans = dp[n][x][y]
if ans == 1000:
    print(-1)
else:
    print(ans)
