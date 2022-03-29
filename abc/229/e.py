from collections import deque


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
dirgraph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    dirgraph[a].append(b)
    graph[a].append(b)
    graph[b].append(a)

parents = [0 for _ in range(n)]
ans = 1
anslist = [ans]
for i in range(len(dirgraph)):
    for j in range(len(dirgraph[i])):
    
    anslist.append(ans)

for i in range(len(anslist)):
    print(anslist[-1*(i+1)])
# gnum = 0
# visited = [False for _ in range(n)]
# q = deque()
# for i in range(n):
#     if visited[i] == False:
#         q.append(i)
#         visited[i] = True
#         gnum += 1
#         while len(q):
#             pop = q.pop()
#             nxt = graph[pop]
#             for j in range(len(nxt)):
#                 if visited[nxt[j]] == False:
#                     q.append(nxt[j])
#                     visited[nxt[j]] = True
# 
# for i in range(len(dirgraph)):
#     one = 0
#     for j in dirgraph[i]:
#         if len(dirgraph[j])
