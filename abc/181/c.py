n = int(input())
point = []
line = []
ans = 0
xline = []

for i in range(n):
    x, y = map(int, input().split())
    point.append([x, y])

for i in range(n):
    for j in range(n-1-i):
        j_idx = j+i+1
        if point[i][0]-point[j_idx][0] == 0:
            # xline.append(point[i][0])
            for k in range(n):
                if (point[i][0] == point[k][0]) and (k != i and k != j_idx):
                    ans += 1
        else:
            a = (point[i][1]-point[j_idx][1])/(point[i][0]-point[j_idx][0])
            b = -a*point[i][0]+point[i][1]
            # line.append([a, b])
            for k in range(n):
                xp = point[k][0]
                yp = point[k][1]
                if (yp == a*xp+b) and (k != i and k != j_idx):
                    ans += 1



# for i in range(len(line)):
#     for j in range(n):
#         if yp == al*x+bl:
#             print(xp, yp)
#             ans += 1

if ans:
    print("Yes")
else:
    print("No")
