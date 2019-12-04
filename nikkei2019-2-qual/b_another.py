n = int(input())
d = list(map(int, input().split()))
lis = [0 for i in range(10**5+100)]
ans = 1
mx = -1
for i in d:
    lis[i] += 1
    if i > mx:
        mx = i
if lis[0] != 1 or d[0] != 0:
    print(0)
else:
    for i in range(1, mx+1):
        ans *= lis[i-1]**lis[i]
    print(ans%998244353)
