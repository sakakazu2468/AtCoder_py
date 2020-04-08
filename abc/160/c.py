k, n = map(int, input().split())
a = list(map(int, input().split()))
ans = []
for i in range(len(a)-1):
    ans.append(a[i+1]-a[i])
ans.append(k-a[-1]+a[0])
print(k-max(ans))

