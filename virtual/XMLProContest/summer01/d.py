n = int(input())
a = list(map(int, input().split()))
a.sort()
if n<=3:
    ans = 10**10
    for i in range(n):
        calc = 0
        for j in range(n):
            calc += a[i]/2+a[j]-min(a[i],a[j])
        ans = min(calc/n, ans)
    print(ans)
else:
    l = 0
    r = n-1
    c1 = (l*2+r)//3
    c2 = (l+r*2)//3
    for k in range(100):
        lm = 0
        for i in range(n):
            lm += a[l]/2+a[i]-min(a[i],a[l])
        rm = 0
        for i in range(n):
            rm += a[r]/2+a[i]-min(a[i],a[r])
        c1m = 0
        for i in range(n):
            c1m += a[c1]/2+a[i]-min(a[i],a[c1])
        c2m = 0
        for i in range(n):
            c2m += a[c2]/2+a[i]-min(a[i],a[c2])
        if c1m > c2m:
            l = c1
            c = c2
            cm = c2m
        else:
            r = c2
            c = c1
            cm = c1m
        c1 = (l*2+r)//3
        c2 = (l+r*2)//3

    print(cm/n)


