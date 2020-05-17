import numpy as np


n, m, c = map(int, input().split())
b = list(map(int, input().split()))
b = np.array(b)
count = 0
for i in range(n):
    a = np.array(list(map(int, input().split())))
    if sum(a*b) + c > 0:
        count += 1
print(count)

