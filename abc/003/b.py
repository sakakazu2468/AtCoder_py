s = input()
t = input()
wild = ['a', 't', 'c', 'o', 'd', 'e', 'r', '@']
for i in range(len(s)):
    if s[i] != t[i]:
        if s[i] == '@' and t[i] in wild:
            pass
        elif s[i] in wild and t[i] == '@':
            pass
        else:
            print("You will lose")
            break
else:
    print("You can win")
