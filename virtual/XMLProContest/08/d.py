n, k, s = map(int, input().split())
ans = [0 for i in range(n)]
if s==10**9:
    for i in range(n):
        if i <= k-1:
            ans[i] = 10**9
        else:
            ans[i] = 1
else:
    for i in range(n):
        if i <= k-1:
            ans[i] = s
        else:
            ans[i] = 10**9
for i in ans:
    print(i, end=" ")
print()
