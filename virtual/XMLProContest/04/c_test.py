import heapq

n = int(input())
d = list(map(int ,input().split()))
m = int(input())
t = list(map(int ,input().split()))
sort_d = sorted(d)
sort_t = sorted(t)
bad = False
for i in range(m):
    t_pop = sort_t.pop()
    while True:
        d_pop = sort_d.pop()
        if d_pop == t_pop:
            break
        elif d_pop < t_pop:
            bad = True
            break
        elif len(sort_d) <= 0:
            bad = True
            break
    if bad:
        print("NO")
        break
else:
    print("YES")

