import numpy as np


n, d = map(int ,input().split())
x = []
sq = [i**2 for i in range(200)]
for i in range(n):
    x.append(list(map(int, input().split())))
x = np.array(x)
count = 0
for i in range(n):
    for j in range(i+1, n):
        if sum((x[i]-x[j])**2) in sq:
            count += 1
print(count)
