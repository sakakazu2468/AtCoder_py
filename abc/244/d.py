s = list(input().split())
t = list(input().split())
same = 0
for si, ti in zip(s, t):
    if si == ti:
        same += 1
if same == 0 or same == 3:
    print("Yes")
else:
    print("No")
