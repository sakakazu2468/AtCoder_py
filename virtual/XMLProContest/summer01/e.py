a = int(input())
n = 1500
dp = [[0 for i in range(j+1)] for j in range(n)]
for i in range(n):
    dp[i][0] = 1
    dp[i][-1] = 1
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
        if dp[i][j] == a:
            print(i+1, j+1)
            break
    else:
        continue
    break
else:
    print(-1, -1)
