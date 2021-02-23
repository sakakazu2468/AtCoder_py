s = input()
for i in range(len(s)):
    if (i%2==0) and (97 <= ord(s[i]) <= 122):
        pass
    elif (i%2==1) and (65 <= ord(s[i]) <= 90):
        pass
    else:
        print("No")
        break
else:
    print("Yes")
    
