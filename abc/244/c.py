n = int(input())
rem = [0 for i in range(2*n+1)]
num = 0
while True:
    for i in range(len(rem)):
        if rem[i] == 0:
            print(i+1)
            rem[i] = 1
            break
    if all(rem) == 1:
        break
    aoki = int(input())-1
    rem[aoki] = 1
    
