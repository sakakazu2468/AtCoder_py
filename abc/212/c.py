n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ai = 0
bi = 0
an = a[ai]
bn = b[bi]
mindis = 10**10
while True:
    if an==bn:
        mindis = 0
        break
    mindis = min(mindis, abs(an-bn))
    if an > bn:
        if bi+1==m:
            break
        bi += 1
        bn = b[bi]
    else:
        if ai+1==n:
            break
        ai += 1
        an = a[ai]
print(mindis)
