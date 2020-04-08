n, m = map(int, input().split())
table = [[0, "None"] for i in range(n+10)]
for i in range(m):
    p, s = input().split()
    p = int(p)
    if table[p][1] == "None" or table[p][1] == "WA":
        if s == "WA":
            table[p][0] += 1
        table[p][1] = s
AC = 0
PEN = 0
for i in table:
    if i[1] == "AC":
        AC += 1
        PEN += i[0]
print(AC, PEN)
