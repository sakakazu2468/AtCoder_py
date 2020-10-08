n = int(input())
count = 0
for i in range(1, n+1):
    if 10 <= i <= 99 or 1000 <= i <= 9999 or i == 100000:
        continue
    count += 1
print(count)