n, m = map(int, input().split())
stu = []
for i in range(n):
    stu.append(list(map(int, input().split())))
chk = []
for i in range(m):
    chk.append(list(map(int, input().split())))
    
for i in range(n):
    near = 10**10
    for j in range(m):
        mht = abs(stu[i][0]-chk[j][0])+abs(stu[i][1]-chk[j][1])
        if near > mht:
            near = mht
            idx = j
    print(idx+1)
