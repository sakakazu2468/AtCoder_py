h, w = map(int, input().split())
if (h*w)%2 == 0:
    print((h*w)//2)
else:
    print((h*w)//2+1)
