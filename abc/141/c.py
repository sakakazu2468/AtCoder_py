n, k ,q = map(int, input().split())
p = [k for i in range(n)]
for i in range(q):
    col = int(input())
    p[col-1] += 1
for i in range(n):
    if p[i] - q > 0:
        print("Yes")
    else:
        print("No")
