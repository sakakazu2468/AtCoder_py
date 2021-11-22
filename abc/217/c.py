n = int(input())
p = list(map(int, input().split()))
pp = []
for i in range(n):
    pp.append([p[i], i+1])
pp.sort()
for i in pp:
    print(i[1], end=" ")