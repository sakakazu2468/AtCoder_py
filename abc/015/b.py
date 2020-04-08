import math

n = int(input())
a = list(map(int, input().split()))
count = 0
total = 0
for i in a:
    if i != 0:
        count += 1
        total += i
print(math.ceil(total/count))
