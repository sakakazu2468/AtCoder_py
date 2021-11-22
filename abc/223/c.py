n = int(input())
alis = []
blis = []
totaltime = 0
for i in range(n):
    a, b = map(int, input().split())
    alis.append(a)
    blis.append(b)
    totaltime += a/b

halftime = totaltime/2

sumtime = 0
idx = 0
while True:
    if sumtime + alis[idx]/blis[idx] > halftime:
        break
    else:
        sumtime += alis[idx]/blis[idx]
        idx += 1

ans = 0
for i in range(idx):
    ans += alis[i]

dis = abs(sumtime-halftime)
ans += blis[idx]*dis
print(ans)




