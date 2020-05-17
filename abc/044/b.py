w = input()
cs = [0 for i in range(26)]
for i in w:
    cs[ord(i)-97] += 1
for i in cs:
    if i%2:
        print("No")
        break
else:
    print("Yes")
