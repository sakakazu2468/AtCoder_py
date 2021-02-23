x = input()
d = -1
for i in x:
    d = max(d, int(i))
m = int(input())

l = d + 1
r = 10**100
while True:
    center = (l+r)//2
    base_center = 0
    for i in range(len(x)):
        base_center += int(x[i])*(center**(len(x)-i-1))
    if base_center <= m:
        l = center
    elif base_center > m:
        r = center
    if l+1 == r:
        break

base_left = 0
for i in range(len(x)):
    base_left += int(x[i])*(l**(len(x)-i-1))
base_right = 0
for i in range(len(x)):
    base_right += int(x[i])*(r**(len(x)-i-1))
if len(x) == 1:
    if int(x) > m:
        print(0)
    else:
        print(1)
elif base_left>m:
    print(0)
else:
    print(l-d)
