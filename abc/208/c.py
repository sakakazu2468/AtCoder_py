n, k = map(int, input().split())
a = list(map(int, input().split()))
a_i = []
for i in range(n):
    a_i.append([a[i], i, 0])
a_i.sort()
count = k//n
rem = k%n
for i in range(n):
    a_i[i][2] += count
    if i < rem:
        a_i[i][2] += 1
    
counted = sorted(a_i, key=lambda x:x[1])
for elem in counted:
    print(elem[2])