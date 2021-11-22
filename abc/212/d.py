import heapq


q = int(input())
fukuro = []
heapq.heapify(fukuro)
minus = 0
minus_list = [0 for i in range(q)]
for i in range(q):
    query = input()
    if query[0] == "1":
        n, x = map(int, query.split())
        heapq.heappush(fukuro, [x-minus, i])
    elif query[0] == "2":
        n, x = map(int, query.split())
        minus += x
    else:
        pop = heapq.heappop(fukuro)
        print(pop[0]+minus)

    minus_list[i] = minus



