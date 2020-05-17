n = int(input())
y = False
for i in range(16):
    for j in range(26):
        if i*7 + j*4 == n:
            print("Yes")  
            y = True
            break
    if y:
        break
else:
    print("No")
