s = input()
count = 0
for i in s:
    if i == 'R':
        count += 1
if s[1] == 'S' and count == 2:
    print(1)
else:
    print(count)
