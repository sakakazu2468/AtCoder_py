s = input()
lc = 0
for i in s:
    lc += 1
    if i == 'A':
        break
rc = 0
for i in s[::-1]:
    rc += 1
    if i == 'Z':
        break
print(len(s)-lc-rc+2)
