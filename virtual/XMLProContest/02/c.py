n, m = map(int, input().split())
Scc = 0
if 2*n > m:
    Scc += m//2
else:
    Scc += n
    rem = m-2*n
    Scc += rem//4
print(Scc)
