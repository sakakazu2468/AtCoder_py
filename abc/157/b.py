a = []
for i in range(3):
    a.append(list(map(int, input().split())))
n = int(input())
bingo = [[0 for i in range(3)] for i in range(3)]
for i in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if a[j][k] == b:
                bingo[j][k] = 1
if sum(bingo[0])==3 or sum(bingo[1])==3 or sum(bingo[2])==3 or (bingo[0][0] and bingo[1][0] and bingo[2][0]) or (bingo[0][1] and bingo[1][1] and bingo[2][1]) or (bingo[0][2] and bingo[1][2] and bingo[2][2]) or (bingo[0][0] and bingo[1][1] and bingo[2][2]) or (bingo[0][2] and bingo[1][1] and bingo[2][0]):
    print("Yes")
else:
    print("No")
