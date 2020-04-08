import heapq
import numpy

n, k = map(int, input().split())
h = list(map(int, input().split()))

h = numpy.array(h)
h *= -1
h = list(h)
heapq.heapify(h)

for i in range(k):
    if i > n-1:
        break
    heapq.heappop(h)
print(sum(h)*-1)

