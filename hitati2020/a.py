s = input()
if len(s)%2 == 0:
    for i in range(len(s)):
        if i%2==0 and s[i] != 'h':
            print("No")
            break
        if i%2==1 and s[i] != 'i':
            print("No")
            break
    else:
        print("Yes")
else:
    print("No")
    
