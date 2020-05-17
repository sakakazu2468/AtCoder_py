n = int(input())
d, x = map(int, input().split())
count = 0
for i in range(n):
    a = int(input())
    j = 0
    day = 1
    while day+j*a <= d:
        count += 1
        j += 1
print(count+x)

