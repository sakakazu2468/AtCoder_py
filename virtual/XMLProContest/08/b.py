n = int(input())
xy = []
for i in range(n):
    xy.append(list(map(int, input().split())))
max_dis = 0
for i in range(n):
    for j in range(i+1, n):
        max_dis = max(max_dis, (xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2)
print(max_dis**0.5)
        
