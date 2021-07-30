import copy


n, q = map(int, input().split())
tree = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False for i in range(n)]
edge_list = [0 for i in range(n)]

def dfs(name, d, edge):
    edge_list[name] = copy.deepcopy(edge)
    for i in range(len(tree[name])):
        nxt = tree[name][i]
        if visited[nxt] == False:
            edge.add(tuple(sorted((nxt, name))))
            visited[nxt] = True
            dfs(nxt, d+1, copy.deepcopy(edge))
            edge.remove(tuple(sorted((nxt, name))))

visited[0] = True
dfs(0, 0, set())
for i in range(q):
    c, d = map(lambda x:int(x)-1, input().split())
    uni = edge_list[c] & edge_list[d]
    distance = len(edge_list[c])+len(edge_list[d])-2*len(uni)
    if distance%2 == 0:
        print("Town")
    else:
        print("Road")
    
