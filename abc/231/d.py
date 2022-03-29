from collections import deque


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x:int(x)-1, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n)]
q = deque()
for i in range(n):
    if visited[i] == False:
        if len(graph[i]) > 2:
            print("No")
            break
        visited[i] = True
        q.append([i, -1])
        while len(q):
            pl = q.popleft()
            pop = pl[0]
            prv = pl[1]
            nxts = graph[pop]
            if len(nxts) > 2:
                print("No")
                break
            for nxt in nxts:
                if nxt == prv:
                    continue
                elif visited[nxt] == True:
                    print("No")
                    break
                else:
                    visited[nxt] = True
                    q.append([nxt, pop])
            else:
                continue
            break
        else:
            continue
        break
else:
    print("Yes")
