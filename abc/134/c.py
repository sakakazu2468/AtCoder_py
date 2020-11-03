n = int(input())
a = []
max_num = -1
mode_max = False
for i in range(n):
    ipt = int(input())
    if ipt == max_num:
        mode_max = True
        a.append(ipt)
    else:
        max_num = max(ipt, max_num)
        a.append(ipt)
if mode_max:
    for i in range(n):
        print(max_num)
else:
    a_copy = a[:]
    idx = a.index(max_num)
    a_copy.remove(max_num)
    sub_max = max(a_copy)
    for i in range(n):
        if i == idx:
            print(sub_max)
        else:
            print(max_num)