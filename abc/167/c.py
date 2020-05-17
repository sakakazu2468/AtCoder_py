n, m, x = map(int, input().split())
prace = []
know = []
for i in range(n):
    acc = list(map(int, input().split()))
    prace.append(acc[0])
    know.append(acc[1:])

ans = 10**10
for i in range(2**n):
    und = [0 for i in range(m)]
    f = "{:b}".format(i)
    s = f.zfill(n)
    mm = 0
    for j in range(len(s)):
        if s[j] == '1':
            for k in range(m):
                und[k] += know[j][k]
            mm += prace[j]
    for j in range(m):
        if und[j] < x:
            break
    else:
        ans = min(ans, mm)
if ans == 10**10:
    print(-1)
else:
    print(ans)
