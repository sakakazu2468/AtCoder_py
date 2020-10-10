t = int(input())

def mod(x):
    return x%1000000007

for i in range(t):
    n, a, b = map(int, input().split())
    af = max(a, b)
    bf = min(a, b)
    rem = n -(a+b)
    # ((n-(af-1))**2)*((n-(bf-1))**2)-(((af-bf)+1)**2)
    if rem < 0:
        print(0)
        break
    else:
        afa = mod((n-af+1)**2)
        bfa = mod((n-bf+1)**2)
        dis = mod((af-bf+1)**2)
        print(mod(mod(afa*bfa)-dis))