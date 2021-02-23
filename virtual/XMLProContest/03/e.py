s = input()
nico = "25"
cont = 0
ans = 0
nicoflag = False
for i in range(len(s)):
    if nicoflag:
        nicoflag = False
        continue
    if s[i:i+2] == nico:
        cont += 1
        nicoflag = True
    else:
        ans += cont*(cont+1)//2
        cont = 0
ans += cont*(cont+1)//2
print(ans)
