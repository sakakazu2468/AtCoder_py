import numpy as np


n = int(input())
table = [[0 for i in range(n+10)] for j in range(n+10)]

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

ab_gcd = [0 for i in range(n+10)]
for i in range(1, n+1):
    for j in range(1, n+1):
        ret = gcd(i, j)
        table[i][j] = ret
        ab_gcd[ret] += 1

table = np.array(table)
ans = 0
for i in range(n+10):
    if ab_gcd[i] != 0:
        ans += int(np.sum(table[i, :]))*ab_gcd[i]
print(ans)

