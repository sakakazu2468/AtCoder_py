n = int(input())
seg = []
for i in range(n):
    t, l, r = map(int, input().split())
    if t==1:
        pass
    elif t==2:
        r -= 0.5
    elif t==3:
        l += 0.5
    else:
        l += 0.5
        r -= 0.5
    seg.append([l, r])

count = 0
for i in range(n):
    for j in range(i+1, n):
        seg_i = seg[i]
        seg_j = seg[j]
        if (max(seg_i) < min(seg_j)) or (min(seg_i) > max(seg_j)):
            pass
        else:
            count += 1
print(count)
