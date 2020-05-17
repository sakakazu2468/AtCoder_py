a, b = map(int, input().split())
s = input()
for i in range(len(s)):
    if i == a:
        if s[i] != '-':
            print("No")
            break
    else:
        if not s[i] in [str(i) for i in range(10)]:
            print("No")
            break
else:
    print("Yes")

