

x, k, d = map(int, input().split())
mnum = x//d
if k > abs(mnum):
    x %= d
    k -= abs(mnum)
    if k%2 == 0:
        print(abs(x))
    else:
        print(abs(x-d))
else:
    if x < 0:
        x = x+k*d
    else:
        x = x-k*d
    print(abs(x))
