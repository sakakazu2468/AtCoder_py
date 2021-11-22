n, m = map(int, input().split())
road = [[-1 for _ in range(n)] for _ in range(n)]
tree = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    road[a-1][b-1] = c
    tree[a-1].append(b-1)

def cost(s, t, k, boad):
    if s==t:
        return boad[t]
    for i in range(len(tree[s])):
        if tree[s][i] <= k or tree[s][i] == t:
            next_cost = boad[s]+road[s][tree[s][i]]
            if next_cost < boad[tree[s][i]]:
                if k==1:
                    print(next_cost, boad)
                boad[tree[s][i]] = next_cost
                return cost(tree[s][i], t, k, boad)

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            boad = [10**9 for _ in range(n)]
            visited = [False for _ in range(n)]
            boad[i] = 0
            ans_cost = cost(i, j, k, boad)
            if ans_cost:
                if ans_cost != 10**9:
                    print(ans_cost, i, j, k)
                    ans += ans_cost
print(ans)

print(road)
print(tree)