n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
c = 0
for i in range(n):
    if c >= 500:
        break
    for j in range(n):
        print(i, j, 'L')
        if c >= 500:
            break
        c += 1
