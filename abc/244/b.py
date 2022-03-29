n = int(input())
t = input()
pos = [0, 0]
d = [[1, 0], [0, -1], [-1, 0], [0, 1]]
dn = 0
for i in range(n):
    if t[i] == "S":
        pos[0] += d[dn][0]
        pos[1] += d[dn][1]
    else:
        dn += 1
        dn %= 4
print(pos[0], pos[1])
