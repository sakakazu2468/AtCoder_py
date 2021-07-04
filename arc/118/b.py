import math


k, n, m = map(int, input().split())
a = list(map(int, input().split()))
diff = []
floor = []
for i in range(k):
    per = a[i]*m/n
    per_floor = math.floor(per)
    per_ceil = math.ceil(per)
    floor.append(per_floor)
    diff.append(per_ceil-per)

rem = m - sum(floor)

plus1 = []
for i in range(k):
    plus1.append([abs((floor[i]+1)*n-a[i]*m)/m*n, i])
plus1.sort()
for i in range(rem):
    floor[plus1[i][1]] += 1

for i in range(len(floor)):
    print(floor[i], end=" ")
print()

