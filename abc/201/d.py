from collections import deque


h, w = map(int, input().split())
a = []
for i in range(h):
    a.append(list(input()[:]))
INF = 10**4
dp = [[INF if (i+j)%2 == 0 else -1*INF for i in range(w)] for j in range(h)]
dp[0][0] = 0

def edge_check(y, x, h, w):
    ret = []
    if y != h-1:
        ret.append([y+1, x])
    if x != w-1:
        ret.append([y, x+1])
    return ret 

q = deque()
q.append((0, 0))
while len(q):
    pop = q.popleft()
    add = edge_check(pop[0], pop[1], h, w)
    t_a = sum(pop)%2
    for i in dp:
        print(i)
    for i in add:
        print(i[0], i[1])
        if a[i[0]][i[1]] == "+":
            if t_a == 0:
                dp[i[0]][i[1]] = max(dp[i[0]][i[1]], dp[pop[0]][pop[1]] + 1)
                q.append((i[0], i[1]))
            else:
                dp[i[0]][i[1]] = min(dp[i[0]][i[1]], dp[pop[0]][pop[1]] - 1)
                q.append((i[0], i[1]))
        else:
            if t_a == 0:
                dp[i[0]][i[1]] = max(dp[i[0]][i[1]], dp[pop[0]][pop[1]] - 1)
                q.append((i[0], i[1]))
            else:
                dp[i[0]][i[1]] = min(dp[i[0]][i[1]], dp[pop[0]][pop[1]] + 1)
                q.append((i[0], i[1]))
    print()

if dp[h-1][w-1] > 0:
    print("takahashi")
elif dp[h-1][w-1] < 0:
    print("aoki")
else:
    print('draw')


print(dp)
