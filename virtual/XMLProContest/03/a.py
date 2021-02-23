t = input()
ans = ""
for i in range(len(t)):
    if t[i] == "?":
        ans += "D"
    else:
        ans += t[i]
print(ans)
