n = int(input())
a = list(map(int, input().split()))

mx = 0
for i in range(n):
    mn = a[i]
    for j in range(i, n):
        mn = min(a[j], mn)
        mx = max(mn*(j-i+1), mx)
print(mx)
