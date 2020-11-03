import queue

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = [[0 for i in range(c+1)]]
maze_check = [[False for i in range(c+1)] for j in range(r+1)]
q = queue.Queue()
for i in range(r):
    maze.append([0] + list(input())[:])

q.put((sy, sx, 0))
maze_check[sy][sx] = True

while not q.empty():
    taken = q.get()
    if taken[0] == gy and taken[1] == gx:
        print(taken[2])
        break
    if maze[taken[0]][taken[1]-1] == '.' and maze_check[taken[0]][taken[1]-1] == False:
        q.put((taken[0], taken[1]-1, taken[2]+1))
        maze_check[taken[0]][taken[1]-1] = True
    if maze[taken[0]][taken[1]+1] == '.' and maze_check[taken[0]][taken[1]+1] == False:
        q.put((taken[0], taken[1]+1, taken[2]+1))
        maze_check[taken[0]][taken[1]+1] = True
    if maze[taken[0]-1][taken[1]] == '.' and maze_check[taken[0]-1][taken[1]] == False:
        q.put((taken[0]-1, taken[1], taken[2]+1))
        maze_check[taken[0]-1][taken[1]] = True
    if maze[taken[0]+1][taken[1]] == '.' and maze_check[taken[0]+1][taken[1]] == False:
        q.put((taken[0]+1, taken[1], taken[2]+1))
        maze_check[taken[0]+1][taken[1]] = True