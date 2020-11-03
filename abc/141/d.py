import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x*-1, a))
heapq.heapify(a)
for i in range(m):
    tar = heapq.heappop(a)
    ins = ((tar*-1) // 2)*-1
    heapq.heappush(a, ins)
a = list(map(lambda x: x*-1, a))
print(sum(a))
