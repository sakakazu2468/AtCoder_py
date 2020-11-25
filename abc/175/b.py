n = int(input())
l = list(map(int, input().split()))
count = 0
if len(l) <= 2:
    print(0)
else:
    for i in range(len(l)-2):
        for j in range(len(l)-2-i):
            for k in range(len(l)-2-j-i):
                n1 = l[k+2+i+j]
                n2 = l[j+1+i]
                n3 = l[i]
                if (n1+n2 > n3) and (n1 != n2 and n2 != n3 and n1 != n3) and (n1+n3 > n2) and (n2+n3 > n1):
                    count += 1
    print(count)
