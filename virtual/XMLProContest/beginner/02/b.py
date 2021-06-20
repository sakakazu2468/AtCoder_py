n = int(input())
rbd = [0, 0, 0]
for i in range(n):
    s = input()
    for j in s:
        if j=="R":
            rbd[0] += 1
        elif j=="B":
            rbd[1] += 1
        else:
            rbd[2] += 1

if rbd[0] == rbd[1]:
    print("DRAW")
elif rbd[0] > rbd[1]:
    print("TAKAHASHI")
else:
    print("AOKI")
