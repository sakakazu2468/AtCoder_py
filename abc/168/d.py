import queue


n, m = map(int, input().split())
to_room = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    to_room[a].append(b)
    to_room[b].append(a)
visited = [False for i in range(n+1)]
visited[0] = True
ans = [0 for i in range(n+1)]

q = queue.Queue()

def putting(t):
    global q
    for i in to_room[t]:
        if visited[i] == False:
            q.put((t, i))
            visited[i] = True

putting(1)
visited[1] == True
while not q.empty():
    prog = q.get()
    ans[prog[1]] = prog[0]
    putting(prog[1])


if all(visited):
    print("Yes")
    for i in range(n+1):
        if not (i == 0 or i == 1):
            print(ans[i])
else:
    print("No")
