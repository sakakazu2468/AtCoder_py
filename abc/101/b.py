s = input()
n = int(s)
sn = 0
for i in range(len(s)):
    sn += int(s[i])
if n%sn:
    print("No")
else:
    print("Yes")
