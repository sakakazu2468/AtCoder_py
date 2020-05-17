n, a, b = map(int, input().split())
count = 0
for i in range(n+1):
    s = 0
    for j in str(i):
        s += int(j)
    if a <= s <= b:
        count += i
print(count)
