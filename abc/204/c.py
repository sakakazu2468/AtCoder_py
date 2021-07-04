from collections import deque

n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    graph[a].append(b)

ans = 0
for i in range(n):
    q = deque()
    visited = [False for i in range(n)]
    q.append(graph[i])
    visited[i] = True
    ans += 1
    while len(q):
        pop = q.popleft()
        for j in range(len(pop)):
            if visited[pop[j]] == False:
                q.append(graph[pop[j]])
                visited[pop[j]] = True
                ans += 1
print(ans)
