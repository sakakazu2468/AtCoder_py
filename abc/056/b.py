w, a, b = map(int, input().split())
ans = max(a, b)-w-min(a, b)
if ans > 0:
    print(ans)
else:
    print(0)
