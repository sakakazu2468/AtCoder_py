n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ae = [-1]
ae += a
ae.append(10**10)
for i in range(q):
    x = int(input())
    l = 0
    r = len(ae)-1
    while True:
        c = (l+r)//2
        if ae[c] < x:
            l = c
        else:
            r = c
        if l+1 == r:
            break
    print(len(ae)-1-r)



