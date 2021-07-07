a, b, c, d = map(int, input().split())
if c*d <= b:
    print(-1)
else:
    blue = a
    red = 0
    count = 0
    while True:
        count += 1
        blue += b
        red += c
        if blue <= red*d:
            print(count)
            break

