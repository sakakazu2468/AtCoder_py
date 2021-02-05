n = int(input())
point = []
for i in range(n):
    point.append(list(map(int, input().split())))

count = 0
for i in range(n-1):
    for j in range(i+1, n):
        x = point[i][0]-point[j][0]
        y = point[i][1]-point[j][1]
        if (-1 <= (y/x) <= 1):
            count += 1
print(count)

