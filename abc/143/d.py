import heapq

n = int(input())
l = list(map(int, input().split()))

heapq.heapify(l)
count = 0

print((n-2)*(n-3)/2-count)
