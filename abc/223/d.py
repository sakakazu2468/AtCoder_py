from collections import deque


n, m = map(int, input().split())
tree = [[] for i in range(n)]
tier = [0 for i in range(n)]
for i in range(m):
    a, b = map(lambda x:int(x)-1, input().split())
    tree[a].append(b)

q = deque()
miss = False
for i in range(n):
    q.append([i, 1])
    tier[i] = 1
    visited = [0 for i in range(n)]
    visited[i] = 1
    while len(q):
        pop = q.pop()
        for nxt in tree[pop[0]]:
            if visited[nxt] != 0:
                miss = True
                break
            else:
                if tier[nxt] < pop[1]+1:
                    q.append([nxt, pop[1]+1])
                    tier[nxt] = pop[1]+1
                    visited[nxt] = 1
    if miss:
        break

if miss:
    print(-1)
else:
    anstier = [[tier[i], i] for i in range(n)]
    anstier.sort()
    for ans in anstier:
        print(ans[1]+1, end=" ")
    print()


