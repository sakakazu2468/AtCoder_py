n, m = map(int, input().split())
sc = []
for i in range(m):
    sc.append(list(map(int, input().split())))
i = 10**(n-1)
if n==1:
    i = 0
no = False
while i<10**n:
    for j in range(m):
        if int(str(i)[sc[j][0]-1])==sc[j][1]:
            pass
        else:
            no = True
    if no == False:
        print(i)
        break
    else:
        i+=1
    no = False
else:
    print(-1)

