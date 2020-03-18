import math


a, b = map(int, input().split())
for i in range(100000):
    a_t = math.floor(i*0.08)
    b_t = math.floor(i*0.1)
    if a==a_t and b==b_t:
        print(i)
        break
else:
    print(-1)
