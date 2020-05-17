s = input()
t = input()
for i in range(len(s)+5):
    if s == t:
        print("Yes")
        break
    s = s[-1] + s[:-1]
else:
    print("No")
