n = int(input())
w = []
for i in range(n):
    s = input()
    if s in w:
        print("No")
        break
    else:
        if i != 0:
            if w[-1][-1] != s[0]:
                print("No")
                break
        w.append(s)
else:
    print("Yes")
