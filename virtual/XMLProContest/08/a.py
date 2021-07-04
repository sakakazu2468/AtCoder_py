n = int(input())
w = list(map(int, input().split()))
ans = 10**5
for i in range(1, n):
    sum1 = sum(w[:i])
    sum2 = sum(w[i:])
    ans = min(abs(sum1-sum2), ans)
print(ans)