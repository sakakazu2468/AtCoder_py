n = int(input())
tree = [[] for i in range(n)]
for i in range(n-1):
    a, b = map(lambda x: int(x)-1, input().split())
    tree[a].append(b)
    tree[b].append(a)

for i in range(n):
    if len(tree[i]) == n-1:
        print("Yes")
        break
else:
    print("No")
