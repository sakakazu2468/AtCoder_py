L, R = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
lshoes = [0 for i in range(50)]
rshoes = [0 for i in range(50)]
for i in range(L):
    lshoes[l[i]] += 1
for j in range(R):
    rshoes[r[j]] += 1

ans = 0
for i in range(len(lshoes)):
    ans += min(lshoes[i], rshoes[i])
print(ans)


