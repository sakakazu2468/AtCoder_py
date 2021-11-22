n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
table = [[0 for i in range(3010)] for j in range(n)]
PRIME = 998244353
for i in range(a[0], b[0]+1):
    table[0][i] = 1

for i in range(len(table[0])-1):
    table[0][i+1] += table[0][i]


for i in range(1, n):
    for j in range(a[i], b[i]+1):
        table[i][j] = table[i-1][j]
    for j in range(len(table[i])-1):
        table[i][j+1] = (table[i][j+1] + table[i][j]) % PRIME

print(table[-1][-1])
