from math import sqrt 


n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
d = []
for i in range(n):
    for j in range(i):
        dis = (l[i][0]-l[j][0])**2+(l[i][1]-l[j][1])**2
        d.append(sqrt(dis))
print(sum(d)/n*2)
        

