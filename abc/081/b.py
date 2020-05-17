import numpy as np


n = int(input())
a = list(map(int, input().split()))
a = np.array(a, int)
count = 0
while True:
    if not (a%2).any():
        a //= 2
        count += 1
    else:
        break
print(count)
