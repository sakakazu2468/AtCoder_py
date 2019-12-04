import heapq

n = int(input())
d = list(map(int, input().split()))
heapq.heapify(d)
if d[0] != 0:
    print(0)
else:
    pre = -1
    num = 0
    ans = 1
    count = True
    dif = 0
    for i in range(len(d)):
        if d[0] == 0:
            if i > 0:
                print(0)
                break
            else:
                pre = 0
                heapq.heappop(d)
                continue
        if d[0] == pre:
            num += 1
            if i == n-1:
                ans *= (pre-dif)**num
            heapq.heappop(d)
        elif d[0] - pre > 1:
            print(0)
            break
        else:
            if i == 1:
                num = 1
                pre = d[0]
                heapq.heappop(d)
                continue
            ans *= (pre-dif)**num
            pre = d[0]
            if i == n-1:
                ans *= pre
            if count:
                if num == 1:
                    dif += 1
                else:
                    count = False
            num = 1
            heapq.heappop(d)
    else:
        print(ans)
