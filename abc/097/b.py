x = int(input())
li = [1]
for i in range(100):
    n = 2
    while x >= (i+2)**n:
        li.append((i+2)**n)
        n += 1
print(max(li))

