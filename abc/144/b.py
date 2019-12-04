n = int(input())
for i in range(9):
    if n%(i+1) == 0:
        if n//(i+1) < 10:
            print("Yes")
            break
else:
    print("No")
