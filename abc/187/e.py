n = int(input())
tree = [[] for i in range(n+1)]
edge = [[0, 0]]
edge_num = [0 for i in range(n+1)]
root_edge_distance = [0 for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    edge.append([a, b])
    tree[a].append(b)
    tree[b].append(a)

visited = [False for i in range(n+1)]
distance = 1
q = []
for i in tree[1]:
    if visited[i] == False:
        q.append((1, i, distance))
visited[1] = True
while q:
    get = q.pop()
    root_edge_distance[get[1]] = get[2]
    visited[get[1]] = True
    for i in tree[get[1]]:
        if visited[i] == False:
            q.append((get[1], i, get[2]+1))

query = int(input())
for i in range(query):
    t, e, x = map(int, input().split())
    left = root_edge_distance[edge[e][0]]
    right = root_edge_distance[edge[e][1]]
    rootside = min(left, right)
    if t == 1:
        if rootside == left:
            edge_num[1] += x
            edge_num[edge[e][1]] -= x
        else:
            edge_num[edge[e][0]] += x
    if t == 2:
        if rootside == right:
            edge_num[1] += x
            edge_num[edge[e][0]] -= x
        else:
            edge_num[edge[e][1]] += x

visited = [False for i in range(n+1)]
for i in tree[1]:
    if visited[i] == False:
        q.append((1, i))
visited[1] = True
while q:
    get = q.pop()
    edge_num[get[1]] += edge_num[get[0]] 
    visited[get[1]] = True
    for i in tree[get[1]]:
        if visited[i] == False:
            q.append((get[1], i))

for i in range(1, n+1):
    print(edge_num[i])
