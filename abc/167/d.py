n, k = map(int, input().split())
a = list(map(int, input().split()))
log = []
visited = [False for i in range(n)]
now = a[0]-1
loop = False
for i in range(k-1):
    if visited[now] == True:
        loop = True
        break
    log.append(now)
    visited[now] = True
    now = a[now]-1
else:
    print(now+1)
if loop:
    for i in range(len(log)):
        if log[i] == now:
            first = len(log[:i])
            log_list = log[i:]
            loop_num = len(log_list)
            break
    k -= first
    k %= loop_num
    print(log_list[k-1]+1)
