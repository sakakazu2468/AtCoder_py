n, m = map(int, input().split())
h = list(map(int, input().split()))
w = list(map(int, input().split()))
h.sort()
dis1 = []
dis2 = []
for i in range(n//2):
    dis1.append(abs(h[i*2]-h[i*2+1]))
    dis2.append(abs(h[i*2+1]-h[i*2+2]))

anss = []
for i in range(m):
    l = 0
    r = len(h)
    while True:
        c = (l+r)//2
        if w[i] < h[c]:
            r = c
        elif h[c] <= w[i]:
            l = c
        if l+1 == r:
            break
    sumdis1 = sum(dis1[:l//2])
    center = abs(h[l]-w[i])
    sumdis2 = sum(dis2[l//2:])
    ans = sumdis1 + sumdis2 + center
    anss.append(ans)
print(min(anss))
