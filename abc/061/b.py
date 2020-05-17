n, m = map(int, input().split())
table = [0 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    table[a-1] += 1
    table[b-1] += 1
for i in table:
    print(i)
