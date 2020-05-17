x = int(input())
sq = []
for i in range(10**3):
    sq.append(i**5)
    sq.append(-i**5)
b = False
for i in range(len(sq)):
    for j in range(len(sq)-i):
        if sq[-i-1]-sq[j] == x:
            if i%2 == 0:
                m = -1
            else:
                m = 1
            if j%2 == 0:
                n = 1
            else:
                n = -1
            print(m*(1000-(i//2+1)), n*(j//2))
            b = True
            break
    if b:
        break

