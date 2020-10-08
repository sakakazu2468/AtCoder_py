a, b = map(int, input().split())
count = 1
ll = a
if b == 1:
    print(0)
else:
    while b > ll:
        count += 1
        ll += a-1
    print(count)