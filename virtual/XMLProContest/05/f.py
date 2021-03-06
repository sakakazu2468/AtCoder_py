from collections import deque

h, w = map(int, input().split())
a = []
for i in range(h):
    a.append(list(input()[:]))

step = [[True for _ in range(w)] for _ in range(h)]

q = deque()
for i in range(h):
    for j in range(w):
        if a[i][j] == "#":
            step[i][j] = False
            q.append((i, j, 0))

ans = -1
while True:
    get = q.popleft()
    ans = max(ans, get[2])
    if get[0] != 0:
        if step[get[0]-1][get[1]]:
            step[get[0]-1][get[1]] = False
            q.append((get[0]-1, get[1], get[2]+1))
    if get[1] != 0:
        if step[get[0]][get[1]-1]:
            step[get[0]][get[1]-1] = False
            q.append((get[0], get[1]-1, get[2]+1))
    if get[0] != h-1:
        if step[get[0]+1][get[1]]:
            step[get[0]+1][get[1]] = False
            q.append((get[0]+1, get[1], get[2]+1))
    if get[1] != w-1:
        if step[get[0]][get[1]+1]:
            step[get[0]][get[1]+1] = False
            q.append((get[0], get[1]+1, get[2]+1))

    if not len(q):
        break

print(ans)
