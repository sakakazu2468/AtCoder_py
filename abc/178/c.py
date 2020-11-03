n = int(input())

def mod(x):
    return x%(10**9+7)

def mult(n):
    if n==1:
        return 10
    elif n==0:
        return 1
    elif n<0:
        return 0
    elif n%2==0:
        return mod(mult(n//2)**2)
    else:
        return mod(mult(n//2)**2*10)



ans = mod(n*(n-1)) * mod(mult(n-2)) - n*(n-1)

print(mod(ans))

