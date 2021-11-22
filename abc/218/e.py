from collections import deque


n, m = map(int, input().split())
graph = [[] for i in range(n)]
ans = 0
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append([b, c, i])
    graph[b].append([a, c, i])
    ans += c

edge_use = [False for i in range(m)]
node_use = [False for i in range(n)]
node_num = [10**10 for i in range(n)]
q = deque()
q.append(0)
while len(q):
    pop = q.pop()
    edges = graph[pop]
    for edge in edges:
        if pop==edge[0] and edge[1]<0:
            ans -= edge[1]
        else:
            if edge_use[edge[2]] == False:
                node_num[edge[0]] = min(node_num[edge[0]], edge[1])
                edge_use[edge[2]] = True
            if node_use[edge[0]] == False:
                q.append(edge[0])
                node_use[edge[0]] = True

print(ans-sum(node_num[1:]))
