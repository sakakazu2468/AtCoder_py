from itertools import permutations


n, k = map(int, input().split())
t = []
for i in range(n):
    t.append(list(map(int, input().split())))

perm = list(permutations([i+2 for i in range(n-1)]))

ans = 0
for i in range(len(perm)):
    prev = 1
    d = 0
    for j in range(len(perm[i])):
        d += t[prev-1][perm[i][j]-1]
        prev = perm[i][j]
    d += t[prev-1][0]
    if d == k:
        ans += 1
print(ans)



