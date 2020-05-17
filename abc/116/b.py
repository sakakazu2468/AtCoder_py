s = int(input())

def f(n):
    if n%2 == 0:
        return n//2
    else:
        return 3*n+1
a = [s]
i = 1
while True:
    i += 1
    p = f(a[-1])
    if p in a:
        print(i)
        break
    a.append(p)
