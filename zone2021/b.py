n, ud, uh = map(int, input().split())
max_tan = 0
md = 0
mh = 0
for i in range(n):
    d, h = map(int, input().split())
    tri_d = ud - d
    tri_h = uh - h
    if max_tan <= tri_d/tri_h:
        max_tan = tri_d/tri_h
        md = tri_d
        mh = tri_h

ans = uh-(mh*ud/md)
if ans > 0:
    print(ans)
else:
    print(0)
    


