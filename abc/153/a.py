h, a = map(int, input().split())
if h%a:
    print(h//a+1)
else:
    print(h//a)
