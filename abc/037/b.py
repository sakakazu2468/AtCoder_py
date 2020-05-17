n, q = map(int, input().split())
seq = [0 for i in range(n)]
for i in range(q):
    l, r, t = map(int, input().split())
    for i in range(r-l+1):
        seq[l+i-1] = t

for i in seq:
    print(i)
