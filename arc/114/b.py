n = int(input())
f = list(map(int, input().split()))
f = [0] + f
f_visited = [False for i in range(n+1)]
f_visited[0] = True
single = 0
for i in range(1, n+1):
    if f_visited[i]:
        continue
    start = i
    next_idx = f[i]
    f_visited[i] = True
    while True:
        if f_visited[next_idx]:
            if next_idx==start:
                single += 1
                break
            else:
                f_visited[next_idx] = False
                break
        else:
            f_visited[next_idx] = True
            next_idx = f[next_idx]
        print(f_visited)
print((2**single)%988244353-1)
