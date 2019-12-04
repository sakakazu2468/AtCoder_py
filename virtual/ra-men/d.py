import heapq

n , k = map(int, input().split())
sushi = []
heapq.heapify(sushi)
for i in range(n):
    t, d = map(int, input().split())
    s = (d, t)
    heapq.heappush(sushi, s)

for i in range(k):

