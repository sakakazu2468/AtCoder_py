n = int(input())
s = list(map(int, input().split()))
poss = []
for i in range(1, 400):
    for j in range(1, 400):
        poss.append(4*i*j+3*i+3*j)
poss = list(set(poss))

ans = 0
for i in range(len(s)):
    if not s[i] in poss:
        ans += 1
print(ans)


