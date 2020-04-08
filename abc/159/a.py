n, m = map(int, input().split())
ans = 0
if n == 0 or n == 1:
    pass
else:
    ans += n*(n-1)//2
if m == 0 or m == 1:
    pass
else:
    ans += m*(m-1)//2
print(ans)
