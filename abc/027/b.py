n = int(input())
a = list(map(int, input().split()))
if sum(a)%len(a) == 0:
    ave = sum(a)/len(a)
    d_sum = 0
    bridge = len(a)
    for i in a:
        d_sum += i - ave
        if d_sum == 0:
            bridge -= 1
    print(bridge)
else:
    print(-1)
