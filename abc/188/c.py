import heapq

n = int(input())
a = list(map(lambda x:x*(-1), map(int, input().split())))
r = a[:n//2+1]
l = a[n//2+1:]
heapq.heapify(r)
heapq.heapify(l)
rnum = heapq.heappop(r)
lnum = heapq.heappop(l)
rnum *= -1
lnum *= -1
elem = min(rnum, lnum)
lside = 0
rside =  n
while True:


