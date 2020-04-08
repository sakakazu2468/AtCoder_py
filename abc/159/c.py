l = int(input())
if l%3 == 0:
    print((l//3)**3)
else:
    t = l//3
    if l%3 == 1:
        print(t**3+t**2+t/3+1/27)
    else:
        print(t**3+2*t**2+4*t/3+8/27)
