s = input()
q = int(input())
ud = False
ud_count = 0
sub_s = ""
for i in range(q):
    query = list(input().split())
    if int(query[0]) == 1:
        ud = not(ud)
        ud_count += 1
    else:
        if (int(query[1])==1 and ud==False) or (int(query[1])==2 and ud==True):
            sub_s += query[2]
        else:
            s += query[2]
s = sub_s[::-1] + s
if ud_count%2:
    print(s[::-1])
else:
    print(s)
