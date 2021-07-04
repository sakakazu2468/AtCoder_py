n = int(input())
bigtree = n+1
left = 1
right = 10**10
while True:
    center = (left+right)//2
    center_calc = (center+1)*center//2
    if center_calc > bigtree:
        right = center
    elif center_calc < bigtree:
        left = center
    if (left+1==right):
        smalls = left
        break
    if (bigtree==center_calc):
        smalls = center
        break
print(n+1-smalls)

