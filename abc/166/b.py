n, k = map(int, input().split())
sunuke = [False for i in range(n)]
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in a:
        sunuke[j-1] = True
ans = 0
for i in sunuke:
    if i == False:
        ans += 1
print(ans)
