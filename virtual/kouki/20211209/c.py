n = int(input())
x = list(map(int, input().split()))
ans = 10**9
for i in range(1, 101):
    ans = min(sum(map(lambda y: (y-i)**2, x)), ans)
print(ans)


