n = int(input())
ans = 0
mount_size = 0
prev = 0
down = False
for i in range(n):
    h = int(input())
    if down and (prev < h):
        ans = max(ans, mount_size)
        mount_size = 2
        down = False
    elif (not down) and (prev > h):
        down = True
        mount_size += 1
    else:
        mount_size += 1
    prev = h
ans = max(ans, mount_size)
print(ans)


