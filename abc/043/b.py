s = input()
ans = ""
for i in s:
    if i == '0':
        ans += '0'
    elif i == '1':
        ans += '1'
    else:
        if ans == "":
            pass
        else:
            ans = ans[:len(ans)-1]
print(ans)
