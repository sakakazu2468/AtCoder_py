s = input()
t = input()
if s == t:
    print("Yes")
else:
    for i in range(len(s)-1):
        swap = s[:i]+s[i+1]+s[i]+s[i+2:]
        if swap == t:
            print("Yes")
            break
    else:
        print("No")
