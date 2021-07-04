from collections import deque
n = int(input())
a = list(map(int, input().split()))
ans = []
q = deque()
q.append((a[0], 0))
while len(q) != 0:
    pop = q.popleft()
    if pop[1] != n-1:
        q.append((pop[0] | (a[pop[1]+1]), pop[1]+1))
        q.append((pop[0] ^ (a[pop[1]+1]), pop[1]+1))
    else:
        ans.append(pop[0])
print(min(ans))



