import queue


n, x, y = map(int, input().split())
x, y = x-1, y-1
q = queue.Queue()

def push(p, d):
    global dis
    if dis[p] != 0:
        return
    else:
        dis[p] = d
        q.put(p)

ans = [0 for i in range(1, n)]
for i in range(n):
    d = 0
    dis = [0 for i in range(n)]
    q.put(i, d)
    while not q.empty():
        get = q.get()
        p = get
        d = dis[p]
        print(p)
        if p > 0:
            push(p-1, d+1)
        if p < n-1:
            push(p+1, d+1)
        if p == x:
            push(y, d+1)
        if p == y:
            push(x, d+1)
    for j in range(len(dis)):
        ans[dis[j]] += 1
for i in range(len(ans)):
    ans[i] = ans[i]//2

print(ans)
for i in ans[-2::-1]:
    print(i)
