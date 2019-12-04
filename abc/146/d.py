n = int(input())
tree = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
ans = []
sub = [0 for i in range(n+1)]
k = 0
for i in range(n+1):
    color = 0
    for j in range(len(tree[i])):
        color += 1
        if color == sub[i]:
            color += 1
        ans.append(color)
        sub[tree[i][j]] = color
        if k < color:
            k = color
print(k)
for i in range(len(ans)):
    print(ans[i])
