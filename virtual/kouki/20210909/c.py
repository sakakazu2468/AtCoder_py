from collections import deque

n = int(input())
mat = [[10**16 for j in range(n)] for i in range(n)]
so = [[] for i in range(n)]
for i in range(n):
    mat[i][i] = 0
for i in range(n-1):
    a, b, c = map(int, input().split())
    mat[a-1][b-1] = c
    mat[b-1][a-1] = c
    so[a-1].append(b-1)
    so[b-1].append(a-1)

Q, k = map(int, input().split())

visited = [False for i in range(n)]
q = deque()
q.append([k-1, 0])
visited[0] = True
while len(q):
    pop = q.pop()
    nxt = so[pop[0]]
    for i in range(len(nxt)):
        if visited[nxt[i]] == False:

            mat[0][nxt[i]] = mat[pop[0]][nxt[i]] + pop[1] 

            visited[nxt[i]] = True
            q.append([nxt[i], mat[pop[0]][nxt[i]]])
for i in range(Q):
    x, y = map(int, input().split())
    print(mat[k-1][x-1] + mat[k-1][y-1])

