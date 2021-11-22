import heapq


n = int(input())

q = {}

for i in range(n):
    a, b = map(int, input().split())
    q[a] = q.get(a, 0) + 1
    q[a+b] = q.get(a+b, 0) - 1

ql = []
for key, value in q.items():
    ql.append([key, value])
ql.sort()

ans = [0 for i in range(n+1)]
playing = 0
day = 1
for i in range(len(ql)):
    ans[playing] += ql[i][0]-day
    playing += ql[i][1]
    day = ql[i][0]

ans = list(map(str, ans[1:]))
print(" ".join(ans))
