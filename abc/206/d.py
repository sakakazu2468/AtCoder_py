from collections import deque


n = int(input())
a = list(map(lambda x: int(x)-1, input().split()))
MAX = 2*10**5

visited = [False for i in range(MAX)]
graph = [[] for i in range(MAX)]
for i in range(n//2):
    if a[i] != a[n-1-i]:
        graph[a[i]].append(a[n-1-i])
        graph[a[n-1-i]].append(a[i])

q = deque()
ans = 0
for i in range(MAX):
    count = 0
    for j in range(len(graph[i])):
        if visited[graph[i][j]] == False:
            q.append(graph[i][j])
            visited[graph[i][j]] = True
            count += 1

    while len(q) != 0:
        pop = q.popleft()
        for j in range(len(graph[pop])):
            if visited[graph[pop][j]] == False:
                q.append(graph[pop][j])
                visited[graph[pop][j]] = True
                count += 1
        if len(q) == 0:
            ans += count - 1
            break
print(ans)
