L, Q = map(int, input().split())

splt = [0, L]
for i in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        splt.append(x)
        splt.sort()
    else:
        if len(splt) == 2:
            print(L)
        else:
            l = 0
            r = len(splt)-1
            c = (l+r)//2
            while l+1 != r:
                if x < splt[c]:
                    r = c
                elif x > splt[c]:
                    l = c
                c = (l+r)//2
            print(splt[r]-splt[l])
