n = int(input())
w = list(map(int, input().split()))
ans = 100000
for i in range(n-1):
    ans = min(abs(sum(w[:i+1])-sum(w[i+1:])), ans)
print(ans)
