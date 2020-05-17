n = int(input())
count = 0
for i in range(1, n+1):
    if i%2:
        j = 1
        div = 0
        while j <= i:
            if i%j==0:
                div += 1
            j += 1
        if div == 8:
            count += 1
print(count)

