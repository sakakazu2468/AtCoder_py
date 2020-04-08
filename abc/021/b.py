n = int(input())
a, b = map(int, input().split())
k = int(input())
p = list(map(int, input().split()))
table = [0 for i in range(n)]
table[a-1] += 1
table[b-1] += 1
for i in range(len(p)):
    table[p[i]-1] += 1
if max(table) > 1:
    print("NO")
else:
    print("YES")
