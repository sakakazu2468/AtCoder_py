a, b, c = map(int, input().split())
num = a
for i in range(b+1):
    if num % b == c:
        print("YES")
        break
    num += a
else:
    print("NO")
