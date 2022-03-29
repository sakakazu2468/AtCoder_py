import heapq


n, w = map(int, input().split())
q = []
for i in range(n):
    a, b = map(int, input().split())
    a *= -1
    q.append((a, b))
heapq.heapify(q)

ans = 0
while len(q):
    pop = heapq.heappop(q)
    ans += -1*pop[0]*min(pop[1], w)
    w -= pop[1]
    if w < 0:
        break
print(ans)
