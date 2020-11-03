import queue


n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
day = [0 for i in range(1008)]
visited = [False for i in range(n*n)]
for i in range(n):
    visited[i*(n+1)] = True

serial = 0

def s2p(s):
    a0 = (s+1) // n
    a1 = (s+1) % (n*a0)
    return [a0, a1]


q = queue.LifoQueue
while not all(visited):
    if visited[serial]:
        serial += 1
    else:
        p1_0 = s2p(serial)[0]
        p1_1 = s2p(serial)[1]
        
        
        
        
        
        
        
        serial += 1