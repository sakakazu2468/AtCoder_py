n = int(input())
c = sorted(list(map(int ,input().split())))
a, b = 0, 0
for i in range(n):
    if i%2 == 0:
        a += c.pop()
    else:
        b += c.pop()
print(a-b)

