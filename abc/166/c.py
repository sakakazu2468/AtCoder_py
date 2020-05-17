n, m = map(int, input().split())
h = list(map(int, input().split()))
table = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    table[a-1].append(b-1)
    table[b-1].append(a-1)
count = 0
for i in range(len(table)):
    for j in range(len(table[i])):
        if h[table[i][j]] >= h[i]:
            break
    else:
        count += 1
print(count)

