from collections import deque


n = int(input())
graph = [[] for _ in range(n)]
val = [0 for i in range(n)]
train = []
for i in range(n):
    ipt = list(map(int, input().split()))
    t = ipt[0]
    k = ipt[1]
    a = ipt[2:]
    val[i] = t
    for j in range(k):
        graph[i].append(a[j]-1)

q = deque() 
visited = [False for _ in range(n)]
ans = val[-1]
for i in range(len(graph[-1])):
    q.append(graph[-1][i])
    visited[graph[-1][i]] = True
    ans += val[graph[-1][i]]

while len(q):
    pop = q.popleft()
    for i in range(len(graph[pop])):
        nxt = graph[pop][i]
        if visited[nxt] == False:
            q.append(nxt)
            visited[nxt] = True
            ans += val[nxt]

print(ans)


