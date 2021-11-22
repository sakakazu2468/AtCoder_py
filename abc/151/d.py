from collections import deque

h, w = map(int, input().split())
maze = []
for i in range(h):
    s = list(input())[:]
    maze.append(s)

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
ans = -1
for i in range(h):
    for j in range(w):
        visited = [[False for _ in range(w)] for _ in range(h)]
        q = deque()
        if maze[i][j] == '.':
            q.append([i, j, 0])
            visited[i][j] = True
        while len(q):
            p = q.popleft()
            ans = max(p[2], ans)
            for k in range(4):
                x = p[1] + dx[k]
                y = p[0] + dy[k]
                if x >= w or x < 0 or y >= h or y < 0:
                    continue
                if visited[y][x] == True or maze[y][x] == '#':
                    continue
                q.append([y, x, p[2]+1])
                visited[y][x] = True
print(ans)