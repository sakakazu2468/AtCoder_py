n = int(input())
xhouse = []
yhouse = []
for i in range(n):
    x, y = map(int, input().split())
    xhouse.append([x, i])
    yhouse.append([y, i])

xhouse.sort()
yhouse.sort()

ans_list = []
ans_list.append([abs(xhouse[0][0]-xhouse[-1][0]), sorted([xhouse[0][1], xhouse[-1][1]])])
ans_list.append([abs(xhouse[1][0]-xhouse[-1][0]), sorted([xhouse[1][1], xhouse[-1][1]])])
ans_list.append([abs(xhouse[0][0]-xhouse[-2][0]), sorted([xhouse[0][1], xhouse[-2][1]])])
ans_list.append([abs(yhouse[0][0]-yhouse[-1][0]), sorted([yhouse[0][1], yhouse[-1][1]])])
ans_list.append([abs(yhouse[1][0]-yhouse[-1][0]), sorted([yhouse[1][1], yhouse[-1][1]])])
ans_list.append([abs(yhouse[0][0]-yhouse[-2][0]), sorted([yhouse[0][1], yhouse[-2][1]])])
    
ans_list.sort()
most = ans_list[-1][1]
ans_list = ans_list[:-1]
while True:
    if ans_list[-1][1] != most:
        print(ans_list[-1][0])
        break
    else:
        ans_list = ans_list[:-1]

