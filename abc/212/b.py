x = input()
if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
    print("Weak")
else:
    prev = int(x[0])
    for i in range(1, 4):
        if (prev+1)%10 != int(x[i]):
            print("Strong")
            break
        prev = int(x[i])
    else:
        print("Weak")

