s = input()
if len(s) < 4:
    print(0)
elif len(s) == 4:
    if int(s)%2019 == 0:
        print(1)
    else:
        print(0)
else:
    ruiseki = [0]
    for i in s:
        ruiseki.append(ruiseki[-1]+int(i))
    for i in range(4):
        ruiseki[i] = 1
    count = 0
    for i in range(len(ruiseki)):
        if ruiseki[i]%3 == 0:
            count += 1
    minus = 0
    for i in range(len(s)-4):
        n = int(s[i:i+4]) 
        print(n)
        if n < 2019 and n%2019 == 0:
            minus += 1
    print(count*(count-1)//2-minus)
    print(ruiseki)


