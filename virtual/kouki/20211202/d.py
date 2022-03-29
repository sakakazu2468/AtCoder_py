h, w = map(int, input().split())
canbas = []
for i in range(h):
    canbas.append(input())

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
for i in range(h):
    for j in range(w):
        if canbas[i][j] == "#":
            poss = False
            for k in range(4):
                x = j
                y = i
                x += dx[k]
                y += dy[k]
                if not (0 <= x < w and 0 <= y < h):
                    continue
                if canbas[y][x] == "#":
                    poss = True
            if not poss:
                print("No")
                break
    else:
        continue
    break
else:
    print("Yes")
