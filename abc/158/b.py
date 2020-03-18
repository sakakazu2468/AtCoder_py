n, a, b = map(int, input().split())
if a==0 and b==0:
    print(0)
else:
    blue = n//(a+b)
    rm = n%(a+b)
    ans = blue*a
    if rm>a:
        ans += a
    else:
        ans += rm
print(ans)
