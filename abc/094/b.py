n, m, x = map(int, input().split())
a = list(map(int, input().split()))
l, h = 0, 0
for i in a:
    if i < x:
        l += 1
    else:
        h += 1
print(min(l, h))

