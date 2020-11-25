n = int(input())
h = list(map(int, input().split()))
INF = 10**10
dp = [INF for i in range(n)]
dp[0] = 0
for i in range(1, n):
    if i == 1:
        dp[i] = min(dp[i], dp[i-1]+abs(h[i]-h[i-1]))
    else:
        dp[i] = min(dp[i], dp[i-1]+abs(h[i]-h[i-1]))
        dp[i] = min(dp[i], dp[i-2]+abs(h[i]-h[i-2]))
print(dp[-1])