q, h, s, d = map(int, input().split())
n = int(input())
if 4*q < s:
    if 4*q < 2*h:
        base = q
    else:
        base = h
else:
    if s < h*2:
        base = s
    else:
        base = h

if (q*8 > d) and (h*4 > d) and (s*2 > d):
    if n%2 == 0:
        print(d*n//2)
    else:
        if base == s:
            print(d*(n//2) + s)
        elif base == h:
            print(d*(n//2) + 2*h)
        elif base == q:
            print(d*(n//2) + 4*q)
else:
    if base == s:
        print(s*n)
    elif base == h:
        print(2*h*n)
    elif base == q:
        print(4*q*n)
