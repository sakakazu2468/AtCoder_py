from collections import deque


h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(input()[:])

visited = [[False for i in range(w)] for j in range(h)]
q = deque()
q.append([0, 0])
visited[0][0] = True

zero = False
ans = 1
for i in range(h+w-1):
    rbd = [0, 0, 0]
    while True:
        if len(q) != 0:
            pop = q.popleft()
            if pop[0]+pop[1] != i:
                q.appendleft([pop[0], pop[1]])
                break
            else:
                if s[pop[0]][pop[1]] == "R":
                    rbd[0] += 1
                elif s[pop[0]][pop[1]] == "B":
                    rbd[1] += 1
                else:
                    rbd[2] += 1
                if pop[0] != h-1 and visited[pop[0]+1][pop[1]] == False:
                    q.append([pop[0]+1, pop[1]])
                    visited[pop[0]+1][pop[1]] = True
                if pop[1] != w-1 and visited[pop[0]][pop[1]+1] == False:
                    q.append([pop[0], pop[1]+1])
                    visited[pop[0]][pop[1]+1] = True
        else:
            zero = True
            break

    if rbd[0]*rbd[1] != 0:
        print(0)
        break
    elif (rbd[0] | rbd[1]) == 0:
        ans *= 2
        ans %= 998244353

    if zero:
        print(ans)
        break
