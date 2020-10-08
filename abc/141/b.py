s = input()
but = False
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == 'L':
            but = True
    else:
        if s[i] == 'R':
            but = True
if but:
    print("No")
else:
    print("Yes")