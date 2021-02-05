n = int(input())
csf = []
for i in range(n-1):
    ipt = list(map(int, input().split()))
    csf.append(ipt)

for i in range(n-1):
    time = 0
    time += csf[i][1] + csf[i][0]
    for j in range(i+1, n-1):
        station_time = csf[j][1]
        dis = time - station_time
        if dis < 0:
            dis = 0
        if dis%csf[j][2] == 0:
            station_time += csf[j][2]*(dis//csf[j][2])
        else:
            station_time += csf[j][2]*(dis//csf[j][2]+1)
        time = station_time
        time += csf[j][0]
    print(time)
print(0)
        

        
