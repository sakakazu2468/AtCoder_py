n = int(input())
p = 0
a = []
for i in range(n):
    a.append(int(input())-1)

count = 0
for i in range(n+10):
    count += 1
    p = a[p]
    if p == 1:
        print(count)
        break
else:
    print(-1)

