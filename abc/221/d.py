import heapq


n = int(input())

q = []
heapq.heapify(q)

for i in range(n):
    a, b = map(int, input().split())
    heapq.heappush(q, [a, 1])
    heapq.heappush(q, [a+b, 0])

ans = [0 for i in range(n+1)]
playing = 0
day = 1
while len(q):
    pop = heapq.heappop(q)
    ans[playing] += pop[0]-day
    if pop[1] == 1:
        playing += 1
    else:
        playing -= 1

    while len(q):
        pop2 = heapq.heappop(q)
        if pop2[0] == pop[0]:
            if pop2[1] == 1:
                playing += 1
            else:
                playing -= 1
        else:
            heapq.heappush(q, pop2)
            break

    day = pop[0]

ans = list(map(str, ans[1:]))
print(" ".join(ans))
