n = int(input())
if n % 2 == 0:
    print(int(n/2)*(n-1))
else:
    print(n*int((n-1)/2))