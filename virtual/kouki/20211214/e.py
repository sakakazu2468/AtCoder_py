n, k, s = map(int, input().split())
if s == 10**9:
    ans = [10**9 if (i+1) <= k else 1 for i in range(n)]
else:
    ans = [s if (i+1) <= k else 10**9 for i in range(n)]
print(" ".join(map(str, ans))+"\n")
