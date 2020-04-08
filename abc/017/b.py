x = input()
c = False
oku = ['o', 'k', 'u']
for i in x:
    if c == True:
        if i != 'h':
            print("NO")
            break
        else:
            c = False 
            continue
    if i == 'c':
        c = True
    elif not i in oku:
        print("NO")
        break
else:
    print("YES")
