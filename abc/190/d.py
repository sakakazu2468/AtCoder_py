n = int(input())
if n==1:
    print(2)
else:
    sums = []
    sumnum = 0
    for i in range(10**7):
        sumnum += i
        sums.append(sumnum)

    count = 0
    flag = 0
    for i in range(10**7):
        if (n-sums[i]) >= 0:
            if (n-sums[i]) == 0:
                flag = 1
            if (n-sums[i])%(i+1) == 0:
                count += 1

    if flag:
        print(count*2-2)
    else:
        print(count*2)

