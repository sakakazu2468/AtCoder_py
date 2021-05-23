n = int(input())
a = list(map(int, input().split()))
ans = 1
hight = 0
a.sort()
for i in range(n):
    ans *= a[i] - hight + 1
    hight = a[i]
    ans %= 10**9+7
print(ans)
