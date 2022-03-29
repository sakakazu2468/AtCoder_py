t = int(input())
for i in range(t):
    a, s = map(int, input().split())
    rem = s-a*2
    if 0 > rem:
        print("No")
    else:
        bi = [2**i for i in range(60)]
        bi.sort(reverse=True)
        for j in range(len(bi)):
            if a >= bi[j]:
                a -= bi[j]
                bi[j] = 0
        bi.sort(reverse=True)
        for j in range(len(bi)):
            if rem >= bi[j]:
                rem -= bi[j]
        if rem == 0:
            print("Yes")
        else:
            print("No")
