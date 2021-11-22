from collections import deque


n, m = map(int, input().split())
tree = [[] for i in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False for i in range(n)]
q = deque()
ans = 0
for i in range(n):
    if visited[i] == False:
        q.append(i)
        visited[i] = True
        while len(q) != 0:
            pop = q.pop()
            for j in tree[pop]:
                if visited[j] == False:
                    q.append(j)
                    visited[j] = True
        ans += 1
print(ans-1)
