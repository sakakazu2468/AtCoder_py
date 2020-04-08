s = input()
same = False
count = 0
ans = ""
for i in range(len(s)):
    if i == 0:
        continue
    if same:
        if s[i] == s[i-1]:
            count += 1
        else:
            count += 1
            ans += str(s[i-1]) + str(count)
            same = False
            
    else:
        if s[i] == s[i-1]:
            same = True
            count = 1
        else:
            count = 1
            ans += str(s[i-1]) + str(count)
    if i == len(s)-1:
        if s[i] == s[i-1]:
            count += 1
            ans += str(s[i]) + str(count)
        else:
            count = 1
            ans += str(s[i]) + str(count)

print(ans)



    
