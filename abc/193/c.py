n = int(input())
expressed = set()
for a in range(2, 10**5+1):
    b = 2
    while True:
        if a**b > n:
            break
        expressed.add(a**b)
        b += 1
print(n-len(expressed))




