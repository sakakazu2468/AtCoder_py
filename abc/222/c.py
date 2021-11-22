import heapq


def janken(x, y):
    if x == 'G':
        if y == 'G':
            return 0
        elif y == 'C':
            return 1
        else:
            return 2
    elif x == 'C':
        if y == 'G':
            return 2
        elif y == 'C':
            return 0
        else:
            return 1
    else:
        if y == 'G':
            return 1
        elif y == 'C':
            return 2
        else:
            return 0



n, m = map(int, input().split())
hand = []
for i in range(2*n):
    hand.append(input())

q = []
heapq.heapify(q)

for i in range(2*n):
    heapq.heappush(q, [0, i])

q2 = []
heapq.heapify(q2)
for i in range(m):
    if len(q):
        while len(q):
            pop1 = heapq.heappop(q)
            pop2 = heapq.heappop(q)
            res = janken(hand[pop1[1]][i], hand[pop2[1]][i])
            if res == 1:
                heapq.heappush(q2, [pop1[0]-1, pop1[1]])
                heapq.heappush(q2, [pop2[0], pop2[1]])
            elif res == 2:
                heapq.heappush(q2, [pop1[0], pop1[1]])
                heapq.heappush(q2, [pop2[0]-1, pop2[1]])
            else:
                heapq.heappush(q2, [pop1[0], pop1[1]])
                heapq.heappush(q2, [pop2[0], pop2[1]])
    else:
        while len(q2):
            pop1 = heapq.heappop(q2)
            pop2 = heapq.heappop(q2)
            res = janken(hand[pop1[1]][i], hand[pop2[1]][i])
            if res == 1:
                heapq.heappush(q, [pop1[0]-1, pop1[1]])
                heapq.heappush(q, [pop2[0], pop2[1]])
            elif res == 2:
                heapq.heappush(q, [pop1[0], pop1[1]])
                heapq.heappush(q, [pop2[0]-1, pop2[1]])
            else:
                heapq.heappush(q, [pop1[0], pop1[1]])
                heapq.heappush(q, [pop2[0], pop2[1]])

ans = [0 for i in range(2*n)]
if len(q):
    for i in range(2*n):
        pop = heapq.heappop(q)
        print(pop[1]+1) 
else:
    for i in range(2*n):
        pop = heapq.heappop(q2)
        print(pop[1]+1) 
