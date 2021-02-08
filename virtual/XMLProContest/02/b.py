n, m = map(int, input().split())
probrem = [[0, 0] for i in range(n)]
AC = 0
WA = 0
for i in range(m):
    p, s = input().split()
    p = int(p)
    if probrem[p-1][1] == 0:
        if s == "AC":
            probrem[p-1][1] = 1
            AC += 1
            WA += probrem[p-1][0]
        else:
            probrem[p-1][0] += 1
print(AC, WA)

