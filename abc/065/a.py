x, a, b = map(int, input().split())
if a>=b:
    print("delicious")
else:
    if b-a>x:
        print("dangerous")
    else:
        print("safe")
