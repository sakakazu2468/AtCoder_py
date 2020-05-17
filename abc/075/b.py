mine = []
h, w = map(int, input().split())
for i in range(h):
    mine.append(list(input()[:]))
ans = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    for j in range(w):
        if mine[i][j] == '#':
            if i != 0:
                ans[i-1][j] += 1
            if j != 0:
                ans[i][j-1] += 1
            if i != h-1:
                ans[i+1][j] += 1
            if j != w-1:
                ans[i][j+1] += 1
            if i != 0 and j != 0:
                ans[i-1][j-1] += 1
            if i != 0 and j != w-1:
                ans[i-1][j+1] += 1
            if i != h-1 and j != 0:
                ans[i+1][j-1] += 1
            if i != h-1 and j != w-1:
                ans[i+1][j+1] += 1

for i in range(h):
    for j in range(w):
        if mine[i][j] == "#":
            print("#", end="")
        else:
            print(ans[i][j], end="")
    print()
