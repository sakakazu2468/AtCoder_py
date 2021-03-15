n, k = map(int, input().split())
table = [0 for i in range(10**5+10)]
for i in range(n):
    a, b = map(int, input().split())
    table[a] += b

order = 0
for i in range(len(table)):
    order += table[i]
    if order >= k:
        print(i)
        break
