s1 = input()
s2 = input()
if s1[0] == s2[1] and s2[1] == ".":
    print("No")
elif s1[1] == s2[0] and s2[0] == ".":
    print("No")
else:
    print("Yes")
