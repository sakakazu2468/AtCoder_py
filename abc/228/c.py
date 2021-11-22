n, k = map(int, input().split())
p = []
points = []
for i in range(n):
    s = sum(list(map(int, input().split())))
    points.append(s)
    p.append(s+300)

points.sort(reverse=True)
for i in range(n):
    if points[k-1] <= p[i]:
        print("Yes")
    else:
        print("No")

