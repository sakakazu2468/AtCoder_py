n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    a[i] = a[i]//2


def lcmroop(n1, n2):
    a1 = n1
    a2 = n2
    while n1 % n2 != 0:
        n1, n2 = n2, n1 % n2
    gcd = n2
    lcm = a1 * a2 // gcd
    print(a1, a2, gcd)
    return lcm

lcm = a[i]
for i in range(n-1):
    lcm = lcmroop(lcm, a[i+1])

if lcm >= m:
    print(0)
else:
    num = m // lcm
    if num % 2 == 0:
        print(num//2)
    else:
        print(num//2+1)
