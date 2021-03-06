n, k = map(int, input().split())
possible = []
for i in range(2, 2*n+1):
    plus = i
    minus = i-k
    if minus >= 2:
        possible.append([plus, minus])

ans = 0
print(possible)
for i in range(len(possible)):
    poss_plus = possible[i][0]+1
    poss_plus -= max(0, (possible[i][0]-n))*2
    if poss_plus == possible[i][0]+1:
        poss_plus -= 2
    if poss_plus < 0:
        poss_plus = 0

    poss_minus = possible[i][1]+1
    poss_minus -= max(0, (possible[i][1]-n))*2
    if poss_minus == possible[i][1]+1:
        poss_minus -= 2
    if poss_minus < 0:
        poss_minus = 0

    ans += poss_plus * poss_minus

print(ans)
