x = int(input())
if x < 100:
    print(0)
else:
    s = x//100
    r = x%100
    s5 = r//5
    r5 = r%5
    if r == 0:
        print(1)
    else:
        if r5 == 0:
            if s5 <= s:
                print(1)
            else:
                print(0)
        else:
            if s5+1 <= s:
                print(1)
            else:
                print(0)


