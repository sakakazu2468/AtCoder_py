from collections import deque


n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    u, v = map(lambda x: int(x)-1, input().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 1
visited = [False for _ in range(n)]
vis_edge = set()
flag = False
for i in range(n):
    q = deque()
    if visited[i] == True:
        continue
    q.append(i)
    visited[i] = True
    edge = 0
    node = 1
    while len(q):
        pop = q.pop()
        l = len(graph[pop])
        for j in range(l):
            nxt = graph[pop][j]
            if visited[nxt] == False:
                q.append(nxt)
                visited[nxt] = True
                node += 1
            before = len(vis_edge)
            vis_edge.add((pop, nxt))
            vis_edge.add((nxt, pop))
            if before != len(vis_edge):
                edge += 1
    if node == edge:
        ans *= 2
        ans %= 998244353
    else:
        flag = True
    
    
if flag:
    print(0)
else:
    print(ans)

