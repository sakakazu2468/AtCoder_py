n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
gans = x//a[0] + 1
gnum = gans * a[0]
gdiff = gnum-x
for i in range(n):
    div = gdiff//a[i]
    gans += div
    gdiff -= div * a[i]

lans = x//a[0]
lnum = lans * a[0]
ldiff = x-lnum
incdiff = ldiff
for i in range(n):
    div = ldiff//a[i]
    lans += div
    ldiff -= div * a[i]

print(min(gans, lans))

for i in range(n):
    if i==0:
        continue
    inc


