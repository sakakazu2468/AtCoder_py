k = int(input())
a, b = map(int, input().split())
i = 0
while i*k <= b:
    if a <= i*k <= b:
        print("OK")
        break
    i += 1
else:
    print("NG")
