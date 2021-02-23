n = int(input())
a = list(map(int, input().split()))
if sum(a)%n != 0:
    print(-1)
else:
    ave = sum(a)//n
    island_count = 0
    people = 0
    bridge = 0
    for i in range(n):
        a[i] -= ave
        island_count += 1
        people += a[i]
        if people == 0:
            bridge += island_count-1
            island_count = 0
            people = 0
    print(bridge)



        

