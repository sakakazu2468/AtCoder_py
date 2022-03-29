a, b, c = map(int, input().split())
if c-a-b < 0:
    print("No")
else:
    l = (c-a-b)**2
    r = 4*a*b
    if l > r:
        print("Yes")
    else:
        print("No")

