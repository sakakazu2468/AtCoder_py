n, m = map(int, input().split())

tree = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(n+1):
    tree[i] = list(set(tree[i]))

visited = [False for i in range(n+1)]


def add(x, count):
    for i in range(len(tree[x])):
        if visited[tree[x][i]] == False:
            count += 1
            visited[tree[x][i]] = True
            count = add(tree[x][i], count)
    return count

max_count = -1
for i in range(1, n+1):
    if visited[i] == False:
        visited[i] = True
        count = 1
        count = add(i, count)
        max_count = max(count, max_count)
print(max_count)
