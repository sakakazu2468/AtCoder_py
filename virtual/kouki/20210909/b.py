from math import gcd

n, k = map(int, input().split())
a = list(map(int, input().split()))
flag = True
odd = False
if n == 1:
    if a[0] == k:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
else:
    g = gcd(a[0], a[1])
    for i in range(n):
        g = gcd(a[i], g)

    for i in range(n):
        if a[i]%g != 0:
            flag = False
        if a[i]%2 == 1:
            odd = True

    if max(a) < k:
        print("IMPOSSIBLE")
    elif flag:
        if k%g != 0:
            print("IMPOSSIBLE")
        else:
            print("POSSIBLE")
    else:
        if (odd == False) and (k%2 != 0):
            print("IMPOSSIBLE")
        else:
            print("POSSIBLE")
