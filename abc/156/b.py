n, k = map(int, input().split())

for i in range(32):
    if n // (k**(31-i)) > 0:
        print(31-i+1)
        break
