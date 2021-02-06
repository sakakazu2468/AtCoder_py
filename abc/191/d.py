import math

x, y, r = map(float, input().split())

if int(y+r) > y+r:
    upper_y = int(y+r)-1
else:
    upper_y = int(y+r)
if int(y-r) < y-r:
    lower_y = int(y-r)+1
else:
    lower_y = int(y-r)

count = 0
for inty in range(lower_y, upper_y+1):
    y2 = (inty*(10**4)-int(y*(10**4)))**2
    r2 = (int(r*(10**4)))**2
    root = math.sqrt(r2-y2)
    if int((x*(10**4)+root)/(10**4)) > (x*(10**4)+root)/(10**4):
        intx_p = int((x*(10**4)+root)/(10**4))-1
    else:
        intx_p = int((x*(10**4)+root)/(10**4))
    if int((x*(10**4)-root)/(10**4)) < (x*(10**4)-root)/(10**4):
        intx_m = int((x*(10**4)-root)/(10**4))+1
    else:
        intx_m = int((x*(10**4)-root)/(10**4))
    count += intx_p - intx_m + 1

print(count)
