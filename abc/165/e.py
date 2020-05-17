n, m = map(int, input().split())
if n%2:
    n -= 1
for i in range(m):
    print(n//2-i, n//2+(i+1))
