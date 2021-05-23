a, b, k, l = map(int, input().split())
if a*l < b:
    print(a*k)
else:
    box = k//l
    rem = k-box*l
    ans = box*b
    if rem*a < b:
        print(ans+rem*a)
    else:
        print(ans+b)
