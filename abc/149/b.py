a, b, k = map(int, input().split())
if a > k:
    print(a-k, b)
else:
    if k-a > b:
        print(0, 0)
    else:
        print(0, a+b-k)

