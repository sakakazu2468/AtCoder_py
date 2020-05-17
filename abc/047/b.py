import numpy as np


w, h, n = map(int, input().split())
v = np.zeros((h, w), dtype=np.int)
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        v[:, :x] = 1
    elif a == 2:
        v[:, x:] = 1
    elif a == 3:
        v[:y, :] = 1
    else:
        v[y:, :] = 1
print(w*h-np.sum(v))

