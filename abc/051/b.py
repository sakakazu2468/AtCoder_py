k, s = map(int, input().split())
count = 0
for i in range(k+1):
    rem = s - i
    for j in range(rem+1):
        y, z = j, rem-j
        if y <= k and z <= k:
            if s == y+z+i:
                count += 1
print(count)
