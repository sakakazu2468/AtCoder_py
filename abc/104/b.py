s = input()
small = [chr(i+97) for i in range(26)]
count = 0
for i in range(len(s)):
    if i == 0:
        if s[i] == 'A':
            continue
        else:
            print("WA")
            break
    elif i == 1:
        if not s[i] in small: 
            print("WA")
            break
    elif i == len(s)-1:
        if not s[i] in small:
            print("WA")
            break
    else:
        if s[i] == 'C':
            count += 1
        elif not s[i] in small:
            print("WA")
            break
else:
    if count == 1:
        print("AC")
    else:
        print("WA")
