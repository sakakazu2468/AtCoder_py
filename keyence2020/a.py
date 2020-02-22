h = int(input())
w = int(input())
n = int(input())

m = max(h, w)
if n%m == 0:
    print(n//m)
else:
    print(n//m+1)
