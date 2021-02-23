s = input()
if s[0]==s[1]:
    print(1, 2)
else:
    for i in range(len(s)-2):
        first = s[i]
        second = s[i+1]
        last = s[i+2]
        if (first==second) or (second==last) or (last==first):
            print(i+1, i+3)
            break
    else:
        print(-1, -1)



