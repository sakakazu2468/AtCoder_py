import heapq


n, d = map(int, input().split())
ql = []
qr = []
heapq.heapify(ql)
heapq.heapify(qr)
for i in range(n):
    l, r = map(int, input().split())
    heapq.heappush(ql, (l, i))
    heapq.heappush(qr, (r, i))

used = [False for i in range(n)]
ans = 0
while len(qr):
    while len(qr):
        pop = heapq.heappop(qr)
        if used[pop[1]] == False:
            ans += 1
            used[pop[1]] = True
            break
    if len(qr) == 0:
        break
    rng = pop[0] + d - 1
    while len(ql):
        lpop = heapq.heappop(ql)
        if lpop[0] > rng and used[lpop[1]] == False:
            heapq.heappush(ql, lpop)
            break
        else:
            used[lpop[1]] = True

print(ans)
