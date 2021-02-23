import heapq

n = int(input())
d = list(map(int ,input().split()))
m = int(input())
t = list(map(int ,input().split()))
heapq.heapify(d)
heapq.heapify(t)
bad = False
for i in range(m):
    t_pop = heapq.heappop(t)
    while True:
        d_pop = heapq.heappop(d)
        if d_pop == t_pop:
            break
        elif d_pop > t_pop:
            bad = True
            break
        elif len(d) <= 0:
            bad = True
            break
    if bad:
        print("NO")
        break
else:
    print("YES")
