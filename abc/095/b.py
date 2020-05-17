n, x = map(int, input().split())
m = []
for i in range(n):
    m.append(int(input()))
count = n
x -= sum(m)
count += x//min(m)
print(count)
