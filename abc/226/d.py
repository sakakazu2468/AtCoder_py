from math import gcd


n = int(input())
ans = set()
town = []
for i in range(n):
    town.append(list(map(int, input().split())))


for i in range(n):
    for j in range(n):
        if i==j:
            continue
        x1 = town[i][0]-town[j][0]
        y1 = town[i][1]-town[j][1]
        x2 = town[j][0]-town[i][0]
        y2 = town[j][1]-town[i][1]
        g1 = gcd(x1, y1)
        g2 = gcd(x2, y2)
        ans.add((x1//g1, y1//g1))
        ans.add((x2//g2, y2//g2))
print(len(ans))

