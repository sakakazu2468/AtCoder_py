n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()
a.append(10**10)
c.append(10**10)
a = [-1] + a
c = [-1] + c
ans = 0
for i in range(len(b)):
    al = 0
    ar = n+1
    while True:
        am = (al+ar)//2
        if a[am] < b[i]:
            al = am
        else:
            ar = am
        an = al
        if al+1 == ar:
            break
    cl = 0
    cr = n+1
    while True:
        cm = (cl+cr)//2
        if c[cm] <= b[i]:
            cl = cm
        else:
            cr = cm
        cn = n - (cr-1)
        if cl+1 == cr:
            break
    ans += an*cn
print(ans)
