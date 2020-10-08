a, b = map(int, input().split())
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)
n = gcd(a, b)
ndiv = n
if n == 1:
    print(1)
else:
    i = 1
    primecount = 0
    divisor = False
    while True:
        i += 1
        while ndiv%i == 0:
            ndiv = ndiv//i
            divisor = True
        if divisor:
            primecount += 1
            divisor = False
            if ndiv == 1:
                break
        if ndiv != 1 and i*i > n:
            primecount += 1
            break
    print(primecount+1)
