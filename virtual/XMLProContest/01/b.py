n = int(input())
d, x = map(int, input().split())
ans = 0
for i in range(n):
    a = int(input())
    day = 1
    count = 0
    while day <= d:
        count += 1
        day = a*count + 1
    ans += count
print(ans+x)

