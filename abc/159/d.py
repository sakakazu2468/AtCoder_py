n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n+10)]
for i in range(n):
    dp[a[i]] += 1
ans = 0
for i in range(n+10):
    ans += dp[i]*(dp[i]-1)//2
for i in range(n):
    print(ans-(dp[a[i]]-1))
    
