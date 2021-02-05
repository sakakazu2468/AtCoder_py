import heapq

n = int(input())
aoki = 0
takahashi = 0
eva_heap = []
for i in range(n):
    a, b = map(int, input().split())
    aoki += a
    eva_heap.append([-1*(2*a+b), a, b])

heapq.heapify(eva_heap)

for i in range(n):
    pop = heapq.heappop(eva_heap)
    takahashi += pop[1] + pop[2] 
    aoki -= pop[1]
    if takahashi > aoki:
        print(i+1)
        break
