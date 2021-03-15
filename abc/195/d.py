n, m, q = map(int, input().split())
nimotsu_ori = []
for i in range(n):
    w, v = map(int, input().split())
    nimotsu_ori.append([w, v])
nimotsu_ori.sort()
x = list(map(int, input().split()))
for i in range(q):
    l, r = map(lambda x:int(x)-1, input().split())
    x_copy = x[:l] + x[r+1:]
    x_copy.sort()
    nimotsu = nimotsu_ori[:]
    ans = 0
    if len(x_copy)!=0:
        nim_pop = nimotsu.pop(-1)
        x_pop = x_copy.pop(-1)
        while True:
            if x_pop >= nim_pop[0]:
                ans += nim_pop[1]
                if len(x_copy)==0:
                    break
                if len(nimotsu)==0:
                    break
                nim_pop = nimotsu.pop(-1)
                x_pop = x_copy.pop(-1)
            else:
                if len(x_copy)==0:
                    break
                if len(nimotsu)==0:
                    break
                nim_pop = nimotsu.pop(-1)
    print(ans)
