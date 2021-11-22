n = 2**20
q = int(input())

ans = [-1 for _ in range(n)]
parents = [i for i in range(n)]

def mod(x):
    return x%n

def find_root(x):
    if parents[x] != x:
        parents[x] = find_root(parents[x])
    return parents[x]

for i in range(q):
    t, x = map(int, input().split())
    if t==1:
        find_root(mod(x))
        ans[parents[mod(x)]] = x
        parents[parents[mod(x)]] = mod(parents[parents[mod(x)]]+1)
    else:
        print(ans[mod(x)])
