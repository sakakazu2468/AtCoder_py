n, q = map(int, input().split())
nxt = [-1 for i in range(n)]
prv = [-1 for i in range(n)]

for i in range(q):
    ipt = list(map(int, input().split()))
    if ipt[0]==1:
        x = ipt[1] - 1
        y = ipt[2] - 1
        nxt[x] = y
        prv[y] = x
    elif ipt[0]==2:
        x = ipt[1] - 1
        y = ipt[2] - 1
        nxt[x] = -1
        prv[y] = -1
    else:
        head = ipt[1]-1
        while True:
            if prv[head] == -1:
                break
            head = prv[head]
        ans = []
        while True:
            ans.append(str(head+1))
            head = nxt[head]
            if head==-1:
                break
        print(len(ans), " ".join(ans))
