n, x, y = map(int, input().split())
tree = [[] for i in range(n+10)]
for i in range(len(tree)):
    if 1 <= i <= n:
        if i == 1:
            tree[i].append(2)
        elif i == n:
            tree[i].append(n-1)
        else:
            tree[i].append(i-1)
            tree[i].append(i+1)
    if i == x:
        tree[i].append(y)
    elif i == y:
        tree[i].append(x)



