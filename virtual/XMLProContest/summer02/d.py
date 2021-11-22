n = int(input())
a = list(map(int, input().split()))
dic = {}
for i in range(n):
    dic[a[i]] = dic.get(a[i], 0) + 1
set_a = set(a)
kind = len(set_a)
list_set_a = list(set_a)
list_set_a.sort()
if 0 in a:
    if kind == 1:
        print("Yes")
    elif kind != 2:
        print("No")
    else:
        if dic[0]*2 == dic[list_set_a[-1]]:
            print("Yes")
        else:
            print("No")
elif kind == 3:
    if list_set_a[0]^list_set_a[1] == list_set_a[2]:
        if dic.get(list_set_a[0]) == dic.get(list_set_a[1]) and dic.get(list_set_a[1]) == dic.get(list_set_a[2]):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")
