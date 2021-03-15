from collections import deque


r, c = map(int, input().split())
start = list(map(lambda x:int(x)-1, input().split()))
start.append(0)
goal = list(map(lambda x:int(x)-1, input().split()))
maze = []
for i in range(r):
    maze.append(list(input())[:])

visited = [[True for _ in range(c)] for _ in range(r)]
d = deque()
d.append(start)
visited[start[0]][start[1]] = False
xdif = [1, -1, 0, 0]
ydif = [0, 0, 1, -1]
while len(d) != 0:
    pop = d.popleft()
    if pop[0] == goal[0] and pop[1] == goal[1]:
        print(pop[2])
        break
    for i in range(4):
        next_x = pop[0] + xdif[i]
        next_y = pop[1] + ydif[i]
        if maze[next_x][next_y] == "." and visited[next_x][next_y]:
            d.append([next_x, next_y, pop[2]+1])
            visited[next_x][next_y] = False

