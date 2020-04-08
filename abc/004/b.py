c = []
for i in range(4):
    c.append(list(input().split()))

for i in range(3, -1, -1):
    for j in range(3, -1, -1):
        print(c[i][j], end="") 
        if j == 0:
            print('\n', end="")
        else:
            print(' ', end="")

