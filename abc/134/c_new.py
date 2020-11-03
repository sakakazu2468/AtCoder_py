n = int(input())
a = []
max_num = -1
for i in range(n):
    ipt = int(input())
    if ipt > max_num:
        max_num = max(ipt, max_num)
        idx = i
    a.append(ipt)
a = sorted(a)
if a[-1] == a[-2]:
    for i in range(n):
        print(max_num)
else:
    for i in range(n):
        if i == idx:
            print(a[-2])
        else:
            print(max_num)