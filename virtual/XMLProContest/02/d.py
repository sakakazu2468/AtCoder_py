n, m = map(int, input().split())
name = input()
kit = input()

namelist = [0 for i in range(26)]
for char in name:
    namelist[ord(char)-65] += 1
print(namelist)

ans = 0
kits = list(kit)
ans += 1
brk = False
for i in range(26):
    for j in range(namelist[i]):
        if chr(i+65) in kit:
            if chr(i+65) in kits:
                kits.remove(chr(i+65))
            else:
                kits += list(kit)
                kits.remove(chr(i+65))
                ans += 1
            print(kits)
        else:
            print(-1)
            brk = True
            break
    if brk:
        break
if not brk:
    print(ans)



