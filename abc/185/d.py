import heapq

n, m = map(int, input().split())
if m == 0:
    print(1)
else:
    a = list(map(int, input().split()))
    heapq.heapify(a)
    state = 0
    mini = 10**10
    dif_list = []
    for i in range(len(a)):
        pop = heapq.heappop(a)
        dif = pop - state - 1
        if dif <= 0:
            dif = 10**10
        mini = min(dif, mini)
        if dif != 10**10:
            dif_list.append(dif)
        state = pop
    pop = n+1
    dif = pop - state - 1
    if dif <= 0:
        dif = 10**10
    mini = min(dif, mini)
    if dif != 10**10:
        dif_list.append(dif)
    state = pop
    count = 0
    for i in range(len(dif_list)):
        if dif_list[i]%mini == 0:
            count += dif_list[i]//mini
        else:
            count += dif_list[i]//mini + 1
    print(count)

