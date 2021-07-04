h, w = map(int, input().split())
board = []
ans = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    board.append(input())

for i in range(h):
    for j in range(w):
        if board[i][j] == "#":
            if i!=0:
                ans[i-1][j] += 1
            if j!=0:
                ans[i][j-1] += 1
            if i!=h-1:
                ans[i+1][j] += 1
            if j!=w-1:
                ans[i][j+1] += 1
            if i!=0 and j!=0:
                ans[i-1][j-1] += 1
            if i!=h-1 and j!=0:
                ans[i+1][j-1] += 1
            if i!=0 and j!=w-1:
                ans[i-1][j+1] += 1
            if i!=h-1 and j!=w-1:
                ans[i+1][j+1] += 1



for i in range(h):
    for j in range(w):
        if board[i][j]=="#":
            ans[i][j] = "#"

for i in range(h):
    print("".join(list(map(lambda x: str(x), ans[i]))))
