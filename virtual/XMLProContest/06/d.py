n = int(input())
a = list(map(int, input().split()))
gcd = a[0]
for i in range(1, n):
    new = a[i]
    while True:
        if new%gcd == 0:
            break
        else:
            tmp = gcd
            gcd = new%gcd
            new = tmp
print(gcd)

        
