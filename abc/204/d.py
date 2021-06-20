n = int(input())
t = list(map(int, input().split()))
s = sum(t)
dp = [[False for i in range(10**5+10)] for j in range(100+10)]
dp[0][0] = True
ans_list = []
for i in range(n):
    for j in range(10**5+10):
        if t[i] > j:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = dp[i][j-t[i]] or dp[i][j]
        if j >= s//2+s%2:
            if dp[i+1][j] == True:
                ans_list.append(j)
                break
print(min(ans_list))
