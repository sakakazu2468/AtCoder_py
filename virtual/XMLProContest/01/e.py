n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    a.append(list(input())[:])
for i in range(m):
    b.append(list(input())[:])

yesflag = False
for i in range(n-m+1):
    for j in range(n-m+1):
        brflag = False
        for k in range(m):
            for l in range(m):
                if a[i+k][j+l] != b[k][l]:
                    brflag = True
                    break
            if brflag:
                break
        if brflag != True:
            print("Yes")
            yesflag = True
            break
    if yesflag:
        break
else:
    print("No")


