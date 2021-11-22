import math


n, m = map(int, input().split())
a = list(map(int, input().split()))
check = [False for i in range(10**5+10)]
for i in range(n):
    for j in range(1, math.ceil(math.sqrt(a[i]))):
        if a[i]%j == 0:
            check[j] = True
            check[a[i]//j] = True

for i in range(2, m+1):
    idx = i
    if check[idx] == True:
        while idx <= m+1:
            check[idx] = True
            idx += i

anslist = [1]
for i in range(2, m+1):
    if check[i] == False:
        anslist.append(i)

print(len(anslist))
for ans in anslist:
    print(ans)
