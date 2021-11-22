s, t = map(int, input().split())
a = 0
b = 0
c = 0
count = 0
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i+j+k <= s and i*j*k <= t:
                count += 1
print(count)
