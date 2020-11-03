



n, k = map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
pt = [False for i in range(n)]
pl = [[]]
plnum = 0
for i in range(n):
    if pt[i] == True:
        continue
    else:
        pl[plnum].append(i)
        pt[i] = True
        num = i
        while True:
            if p[num]-1 in pl[plnum]:
                break
            pl[plnum].append(p[num]-1)
            pt[p[num]-1] = True
            num = p[num]-1
        plnum += 1
        pl.append([])
print(pl)
ppm = [0 for i in range(len(pl)-1)]
for i in range(len(pl)-1):
    pm = 0
    for j in range(len(pl[i])):
        pm += p[pl[i][j]]
    if pm <= 0:
        ppm[i] = False
    else:
        ppm[i] = True
ans = -1
for i in range(len(pl)-1):
    m = 0
    for j in range(len(pl[i])):
        m += p[pl[i][j]]
        ans = max(m, ans)
    
