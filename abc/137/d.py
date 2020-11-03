import heapq

n, m = (map(int, input().split()))
part = []
for i in range(n):
    a, b = map(int, input().split())
    part.append([a, b*-1])

part.sort()
# print(part)
idx = 0
takable = []
allmoney = 0

for i in range(m):
    if len(part) > idx:
        # print(part[idx])
        while part[idx][0] <= i+1:
            heapq.heappush(takable, part[idx][1])
            # print(takable, 0)
            idx += 1
            if len(part)-1 < idx:
                break
    if len(takable):
        pop = heapq.heappop(takable)
        # print(pop, 1)
        allmoney += pop*-1

print(allmoney)