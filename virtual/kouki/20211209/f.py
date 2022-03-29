s = input()
abc = [0, 0, 0]
for c in s:
    if c=="a":
        abc[0] += 1
    elif c=="b":
        abc[1] += 1
    else:
        abc[2] += 1

if (abs(abc[0]-abc[1]) < 2) and (abs(abc[1]-abc[2]) < 2) and (abs(abc[2]-abc[0]) < 2):
    print("YES")
else:
    print("NO")
