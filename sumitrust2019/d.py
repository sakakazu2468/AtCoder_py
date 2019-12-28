n = int(input())
new_s = input()
# new_s = ""
# for i in range(len(s)):
#    if i<3:
#        new_s+=s[i]
#     else:
#         if s[i-1] == s[i] and s[i-2] == s[i]:
#             pass
#         else:
#             new_s+=s[i]
pas = -1
ans = 0
lens = len(new_s)
for i in range(1000):
    ott = 0
    pas = int(pas)+1
    if pas < 10:
        pas = "00"+str(pas)
    elif pas < 100:
        pas = "0"+str(pas)
    pas = str(pas)
    idx = -1
    while idx < lens-1:
        idx += 1
        if ott == 0:
            if pas[0] == new_s[idx]:
                ott += 1
        elif ott == 1:
            if pas[1] == new_s[idx]:
                ott += 1
        elif ott == 2:
            if pas[2] == new_s[idx]:
                ott += 1
                ans += 1
        if ott == 3:
            break
print(ans)

