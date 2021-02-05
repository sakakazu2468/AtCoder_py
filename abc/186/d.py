import heapq

n = int(input())
a = list(map(int, input().split()))
heapq.heapify(a)
keisu = -1*(n-1)
ans = 0
for i in range(n):
    ans += keisu*heapq.heappop(a)
    keisu += 2 
print(ans)
