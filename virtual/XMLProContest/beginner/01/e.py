x, k, d = map(int, input().split())
x = abs(x)
count = x//d
if count > k:
    print(x-d*k)
else:
    k -= count
    if k%2 == 0:
        print(x%d)
    else:
        print(d-(x%d))

        

