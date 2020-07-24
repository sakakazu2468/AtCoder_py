n = int(input())
a = list(map(int, input().split()))
q = int(input())
table = [0 for i in range(10**5+10)]
for i in range(n):
    table[a[i]] += 1

ans = 0
for i in range(len(table)):
    ans += table[i]*i

for i in range(q):
    b, c = map(int, input().split())
    ans = ans + table[b]*c - table[b]*b
    table[c] += table[b]
    table[b] = 0
    print(ans)


