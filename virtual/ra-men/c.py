n, m = map(int, input().split())
l = 0
r = 1000000
for i in range(m):
    li, ri = map(int, input().split())
    if li > l:
        l = li
    if ri < r:
        r = ri
    if l > r:
        print(0)
        break
else:
    if r >= n:
        print(n-l+1)
    else:
        print(r-l+1)
        
