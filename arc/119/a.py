n = int(input())
sums = []
for i in range(60):
    a = n // 2**i
    c = n - (a*2**i)
    sums.append(a+i+c)
print(min(sums))
