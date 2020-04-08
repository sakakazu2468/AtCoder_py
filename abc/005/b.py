n = int(input())
ans = 1000
for i in range(n):
    ans = min(ans, int(input()))
print(ans)
