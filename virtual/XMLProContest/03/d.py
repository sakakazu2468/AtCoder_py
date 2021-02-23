import heapq
n = int(input())
a = list(map(lambda x:int(x)*-1, input().split()))
heapq.heapify(a)
ans = 0
for i in range(2*n):
    pop = heapq.heappop(a)
    if i%2 != 0:
        ans += pop*-1

print(ans)
