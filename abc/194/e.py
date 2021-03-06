import heapq
n, m = map(int, input().split())
a = list(map(int, input().split()))
numbers = [0 for i in range(1500000+1)]
zero_heap = []
heapq.heapify(zero_heap)
ans = 10**7
for i in range(m):
    numbers[a[i]] += 1 
for i in range(len(numbers)):
    if numbers[i] == 0:
        heapq.heappush(zero_heap, i)
firstpop = heapq.heappop(zero_heap)
ans = min(firstpop, ans)
for i in range(m, n):
    add_num = a[i]
    numbers[add_num] += 1
       
    delete_num = a[i-m]    
    numbers[delete_num] -= 1
    if numbers[delete_num] == 0:
        ans = min(ans, delete_num)

print(ans)
