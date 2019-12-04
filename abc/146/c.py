a, b, x = map(int, input().split())
n = 1
if x >= (a*n) + (b*len(str(n))):
    while x >= (a*n) + (b*len(str(n))):
        n *= 10
    n = n//10
    if n >= 10**9:
        print(10**9)
    else:
        for i in range(len(str(n)), -1, -1):
            while x >= (a*n) + (b*len(str(n))):
                n += 10**i
            n -= 10**i
        print(n)
else:
    print(0)
