n, a, b = map(int, input().split())
a -= 1
b -= 1
p, q, r, s = map(int, input().split())
canbas = [["." for _ in range(s-r+1)] for _ in range(q-p+1)]
cannum = [[(j+p-1, i+r-1) for i in range(s-r+1)] for j in range(q-p+1)]
for i in range(q-p+1):
    for j in range(s-r+1):
        if abs(a-cannum[i][j][0]) == abs(b-cannum[i][j][1]):
            canbas[i][j] = "#"

for can in canbas:
    for c in can:
        print(c, end="")
    print()
