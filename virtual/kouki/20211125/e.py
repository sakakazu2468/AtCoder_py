from itertools import combinations


n = int(input())
MARCH = [0, 0, 0, 0, 0]
for i in range(n):
    s = input()
    if s[0] == "M":
        MARCH[0] += 1
    elif s[0] == "A":
        MARCH[1] += 1
    elif s[0] == "R":
        MARCH[2] += 1
    elif s[0] == "C":
        MARCH[3] += 1
    elif s[0] == "H":
        MARCH[4] += 1

ans = 0
for per in combinations(MARCH, 3):
    mult = 1
    for p in per:
        mult *= p
    ans += mult
print(ans)
